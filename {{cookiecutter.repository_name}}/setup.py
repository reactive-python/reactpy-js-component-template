from __future__ import print_function

import os
import subprocess
import sys

from setuptools import setup, find_packages
from distutils.command.build import build  # type: ignore
from distutils.command.sdist import sdist  # type: ignore
from setuptools.command.develop import develop

# the name of the project
name = "{{ cookiecutter.python_package_name }}"

# basic paths used to gather files
here = os.path.abspath(os.path.dirname(__file__))
package_dir = os.path.join(here, name)


# -----------------------------------------------------------------------------
# General Package Info
# -----------------------------------------------------------------------------


package = {
    "name": name,
    "python_requires": ">=3.7",
    "packages": find_packages(exclude=["tests*"]),
    "description": "{{ cookiecutter.project_short_description }}",
    "author": "{{ cookiecutter.author_name }}",
    "author_email": "{{ cookiecutter.author_email }}",
    "url": "{{ cookiecutter.repository_url }}",
    "platforms": "Linux, Mac OS X, Windows",
    "keywords": ["idom", "components"],
    "include_package_data": True,
    "zip_safe": False,
    "classifiers": [
        "Framework :: IDOM",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Multimedia :: Graphics",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
}


# -----------------------------------------------------------------------------
# Library Version
# -----------------------------------------------------------------------------

with open(os.path.join(package_dir, "__init__.py")) as init_file:
    for line in init_file:
        if line.split("=", 1)[0].strip() == "__version__":
            package["version"] = eval(line.split("=", 1)[1])
            break
    else:
        print("No version found in %s/__init__.py" % package_dir)
        sys.exit(1)


# -----------------------------------------------------------------------------
# Requirements
# -----------------------------------------------------------------------------


package["install_requires"] = ["idom>=0.18.0"]


# -----------------------------------------------------------------------------
# Library Description
# -----------------------------------------------------------------------------


with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

package["long_description"] = long_description
package["long_description_content_type"] = "text/markdown"


# ----------------------------------------------------------------------------
# Build Javascript
# ----------------------------------------------------------------------------


def build_javascript_first(cls):
    class Command(cls):
        def run(self):
            for cmd_str in ["npm install", "npm run build"]:
                subprocess.check_call(
                    cmd_str.split(), cwd=os.path.join(here, "js")
                )
            super().run()

    return Command


package["cmdclass"] = {
    "sdist": build_javascript_first(sdist),
    "build": build_javascript_first(build),
    "develop": build_javascript_first(develop),
}


# -----------------------------------------------------------------------------
# Install It
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    setup(**package)
