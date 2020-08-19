FROM python:3.7.9-slim-buster
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Install Airflow --------------------------------------------------------------
# <https://airflow.apache.org/docs/stable/installation.html>
RUN apt-get update && apt-get install -y --no-install-recommends \
    dos2unix \
    freetds-bin \
    git \
    krb5-user \
    ldap-utils \
    libffi6 \
    libsasl2-2 \
    libsasl2-modules \
    libssl1.1 \
    locales  \
    lsb-release \
    sasl2-bin \
    sqlite3 \
    unixodbc

RUN pip install \
    apache-airflow==1.10.10 \
    --constraint \
    https://raw.githubusercontent.com/apache/airflow/1.10.10/requirements/requirements-python3.7.txt
#RUN pip install \
#    apache-airflow[postgres,gcp]==1.10.10 \
#    --constraint \
#    https://raw.githubusercontent.com/apache/airflow/1.10.10/requirements/requirements-python3.7.txt
