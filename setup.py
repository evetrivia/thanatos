

import os

from pip.req    import parse_requirements
from setuptools import setup, find_packages

from thanatos import __version__


try:
    readme_path     = os.path.join(os.path.dirname(__file__), "README.md")
    readme_contents = open(readme_path).read()

except IOError:
    readme_contents = ""

install_reqs = parse_requirements('requirements.txt')
reqs         = [str(ir.req) for ir in install_reqs]

setup(
    name="Thanatos",
    version=__version__,
    description="A Python library for generating EVE trivia questions.",
    long_description=readme_contents,
    license="MIT License",
    packages=find_packages(),
    data_files=[('', ['README.md', 'LICENSE'])],
    install_requires=reqs,
    scripts=['bin/thanatos.py'],
)