from setuptools import find_packages, setup


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="FlaskMotors",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    author="Diego Schmitz",
    author_email="diego@dschmitz.dev",
    install_requires=read("requirements.txt"),
    description="Uma API para treinar habilidades com Python e Flask",
    long_description=read("README.md"),
    extras_require={"dev": read("requirements-dev.txt")},
    python_requires=">=3.10",
    classifiers=[
        "Framework :: Flask",
        "Natural Language :: Portuguese",
        "Programming Language :: Python :: 3.10",
    ]
)
