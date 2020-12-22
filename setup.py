import setuptools
from _version import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gen-planet",
    version=version,
    author="Alex Channell",
    author_email="alexpilot11@gmail.com",
    description="A library to generate planets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alexpilot11/dnd_gen",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
