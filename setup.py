import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dsf-cnn", # Replace with your own username
    version="0.0.1",
    author="Simon Graham",
    author_email="simon_graham@hotmail.co.uk",
    description="A densely connected rotation-equivariant CNN for histology image analysis.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/simongraham/dsf-cnn",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
