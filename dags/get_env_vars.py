import os
from airflow.operators.python import PythonOperator

def print_env_vars():
    keys = str(os.environ.keys()).replace("', '", "'|'").split("|")
    keys.sort()
    for key in keys:
        print(key)

get_env_vars_operator = PythonOperator(
    task_id='get_env_vars_task',
    python_callable=print_env_vars
)