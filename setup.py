"""
setup.py
~~~~~~~~~~~~~


:copyright: (c) 2016 Sander Bollen
:copyright: (c) 2016 Leiden University Medical Center
:license: MIT
"""

from setuptools import setup

setup(
    name="gvcf2bed",
    version="0.1",
    description="Convert gVCF into BED",
    author="Sander Bollen",
    author_email="a.h.b.bollen@lumc.nl",
    license="MIT",
    packages=["gvcf2bed"],
    install_requires=["pyvcf==0.6.8"],
    test_requires=["pytest", "pytest-cov"],
    entry_points={
        "console_scripts": [
            "gvcf2bed = gvcf2bed.gvcf2bed:main"
        ]
    },
    classifiers=[
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ]

)
