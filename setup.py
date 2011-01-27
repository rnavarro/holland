from setuptools import setup, find_packages
import sys, os

extra = {}
if sys.version_info >= (3, 0):
    extra.update(
        use_2to3=True,
        use_2to3_fixers=[]
    )

version = '1.1.0'

setup(
    name="holland",
    version=version,
    description="Holland Core Framework",
    long_description="""\
    This package provides the core functionality for
    performing backups along with a command line client interface.
    """,
    author="Rackspace",
    author_email="holland-discuss@lists.launchpad.net",
    url='http://www.hollandbackup.org',
    license="3-Clause BSD",
    packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
    include_package_data=True,
    zip_safe=False,
    test_suite='tests',
    install_requires=[
    ],
    entry_points="""
    # Scripts generated by setuptools
    [console_scripts]
    holland = holland.cli.main:holland

    # Holland subcommands
    [holland.commands]
    help            = holland.cli.cmd:Help
    listplugins     = holland.cli.cmd:ListPlugins
    listcommands    = holland.cli.cmd:ListCommands
    listbackups     = holland.cli.cmd:ListBackups
    backup          = holland.cli.cmd:Backup
    mk-config       = holland.cli.cmd:MakeConfig
    purge           = holland.cli.cmd:Purge

    [paste.paster_create_template]
    holland:backup  = holland.devtools:HollandBackupTemplate
    holland:stream  = holland.devtools:HollandStreamTemplate
    """,
    namespace_packages=['holland', 'holland.backup', 'holland.lib'],
    **extra
)
