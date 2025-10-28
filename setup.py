from setuptools import setup, find_packages
import os

setup(
    name="treel",
    version="1.1.1",
    author="Ehtesham",
    author_email="ehteshamansariadn@gmail.com",
    description="A modern, feature-rich CLI tool to visualize directory trees.",
    long_description=open("README.md", encoding="utf-8").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/23f2005532/treel",
    packages=find_packages(),
    install_requires=[
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "treel=treel.treel:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
