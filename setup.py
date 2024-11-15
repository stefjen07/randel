from setuptools import find_packages, setup

setup(
    name='randel',
    version='0.1',
    description='A library for modeling random processes and variogram analysis',
    author='stefjen07',
    author_email='stefjen@mail.ru',
    url='https://github.com/stefjen07/randel',
    packages=find_packages(),
    install_requires=['numpy', 'scipy', 'matplotlib', 'pandas']
)