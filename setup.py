import os
from setuptools import setup, find_packages

long_desc = """
Opal Observations is a plugin for the Opal web framework that allows on to record
patient observations and visualise trends over time in Opal.

Source code and documentation available at https://github.com/openhealthcare/opal-observations/
"""

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='opal-observations',
    version='0.5.0',
    packages=find_packages(),
    include_package_data=True,
    license='GPL3',
    description='Opal Plugin for observations',
    long_description=long_desc,
    url='http://opal.openhealthcare.org.uk/',
    author='Open Health Care UK',
    author_email='hello@openhealthcare.org.uk',
)
