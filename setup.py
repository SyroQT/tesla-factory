import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SyroQT-tesla-factory",
    version="0.0.1",
    author="Titas Janusonis",
    description="OOP exercise",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SyroQT/tesla-factory",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
