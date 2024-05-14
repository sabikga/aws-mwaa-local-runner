from airflow.decorators import dag, task
import pendulum

default_args = {
    'owner': 'airflow',
}

@dag(default_args=default_args, start_date=pendulum.datetime(2024, 5, 12, tz="UTC"), schedule_interval="@daily", tags=['test'])
def test_dag_with_taskflow_api_2():
    
    @task()
    def print_hello():
        '''this function prints hello'''
        print('hello')
    t1 = print_hello()
test_dag_with_taskflow_api = test_dag_with_taskflow_api_2()

