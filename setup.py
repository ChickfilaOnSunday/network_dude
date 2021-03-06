from setuptools import setup

setup(
    name='network_dude',
    version='0.0.1',
    packages=['network_dude'],
    scripts=['bin/network-dude'],
    install_requires=[i.strip() for i in open('requirements.txt').readlines() if 'git' not in i],
    description='Continuous traffic processor from DARPA.',
    url='https://github.com/mechaphish/network_dude',
)
