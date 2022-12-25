from setuptools import setup
from pwy.__version__ import __version__


README = open("README.md").read()

setup(
    name="pwy",
    version=__version__,
    description="A simple weather information tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/cliegargo/pwy",
    author="Clint",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["pwy"],
    include_package_data=True,
    package_data={"pwy": ["pwy/*"]},
    install_requires=["requests", "rich"],
    entry_points={"console_scripts": ["pwy = pwy.__main__:main"]},
)
