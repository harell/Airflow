FROM puckel/docker-airflow:1.10.2

USER root
RUN groupadd --gid 999 docker \
    && usermod -aG docker airflow \
    &&pip install psycopg2 \
    && pip install psycopg2-binary
RUN apt-get update && \
    apt-get -y install sudo
RUN echo 'airflow:airflow' | chpasswd && adduser airflow sudo \
    && sudo gpasswd -a airflow docker

USER airflow