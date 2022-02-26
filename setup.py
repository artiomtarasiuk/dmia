from setuptools import setup

setup(
    name="dmia",
    version="0.1.0",
    author="me",
    url="https://github.com/artiomtarasiuk/dmia",
    description="log reg",
    python_requires=">=3.8,<3.11",
    install_requires=[
        "numpy~=1.22.2",
        "matplotlib~=3.5.1",
        "scipy~=1.8.0",
        "pandas~=1.4.1",
        "seaborn~=0.11.2",
        "tqdm~=4.62.3",
        "scikit-learn~=1.0.2",
    ],
    extras_require={
        "format": ["black~=21.12b0", "isort~=5.10.1", "safety~=1.10.3"],
    },
)
