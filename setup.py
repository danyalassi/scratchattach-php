from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = 'An Scratch-php API Wrapper for scratch.synt2x.xyz'
LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
    name="scratchattachPHP",
    version=VERSION,
    author="TimMcCool",
    author_email="none@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=["websocket-client","numpy","requests","bs4"],
    keywords=['scratch-php api', 'scratchattach-php', 'scratch-php api python', 'scratch python', 'scratch for python', 'scratch-php', 'scratch-php cloud', 'scratch-php cloud variables', 'scratch-php bot'],
    url='https://github.com/TimMcCool/scratchattach',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
