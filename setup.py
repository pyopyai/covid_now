from setuptools import setup, find_packages

setup(
    name='covid-now',
    version="0.0.1",
    description='',
    author='fujisawa',
    url='',
    install_requires=["requests"],
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts': "covid-now=covid_now.covid_now:main"
    }

)