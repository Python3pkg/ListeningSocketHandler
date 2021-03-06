import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

from pkg_resources import parse_requirements

req_fn = os.path.join(os.path.dirname(__file__), 'requirements.txt')
with open(req_fn) as f:
    requires = f.read().split()

setup(
    name='ListeningSocketHandler',
    version='0.1.1',
    author='Ben Cordero',
    author_email='bmc@linux.com',
    packages=['ListeningSocketHandler'],
    url='https://github.com/bencord0/ListeningSocketHandler',
    license='Apache License 2.0',
    description='The opposite of logging.handlers.SocketHandler',
    long_description=open('README.rst').read(),
    install_requires=parse_requirements(requires),
    test_suite="tests.get_tests",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Topic :: System :: Logging",
    ]
)
