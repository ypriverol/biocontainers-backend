#!/usr/bin/env python3

import click
import connexion
from pymodm import connect
from flask_cors import CORS

from biocontainers_flask.server import encoder

_PUBLIC_REGISTRY_URL = "http://biocontainers.pro/registry/"


def connect_to_db(db_name, db_host, db_auth_database, db_user, db_password, db_port):
    uri = 'mongodb://' + db_user + ":" + db_password + '@' + db_host + ':' + \
          db_port + '/' + db_name + '?ssl=false&authSource=' + db_auth_database
    connect(uri, 'default')


def print_help(ctx, param, value):
    if value is False:
        return
    click.echo(ctx.get_help())
    ctx.exit()


@click.command()
@click.option('-db', '--db-name', help="Name of the database", envvar='BIOCONT_DB_NAME')
@click.option('-h', '--db-host', help='Host the database', envvar='MONGODB_HOST')
@click.option('-a', '--db-auth-database', help='Authentication database in Mongo', envvar='MONGODB_ADMIN_DB')
@click.option('-u', '--db-user', help='Database root user', envvar='MONGODB_USER', default='admin')
@click.option('-pw', '--db-password', help='Database password', envvar='MONGODB_PASS')
@click.option('-p', '--db-port', help='Database port', envvar='MONGO_PORT', default='27017')
@click.option('--help', is_flag=True, expose_value=False, is_eager=False, callback=print_help,
              help="Print help message")
@click.pass_context
def main(ctx, db_name, db_host, db_auth_database, db_user, db_password, db_port):
    if (db_name is None) or (db_host is None) or (db_user is None):
        print_help(ctx, None, value=True)
    connect_to_db(db_name, db_host, db_auth_database, db_user, db_password, db_port)
    app = connexion.App(__name__, specification_dir='./swagger/')
    CORS(app.app, expose_headers='next_page, last_page, self_link, current_offset, current_limit')  # adds CORS support
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'GA4GH Tool Discovery API'})
    app.run(port=8090)


if __name__ == '__main__':
    main()
