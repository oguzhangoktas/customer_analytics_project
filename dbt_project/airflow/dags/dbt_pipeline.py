from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 2, 1),
    'retries': 1
}

dag = DAG(
    dag_id='dbt_pipeline',
    default_args=default_args,
    schedule='@daily', 
    catchup=False
)

# dbt run task
dbt_run = BashOperator(
    task_id='run_dbt',
    bash_command='/home/airflow/.local/bin/dbt run --profiles-dir /opt/airflow/dbt',
    dag=dag
)

# DAG test
if __name__ == "__main__":
    dag.test()
