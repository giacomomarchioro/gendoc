import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gendoc",
    version="0.0.1",
    author="Giacomo Marchioro",
    author_email="giacomomarchioro@outlook.com",
    description="A wizard for writing docstrings.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/giacomomarchioro/gendoc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
