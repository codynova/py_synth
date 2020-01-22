import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ask_siri",
    version="0.0.1",
    author="Intouch Group",
    author_email="codyrnova@gmail.com",
    description="Simple Python 3 synthesizer using numpy and scipy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codynova/py_synth",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pyaudio"
    ]
)