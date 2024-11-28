# setup.py

from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# Read the README file
README = (HERE / "README.md").read_text(encoding="utf-8")

# Read the LICENSE file
LICENSE = (HERE / "LICENSE").read_text(encoding="utf-8")

setup(
    name="logstyles",  # Required
    version="0.1.2",  # Required
    description="A logging styling library for Loguru with customizable themes and formats.",  # Required
    long_description=README,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/jaylann/logstyles",  # Optional
    author="Justin Lanfermann",  # Optional
    author_email="Justin@Lanfermann.dev",  # Optional
    license="MIT",  # Optional
    classifiers=[
        "Development Status :: 4 - Beta",  # "3 - Alpha", "4 - Beta", "5 - Production/Stable"
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    keywords="logging loguru log styles themes formats",  # Optional
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),  # Required
    python_requires=">=3.7, <4",
    install_requires=[
        "loguru>=0.5.3",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "flake8>=3.8",
            "black>=21.0",
        ],
        "test": [
            "pytest>=6.0",
            "flake8>=3.8",
        ],
    },
    package_data={
        "logstyles": ["*.py"],
    },
    include_package_data=True,
    project_urls={
        "Bug Reports": "https://github.com/jaylann/logstyles/issues",
        "Source": "https://github.com/jaylann/logstyles/",
    },
    entry_points={
        "console_scripts": [
            # If you have any command-line scripts, list them here
            # "logstyles=logstyles.cli:main",
        ],
    },
    test_suite="tests",
    # zip_safe=False,  # Optional, uncomment if your package needs to be unpacked to run
)
