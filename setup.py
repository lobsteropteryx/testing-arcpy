from setuptools import setup, find_packages

setup(
    name='my_project',
    version='1.0.0',
    description='Sample project for arcpy applications',
    url='https://github.com/lobsteropteryx/arcpy-testing',
    author='Ian Firkin',
    author_email='ian.firkin@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['arcpy'],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'pytest-watch', 'pylint']
    },
    entry_points={
        'console_scripts': []
    },
)