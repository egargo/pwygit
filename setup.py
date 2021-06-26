import pathlib
from setuptools import setup


__version__ = '1.4.0'
__author__ = 'Clint'


HERE = pathlib.Path(__file__).parent
README = (HERE / 'README.md').read_text()


setup(
    name = 'pwy',
    version = __version__,
    description = 'A simple weather tool.',
    long_description = README,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/clieg/pwy',
    author = __author__,
    license = 'GPLv3',
    classifiers = [
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    packages = ['pwy'],
    include_package_data = True,
    install_requires = ['requests'],
    entry_points = {'console_scripts': ['pwy=pwy.__main__:main']},
)