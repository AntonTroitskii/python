import pathlib
import click
from pathlib import Path

from ge_ct_reading_exams import read_exams, save_protocols_names

@click.group()
def cli():
    pass

@click.command()
@click.option('-i', type=pathlib.Path)
@click.option('-o', type=pathlib.Path)
def protocolslist(i, o):
    exams = read_exams(i)
    # click.echo(exams)
    save_protocols_names(o, exams)

    # click.echo(i)
    # click.echo(o)
    # click.echo('test')
# def protocolslist():
    # print(i)
    # print(o)
    # click.echo('test')

@click.command()
def protocolstable():
    pass

cli.add_command(protocolslist)
cli.add_command(protocolstable)

if __name__ == '__main__':
    cli()