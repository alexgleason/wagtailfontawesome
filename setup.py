from setuptools import setup, find_packages
from wagtailfontawesome import __version__
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

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
        "wagtail>=0.8.7",
        "Django>=1.7.1",
    ],
)
