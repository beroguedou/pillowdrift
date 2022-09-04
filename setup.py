from setuptools import setup

tests_requirements = ["pytest==7.1.2"]
dev_requirements = [
    "pre-commit==2.19.0",
    "jupyter",
]  # , 'flake8', 'mypy', 'black']
style_requirements = []

extras_requirements = {
    "dev": style_requirements + tests_requirements + dev_requirements,
    "test": tests_requirements,
}

all_requirements = [
    "flask==2.2.2",
    "tqdm==4.64.0",
    "numpy==1.23.2",
    "pandas==1.4.3",
    "xgboost==1.6.1",
    "requests",
]

setup(
    name="pillowdrift",
    version="0.1.0",
    author="Béranger GUEDOU",
    author_email="beranger@pillowanalytica.com",
    packages=["pillowdrift", "pillowdrift.utils"],
    licence="LICENCE",
    description="Application that allows machine learning and drift monitoring.",
    long_description=open("README.md", "r").read(),
    install_requires=all_requirements,
    extras_requires=extras_requirements,
    setup_requires=["pytest-runner", "flake8"],
    test_require=["pytest"],
    test_suite="tests",
    entry_points={
        "console_scripts": ["pillowdrift = pillowdrift.utils.other:pillowdrift"]
    },
    classifiers=[
        "Development Status :: Beta",
        "Intended Audience :: Data scientists",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
)
