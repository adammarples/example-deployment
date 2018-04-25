"""
example of module packaged with code in main function, accepting config file args.

"""

import configparser

def func1():
    pass 

def func2():
    pass 

def main(client_name=None, client_id=None, dry_run=None):
    print('function main has args:', client_name, client_id, dry_run)
    pass


if __name__ == '__main__':
    import configparser  
    parser = configparser.ConfigParser()
    parser.read("example.ini")
    client_name = parser.get('DEFAULT','client_name')
    client_id = parser.get('DEFAULT','client_id')
    dry_run = parser.get('DEFAULT','dry_run')

    main(client_name=client_name,
        client_id=client_id,
        dry_run=dry_run,
    )