import sys
import os.path as op

from setuptools import setup

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 3',
    'Programming Language :: Objective C',
    'Programming Language :: C',
    'Topic :: Desktop Environment :: File Managers',
]

setup(
    name='Send2Trash3k',
    version='1.0.2',
    author='Hardcoded Software',
    author_email='hsoft@hardcoded.net',
    packages=['send2trash'],
    scripts=[],
    url='http://hg.hardcoded.net/send2trash/',
    license='BSD License',
    description='Send file to trash natively under Mac OS X, Windows and Linux.',
    long_description=open('README').read(),
    classifiers=CLASSIFIERS,
    zip_safe=False,
)