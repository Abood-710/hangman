try:
    from setuptools import setup
except ImportError as error:
    from distutils.core import setup

name = "hangman"
version = "1.0"

setup(
    name=name,
    version=version,
    description="control the Hangman game",
    author="Abdullah Al-Rumaithah",
    author_email="aboodagl710@gmail.com",
    maintainer=" You! ",
    url="https://git.yseq.net:3333/abdullah/Hangman",
    py_modules=['hangman'],
    zip_safe=False,
    install_requires=[],
    provides=[
        "{} ({})".format(name, version),
    ],
) 