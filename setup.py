from setuptools import find_packages, setup

setup(
    name='colaboratory-drive-sync',
    version='0.0',
    description='Helper functions for syncing with google drive folder',
    maintainer='Jaime McCandless',
    maintainer_email='jaime.m.mccandless@gmail.com',
    packages=find_packages(exclude=('tests',)),
    entry_points={
        'console_scripts': []
    },
    install_requires=(
        'pydrive',
        'google',
        'oath2client'
    ),
    include_package_data=True,   # See MANIFEST.in
)
