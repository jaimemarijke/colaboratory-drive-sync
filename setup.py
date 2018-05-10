import os

from setuptools import find_packages, setup

setup(
    name='colaboratory-drive-sync',
    version='0.0',
    description='Helper function to sync Google Drive files to Colaboratory',
    author='Jaime',
    maintainer='Jaime',
    maintainer_email='jaimemarijke@gmail.com',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    entry_points={
        'console_scripts': []
    },
    install_requires=(
        'pydrive',
        'google',
        'oauth2client'
    ),
)
