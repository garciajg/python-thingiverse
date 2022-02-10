import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


def load_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


requirements = [
    "certifi==2021.10.8", "charset-normalizer==2.0.11",
    "idna==3.3","requests==2.27.1","urllib3==1.26.8",
    "python-box==5.4.1", "nose==1.3.7", "coverage==6.3.1",
    "mypy==0.931", "mypy-extensions==0.4.3", "tomli==2.0.1",
    "types-requests==2.27.9", "types-urllib3==1.26.9"
]


setuptools.setup(
    name="python-thingiverse",
    version="0.0.1a3",
    author="Jose Garcia",
    author_email="jose.garcia@vokal.io",
    description="A Python Thingiverse REST API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/garciajg/python-thingiverser",
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
    install_reqires=[],
    python_requires=">=3.6",
)
