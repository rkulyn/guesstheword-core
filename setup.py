"""`Guess The Word core` setup script."""

import re

from setuptools import setup


AUTHOR = 'Roman Kulynych'
AUTHOR_EMAIL = 'kulynych.r@gmail.com'

# Getting description:
with open('README.rst') as readme_file:
    description = readme_file.read()

# Getting version:
with open('src/guesstheword/__init__.py') as init_file:
    version = re.search('__version__ = \'(.*?)\'', init_file.read()).group(1)


setup(
    name='Guess The Word game core',
    version=version,
    description='Guess The Word game core module',
    long_description=description,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    url='https://github.com/rkulyn/guesstheword-core',
    packages=['guesstheword', 'guesstheword.examples'],
    package_dir={'': 'src'},
    zip_safe=True,
    license='BSD New',
    platforms=['any'],
    keywords=[
        'Guess The Word',
        'Word Game',
        'Game',
    ],
)
