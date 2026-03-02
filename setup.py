try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='beancount-ethereum',
    version='2.0.0',
    description='Ethereum transaction importer for Beancount (v3 avec Beangulp)',
    packages=['beancount_ethereum'],
    license='GPLv3',
    install_requires=[
        'beancount>=3.2.0',
        'beangulp>=0.2.0'
    ]
)
