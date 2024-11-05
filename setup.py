# setup.py

from setuptools import setup, find_packages

setup(
    name='wikiracer',
    version='0.1',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "click",
    ],
    entry_points={
        'console_scripts': [
            'wikiracer=wikiracer.cli:main',
        ],
    },
    description='CLI tool to extract and display links from a Wikipedia page.',
    author='akablockchain2',
    url='https://github.com/akablockchain2/wikiracer',
)
