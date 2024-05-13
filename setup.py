from setuptools import find_packages, setup

setup(
    name='functions.gcexplain',
    packages=find_packages(include=['functions.gcexplain']),
    version='0.1.0',
    description='Library for using Granger causality for Feature Importance Estimation',
    author='Henrique Peixoto Machado',
    install_requires=['tensorflow==2.15.0', 'scikit-learn==1.2.2', 'pandas==2.0.3', 'numpy==1.25.2'],

)