import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / 'README.md').read_text()

setup(
    name='wwy',
    version='0.1.2',
    description='A simple weather information tool',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/clieg/wwy',
    author='Clint E.',
    license='GPLv3',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages=['wwy'],
    include_package_data=True,
    install_requires=[],
    entry_points={'console_scripts': ['wwy=wwy.__main__:main']},
)