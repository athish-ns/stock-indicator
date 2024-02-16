import sys
import setuptools

PREFIX_VERSION = "semver:"
DEFAULT_VERSION = "0.0.0.dev0"

if sys.argv[-1].startswith(PREFIX_VERSION):
    version = sys.argv[-1].split(':')[1]
    sys.argv.pop()
else:
    version = DEFAULT_VERSION

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stock-indicators",
    version=version,
    author="Athish NS",
    maintainer="Athish",
    description="Stock Indicators for Python. Send in historical price quotes and get back desired technical indicators such as Stochastic RSI, Average True Range, Parabolic SAR, etc.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Athish-1/stock-indicators",
    project_urls={
        "Bug Tracker": "https://github.com/Athish-1/stock-indicators/issues",
        "Documentation": "https://your-documentation-url.com",  # Replace with the actual documentation URL
        "Source Code": "https://github.com/Athish-1/stock-indicators",
    },
    license="Apache 2.0",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(
        exclude=(
            'tests',
            'tests.*',
            'benchmarks',
            'benchmarks.*'
        )
    ),
    package_data={
        "stock_indicators._cslib": [
            "runtimeconfig.json",
            "lib/*.dll"
        ],
    },
    python_requires=">=3.7",
    install_requires=[
        'pythonnet==3.0.1',
        'typing_extensions>=4.0.0',
    ],
)
