#!/usr/bin/env python

from setuptools import setup, find_packages

desc = ''
with open('README.md') as f:
    desc = f.read()

setup(
    name='paranuara',
    version='1.0.0',
    description=('paranuara'),
    long_description=desc,
    url='',
    author='',
    author_email='',
    license='Apache v2',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Hivery',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='',
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    install_requires=[
        'alchemize==0.13.2',
        'atomicwrites==1.3.0',
        'attrs==18.2.0',
        'aumbry==0.9.0',
        'deepmerge==0.0.5',
        'docopt==0.6.2',
        'falcon==1.4.1',
        'gunicorn==19.9.0',
        'mock==2.0.0',
        'mongoengine==0.16.3',
        'more-itertools==6.0.0',
        'pbr==5.1.2',
        'pike==0.1.1',
        'pluggy==0.8.1',
        'py==1.7.0',
        'pymongo==3.7.2',
        'pytest==4.2.1',
        'python-mimeparse==1.6.0',
        'PyYAML==3.13',
        'six==1.12.0'
    ],
    package_data={},
    data_files=[],
    entry_points={
        'console_scripts': [
            'paranuara = paranuara.__main__:main'
        ],
    },
)
