from __future__ import absolute_import, print_function, unicode_literals

import datetime
import io
import re
import subprocess
from os import path

from setuptools import find_packages, setup
from setuptools.command.egg_info import egg_info as base_egg_info

from wagtailfontawesome import __version__

RE_MD_CODE_BLOCK = re.compile(r'```(?P<language>\w+)?\n(?P<lines>.*?)```', re.S)
RE_LINK = re.compile(r'\[(?P<text>.*?)\]\((?P<url>.*?)\)')
RE_IMAGE = re.compile(r'\!\[(?P<text>.*?)\]\((?P<url>.*?)\)')
RE_TITLE = re.compile(r'^(?P<level>#+)\s*(?P<title>.*)$', re.M)
RE_CODE = re.compile(r'``([^<>]*?)``')

RST_TITLE_LEVELS = ['=', '-', '~']

GITHUB_REPOSITORY = 'https://github.com/alexgleason/wagtailfontawesome'


def md2pypi(filename):
    '''
    Load .md (markdown) file and sanitize it for PyPI.
    '''
    content = io.open(filename).read()

    for match in RE_MD_CODE_BLOCK.finditer(content):
        rst_block = '\n'.join(
            ['.. code-block:: {language}'.format(**match.groupdict()), ''] +
            ['    {0}'.format(l) for l in match.group('lines').split('\n')] +
            ['']
        )
        content = content.replace(match.group(0), rst_block)

    for match in RE_IMAGE.finditer(content):
        url = match.group('url')
        if not url.startswith('http'):
            url = '/'.join((GITHUB_REPOSITORY, 'raw/master', url))

        rst_block = '\n'.join([
            '.. image:: {0}'.format(url),
            '  :alt: {0}'.format(match.group('text'))
        ])
        content = content.replace(match.group(0), rst_block)

    content = RE_LINK.sub('`\g<text> <\g<url>>`_', content)
    content = RE_CODE.sub('``\g<1>``', content)

    for match in RE_TITLE.finditer(content):
        level = len(match.group('level')) - 1
        underchar = RST_TITLE_LEVELS[level]
        title = match.group('title')
        underline = underchar * len(title)

        full_title = '\n'.join((title, underline))
        content = content.replace(match.group(0), full_title)

    return content


# Get the long description from the README file
long_description = md2pypi('README.md')


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
