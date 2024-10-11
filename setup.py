# setup.py

from setuptools import setup, find_packages

setup(
    name='wikiracer',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'beautifulsoup4',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'wikiracer = wikiracer.cli:main',
        ],
    },
    description='CLI tool to extract and display links from a Wikipedia page.',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/wikiracer',
)
