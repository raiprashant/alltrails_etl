from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

from alltrails_dataset import df_to_csv

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 08, 13),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'alltrails_dag',
    default_args=default_args,
    description='DAG to process alltrails ETL!',
    schedule_interval=timedelta(days=1),
)

def just_a_function():
    print("I'm going to show you something :)")

run_etl = PythonOperator(
    task_id='alltrails_etl',
    python_callable=df_to_csv,
    dag=dag,
)

run_etl