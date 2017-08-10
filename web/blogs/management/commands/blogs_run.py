# -*- coding: utf-8 -*-
import djclick as click


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.option('--host', default='localhost', help="host")
@click.option('--port', default=8000, help="port")
@click.option('--scheme', default='http', help="scheme")
@click.pass_context
def post_article(ctx, host, port, scheme):
    '''POST an Article'''
    import requests
    from datetime import datetime

    now = str(datetime.now())
    path = '{}://{}:{}/api/blogs/articles/'.format(scheme, host, port)
    res = requests.post(
        path, {
            'title': 'Sample Title ' + now,
            'body': 'Sample Body ' + now,
            'author': 1,
            'status': 1,
        })
    click.echo(res.json())
