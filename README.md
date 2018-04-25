## Example Code
For keeping core functionality in one place without relying on Jupyter as a
deployment environment.

### Argparse

helpful reference: https://stackoverflow.com/a/30493366/1910565

```python
#module.py

import argparse

def func1():
    """function that will be a part of your module, returns 1
    """
    return 1 

def func2():
    """function that will be a part of your module, returns 2
    """
    return 2 

def main(client_name=None, client_id=None, dry_run=None):
    """
    this is the main code that you want to keep in one place, it is the core
    of your module. This example just prints out its own arguments.

    """
    print('function main has args:', client_name, client_id, dry_run)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str,
                    help='A optional string argument')
    parser.add_argument('--client_id', type=str,
                    help='An optional string argument')
    parser.add_argument('--dry_run', action='store_true',
                    help='A boolean switch')

    args = parser.parse_args()

    main(
        client_name=args.client_name,
        client_id=args.client_id,
        dry_run=args.dry_run,
    )
```

#### Command line

```console
$ python module.py --client_name Santander --client_id 123 --dry_run
function main has args: Santander 123 True
```

#### Airflow

```python
#airflow_dag.py

import airflow

from module import main

dag = airflow.models.DAG(
    dag_id="example-dag",
    default_args={},
    )

task = airflow.operators.python_operator.PythonOperator(
    dag=dag,
    task_id='example-task-run-main',           
    python_callable=main,                   # main function imported above
    op_kwargs={                             # dict of args for python_callable
        'client_name': 'Santander',
        'client_id': 123,
        'dry_run': True,        
    },               
    dag=dag,
)
```

```console
$ airflow run example-dag example-task-run-main
function main has args: Santander 123 True
```

#### Cronjob

```bash
# crontab -e

# m h  dom mon dow   command
0 1 * * * /bin/bash python module.py --client_name Santander --client_id 123
```

#### Unit Tests

```python
#test_main.py

from unittest import TestCase

from module import func1, func2

class TestAccount(TestCase):

    def setUp(self):
        pass

    def test_func1(self):
        assert func1() == 1

    def test_func2(self):
        assert func2() == 2

    def tear_down(self):
        pass
```

```console
$ python -m unittest test_main
----------------------------------------------------------------------
Ran 2 tests in 0.001s

OK
```


#### Config file

If the number of command line arguments gets too great or is too complex, you
could use a config file. Provide an example.ini in your version control repository.

```ini
; example.ini

[DEFAULT]
client_name = Santander
client_id = 123
dry_run = true
```

```python
#module.py using config file

#main module code goes here

if __name__ == '__main__':

    import configparser  
    parser = configparser.ConfigParser()
    parser.read("example.ini")
    client_name = parser.get('DEFAULT','client_name')
    client_id = parser.get('DEFAULT','client_id')
    dry_run = parser.get('DEFAULT','dry_run')

    main(
        client_name=client_name,
        client_id=client_id,
        dry_run=dry_run,
    )
```


```console
$ python module.py
function main has args: Santander 123 True
```

#### Combining argparse and configparser

```python

#module.py using config file and giving the path as a command line argument

#main module code goes here

if __name__ == '__main__':

    import argparse
    import configparser
    
    argparser = argparse.ArgumentParser()
    confparser = configparser.ConfigParser()

    argparser.add_argument('--config_path', type=str,
                    help='A optional string argument')

    args = argparser.parse_args()
    confparser.read(args.config_path)

    client_name = confparser.get('DEFAULT','client_name')
    client_id = confparser.get('DEFAULT','client_id')
    dry_run = confparser.get('DEFAULT','dry_run')

    main(
        client_name=client_name,
        client_id=client_id,
        dry_run=dry_run,
    )
```

```console
$ python module.py --config_path /path/to/your/config.ini
function main has args: Santander 123 True
```


    