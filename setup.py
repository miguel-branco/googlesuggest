from setuptools import setup, find_packages

setup(
    name='googlesuggest',
    version='0.0.0',
    author=u'Miguel Branco',
    author_email='miguel.branco@epfl.ch',
    install_requires = [
        'psycopg2==2.5.2',
        'boto==2.27.0'
    ]
)
