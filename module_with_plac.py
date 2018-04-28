"""
example of module accepting command line arguments via plac.

ref: https://github.com/micheles/plac/blob/0.9.6/doc/plac.pdf

plac annotations are a 6-tuple of the form: (help, kind, abbrev, type, choices, metavar)

"""

import plac


@plac.annotations(
    client_name=('Client Name ie. Santander', 'positional', None, str),
    client_id=('Client ID ie. 123', 'positional', None, int),
    dry_run=('Dry run flag, True/False', 'flag', 'd', bool),
)
def main(client_name=None, client_id=None, dry_run=False):
    print('function main has args:', client_name, client_id, dry_run)
    print(type(client_id), type(dry_run))
    pass


if __name__ == '__main__':
    plac.call(main)
