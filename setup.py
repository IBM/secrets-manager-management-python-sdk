from setuptools import setup, find_packages

setup(
    name='ibm-secrets-manager-instance-management',
    version='2.0.0',
    description='IBM Cloud Secrets Manager instance management Python SDK',
    author='IBM',
    packages=find_packages(exclude=['test', 'test.*']),
    install_requires=[
        'ibm-cloud-sdk-core>=3.16.0,<4.0.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-cov>=4.0.0',
            'python-dotenv>=0.19.0',
            'responses>=0.20.0',
        ]
    },
    python_requires='>=3.8',
)
