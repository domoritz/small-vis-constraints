#!/usr/bin/env python

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, setup

from draco import __version__

this_dir = abspath(dirname(__file__))
with open(join(this_dir, "README.md"), encoding="utf-8") as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = "run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(["pytest", "--cov=draco", "--cov-report=term-missing"])
        raise SystemExit(errno)


setup(name="Draco",
      version=__version__,
      description="Visualization recommendation using constraints",
      author="Dominik Moritz, Chenglong Wang",
      author_email="domoritz@cs.washington.edu, clwang@cs.washington.edu",
      license="BSD-3",
      url="https://github.com/domoritz/draco",
      packages = ["draco"],
      entry_points = {
        "console_scripts": [
            "draco=draco.cli:main",
        ],
      },
      extras_require = {
        "test": ["coverage", "pytest", "pytest-cov"],
      },
      cmdclass = {"test": RunTests},
     )
