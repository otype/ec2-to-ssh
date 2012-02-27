#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    setup script EC2-TO-SSH

    usage: sudo python setup.py install
"""

from distutils.core import setup
import os
from setuptools import find_packages
import version

required = ['boto']

extra_options = dict(
    # Nothing
)

DOWNLOAD_URL = 'https://github.com/downloads/otype/ec2-to-ssh/ec2-too-ssh-{0}.tar.gz'.format(version.__version__)

setup(
    name="ec2-to-ssh",
    version=version.__version__,
    description='ec2-to-ssh',
    author='Hans-Gunther Schmidt',
    author_email='hgs@cloudcontrol.de',
    url='https://www.cloudcontrol.com',
    install_requires=required,
    packages=find_packages('src'),
    package_dir={'': 'src'},
    scripts=['ec2-to-ssh', 'src/ec2-instances.py'],
    data_files=[
        (os.path.join(os.environ['HOME'], '.ec2ssh'), ['src/conf/settings.cfg'])
    ],
    download_url=DOWNLOAD_URL,
    license='Apache 2.0',
    **extra_options
)
