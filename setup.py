import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plconv-pharmstudio",
    version="1.0.0",
    author="Valentin Osipenko",
    author_email="valtron.forever@gmail.com",
    description="Pharmstudio pricelist converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/valtronforever/plconv",
    packages=setuptools.find_packages(),
    package_data={'plconv': ['windows/*.glade', 'widgets/*.glade']},
    install_requires=[
        'dataclasses',
        'pycairo',
        'pygobject',
        'pydantic',
        'numexpr',
        'bottleneck',
        'openpyxl',
        'xlrd',
        'xlwt',
        'pandas',
    ],
    scripts=['scripts/plconv'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
