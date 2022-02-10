import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


requirements = [
    "certifi==2021.10.8", "charset-normalizer==2.0.11",
    "coverage==6.3.1", "distlib==0.3.4", "filelock==3.4.2",
    "idna==3.3", "mypy==0.931", "mypy-extensions==0.4.3",
    "nose==1.3.7", "packaging==21.3", "platformdirs==2.5.0",
    "pluggy==1.0.0", "py==1.11.0", "pyparsing==3.0.7",
    "python-box==5.4.1", "requests==2.27.1", "six==1.16.0",
    "toml==0.10.2", "tomli==2.0.1", "tox==3.24.5",
    "types-requests==2.27.9", "types-urllib3==1.26.9",
    "typing-extensions==4.0.1", "urllib3==1.26.8", "virtualenv==20.13.1"
]


setuptools.setup(
    name="python-thingiverse",
    version="0.0.2",
    author="Jose Garcia",
    author_email="jose.garcia@vokal.io",
    description="A Python Thingiverse REST API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garciajg/python-thingiverse",
    project_urls={
        "Bug Tracker": "https://github.com/garciajg/python-thingiverser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    install_reqires=requirements,
    python_requires=">=3.6",
)
