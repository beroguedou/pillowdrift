from setuptools import setup

tests_requirements = ['pytest==7.1.2']
extras_requirements = ['jupyter']
all_requirements = [
    'flask==2.2.2',
    'scikit-learn==1.1.2',
    'tqdm==4.64.0',
    'numpy==1.23.2',
    'pandas==1.4.3',
    'xgboost==1.6.1'
]

setup(
    name='mool',
    version='0.1.0',
    author="Béranger GUEDOU",
    author_email="beranger@pillowanalytica.com",
    packages=[
        "mool",
        "mool.utils"
        ],
    licence='LICENCE',
    description="Application that allows machine learning and drift monitoring.",
    long_description=open("README.md", "r").read(),
    install_requires=all_requirements,
    extras_requires=extras_requirements,
    setup_requires=['pytest-runner', 'flake8'],
    test_require=['pytest'],
    test_suite='tests',
    classifiers=[
        "Development Status :: Beta",
        "Intended Audience :: Data scientists",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8"
    ]
)