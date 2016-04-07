from __future__ import absolute_import, print_function, unicode_literals

import datetime
import subprocess
from codecs import open
from os import path

from setuptools import find_packages, setup
from setuptools.command.egg_info import egg_info as base_egg_info

from wagtailfontawesome import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class egg_info(base_egg_info):
    def run(self):
        self.compile_assets()
        base_egg_info.run(self)

    def compile_assets(self):
        try:
            subprocess.check_call(['npm', 'run', 'build'])
        except (OSError, subprocess.CalledProcessError) as e:
            print('Error compiling assets: ' + str(e))
            raise SystemExit(1)


setup(
    name='wagtailfontawesome',
    version=__version__,
    description='Add FontAwesome icons to StreamField.',
    long_description=long_description,
    url='https://github.com/alexgleason/wagtailfontawesome',
    author='Alex Gleason',
    author_email='alex@alexgleason.me',
    license='MIT',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
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
    cmdclass={'egg_info': egg_info},
)
