from setuptools import setup, find_packages
import re

setup(
    name="ppnet",
    install_requires=[
    ],
    packages=find_packages(),
    scripts=[
        "bin/ppnet-augment",
        "bin/ppnet-test",
        "bin/ppnet-train",
    ],
    version=re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        open(
            "ppnet/__init__.py",
            "r").read(),
        re.M).group(1),
)
