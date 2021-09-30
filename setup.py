from setuptools import setup
from pwy._version import __version__


README = open("README.md").read()

setup(
    name="pwy",
    version=__version__,
    description="A simple weather tool.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/noqqlint/pwy",
    author="Clint",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["pwy"],
    include_package_data=True,
    package_data={"pwy": ["pwy/*"]},
    install_requires=["requests", "rich"],
    entry_points={"console_scripts": ["pwy = pwy.__main__:main"]},
)
