

import os
import pip

from pip.req import parse_requirements
from setuptools import setup, find_packages

from thanatos import __version__


try:
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    readme_contents = open(readme_path).read()

except IOError:
    readme_contents = ""

install_reqs = parse_requirements('requirements.txt', session=pip.download.PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="Thanatos",
    version=__version__,
    description="A Python library for generating EVE Online trivia questions.",
    long_description=readme_contents,
    license="MIT License",
    packages=find_packages(),
    author="Regner Blok-Andersen",
    author_email="regnerba@gmail.com",
    url="https://github.com/Regner/thanatos",
    data_files=[('', ['README.md', 'LICENSE'])],
    install_requires=reqs,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Games/Entertainment",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
