"""Automate manual tasks."""
from fabric.api import local, task


@task
def docs():
    """Build the html and pdf documentations."""
    local("sphinx-build -b html source build")
    local("make html")
    local("make latexpdf")
