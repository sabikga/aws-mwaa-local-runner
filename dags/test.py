from airflow.decorators import dag, task

default_args = {
    'owner': 'airflow',
}

@dag(default_args=default_args, schedule_interval="@daily", tags=['test'])
def dag_with_taskflow_api():
    
    @task()
    def print_hello():
        '''this function prints hello'''
        print('hello')
    t1 = print_hello()
dag_with_taskflow_api = dag_with_taskflow_api()

