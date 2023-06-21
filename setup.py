from logging import root
import os
import sys
from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess




class PostInstallCommand(install):
    def run(self):
        install.run(self)

class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)


if __name__ == '__main__':
    setup(
        name='TMscore',
        version='0.1.0',
        description='Compute TMscore',
        author='Xinyi',
        keywords='',
        packages=[
            'TMscore',
        ],
        python_requires = '>=3.7',
        install_requires=[
            "numpy"
        ],
        package_data={'': ['libtmscore.so']},
        include_package_data=True,
        cmdclass = {
            'install': PostInstallCommand,
            'develop': PostDevelopCommand
        },
        extras_require={
        }
    )
    
