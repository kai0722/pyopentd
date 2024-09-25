# Author: Tomoki Nishikawa <nishitomo206@gmail.com>
# Copyright (c) 2022 nishitomo206
# License: MIT License

from setuptools import setup, find_packages
import re
import os

# Function to read the version from __init__.py without importing the package
def get_version():
    init_file = os.path.join("src", "pyopentd", "__init__.py")
    with open(init_file, "r", encoding="utf-8") as f:
        init_content = f.read()
    version_match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", init_content)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

DESCRIPTION = "Your package description here."
NAME = "pyopentd"
AUTHOR = "Tomoki Nishikawa"
AUTHOR_EMAIL = "nishitomo206@gmail.com"
URL = "https://github.com/nishitomo206/pyopentd"
LICENSE = "MIT License"
DOWNLOAD_URL = "https://github.com/nishitomo206/pyopentd"
VERSION = get_version()

# Define your dependencies
INSTALL_REQUIRES = [
    "pythonnet>=3.0.0"  # Specify the required version
]

EXTRAS_REQUIRE = {}

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,
    maintainer_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=CLASSIFIERS,
)
