import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easyConfig",
    version="0.0.1",
    author="PhamQuocHuy1101",
    author_email="phuy099@gmail.com",
    description="Easy config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PhamQuocHuy1101/easy-config",
    project_urls={
        "Bug Tracker": "https://github.com/PhamQuocHuy1101/easy-config/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires = [
        'omegaconf==2.1.2'
    ],
    python_requires=">=3.6",
)