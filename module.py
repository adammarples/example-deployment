"""
example of module packaged with code in main function, accepting command line args.

"""

import argparse

def func1():
    pass 

def func2():
    pass 

def main(client_name=None, client_id=None, dry_run=None):
    print('function main has args:', client_name, client_id, dry_run)
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--client_name', type=str,
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

    #main(**vars(args)) <- this also works if you want to be less explicit