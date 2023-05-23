"""setup module."""

import re
from pathlib import Path

from setuptools import find_packages, setup

name = "mse_cli_core"

version = re.search(
    r"""(?x)
    __version__
    \s=\s
    \"
    (?P<number>.*)
    \"
    """,
    Path(f"src/{name}/__init__.py").read_text(),
)

setup(
    name=name,
    version=version["number"],
    url="https://cosmian.com",
    license="MIT",
    project_urls={
        "Documentation": "https://docs.cosmian.com",
        "Source": "https://github.com/Cosmian/mse-cli-core",
    },
    author="Cosmian Tech",
    author_email="tech@cosmian.com",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    python_requires=">=3.8.0",
    description="Utils for MicroService Encryption Python CLI ",
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=True,
    install_requires=[
        "cryptography>=39.0.0,<40.0.0",
        "docker>=6.0.1,<7.0.0",
        "intel-sgx-ra>=1.0,<1.1",
        "jinja2>=3.0,<3.1",
        "mse-lib-crypto>=1.1,<1.2",
        "pydantic>=1.10.2,<2.0.0",
        "pyjwt>=2.6.0,<2.7.0",
        "requests>=2.28.1,<3.0.0",
        "toml>=0.10.2,<0.11.0",
        "urllib3>=1.26.13,<1.27.0",
    ],
    setup_requires=["wheel"],
    tests_require=["pytest>=7.2.0,<7.3.0"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
