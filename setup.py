# -*- coding: utf-8 -*-
"""
Scans the given paths for images and identify unique images.
"""
from setuptools import find_packages
from setuptools import setup

dependencies = ["click"]

setup(
    python_requires=">=3.6",
    name="unique_image_scan",
    version="0.1.0",
    url="https://github.com/danielhoherd/unique-image-scan",
    license="BSD",
    author="Daniel Hoherd",
    author_email="daniel.hoherd@gmail.com",
    description="Scans the given paths for images and identify unique images.",
    long_description=__doc__,
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    platforms="any",
    install_requires=dependencies,
    entry_points={"console_scripts": ["unique-image-scan = unique_image_scan.cli:main"]},
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 1 - Planning",
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
