from __future__ import absolute_import, print_function, unicode_literals

import datetime
import io
import re
import subprocess
from os import path

from setuptools import find_packages, setup
from setuptools.command.sdist import sdist as base_sdist
from setuptools.command.bdist_egg import bdist_egg as base_bdist_egg

from wagtailfontawesome import __version__

GITHUB_REPOSITORY = 'https://github.com/alexgleason/wagtailfontawesome'


with open('README.rst', 'r') as readme:
    long_description = readme.read()


class assets_mixin:
    def compile_assets(self):
        try:
            subprocess.check_call(['npm', 'run', 'build'])
        except (OSError, subprocess.CalledProcessError) as e:
            print('Error compiling assets: ' + str(e))
            raise SystemExit(1)


class sdist(base_sdist, assets_mixin):
    def run(self):
        self.compile_assets()
        base_sdist.run(self)


class bdist_egg(base_bdist_egg, assets_mixin):
    def run(self):
        self.compile_assets()
        base_bdist_egg.run(self)


setup(
    name='wagtailfontawesome',
    version=__version__,
    description='Add FontAwesome icons to StreamField.',
    long_description=long_description,
    url=GITHUB_REPOSITORY,
    author='Alex Gleason',
    author_email='alex@alexgleason.me',
    license='MIT',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    keywords='development',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "wagtail>=1.4.0",
        "Django>=1.7.1",
    ],
    cmdclass={
        'sdist': sdist,
        'bdist_egg': bdist_egg,
    },
)
