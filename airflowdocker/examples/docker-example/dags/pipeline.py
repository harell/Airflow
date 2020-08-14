import json
from datetime import timedelta, datetime
import docker
import logging
from airflow import DAG
from airflow.models import Variable
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.python_operator import PythonOperator



# Config variables
# dag_config = Variable.get("bigquery_github_trends_variables", deserialize_json=True)
# BQ_CONN_ID = dag_config["bq_conn_id"]
# BQ_PROJECT = dag_config["bq_project"]
# BQ_DATASET = dag_config["bq_dataset"]

default_args = {
    'owner': 'airflow',
    'depends_on_past': True,    
    'start_date': datetime(2020, 5, 28),
    # 'end_date': datetime(2020, 5, 28),
    'email': ['airflow@airflow.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

# Set Schedule: Run pipeline once a day. 
# Use cron to define exact time. Eg. 8:15am would be "15 08 * * *"
schedule_interval = "00 21 * * *"
def do_test_docker():
    client = docker.APIClient()
    for image in client.images():
        logging.info(str(image))
# Define DAG: Set ID and assign default args and schedule interval
dag = DAG('docker_dag', default_args=default_args, schedule_interval=schedule_interval, catchup=False)

## Task 1: check that the github archive data has a dated table created for that date
# To test this task, run this command:
# docker-compose -f docker-compose-gcloud.yml run --rm webserver airflow test bigquery_github_trends bq_check_githubarchive_day 2018-12-01
t_date = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag
)
t_docker = DockerOperator(
    task_id='scraper',
    image='python:3.7',
    # auto_remove=True,
    # environment={
    #         'PYSPARK_PYTHON': "python3",
    #         'SPARK_HOME': "/spark"
    # },
    volumes=['/home/airflow/data:/home/data','/var/run/docker.sock:/var/run/docker.sock'],
    command='python3 /home/data/filename.py',
    docker_url='unix://var/run/docker.sock',
    network_mode='bridge',
    dag=dag
)

t_test = PythonOperator(
    task_id="test_docker",
    python_callable=do_test_docker,
    dag=dag
)

t_date >> t_docker >> t_test