#!/usr/bin/env python

"""Check if we're using setuptools or ditutils if not available"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = ('pkiutils', 'argparse')

setup(name='gencsr',
    version='0.1b',
    description='Generates a CSR for creating your sits SSL certificate',
    long_description=open('README.md'),
    author='Doug Bromley',
    author_email='doug@tintophat.com',
    url='https://github.com/OdinsHat/gencsr',
    scripts=['gencsr.py'],
    license='BSD',
    keywords='ssl key csr openssl',
    platforms = 'any',
    setup_requires=requirements,
    install_requires=requirements,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Beta'
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)