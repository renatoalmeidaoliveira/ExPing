from setuptools import setup, find_packages

setup(
    name='exping',
    version='1.0.0',
    description='A simple exfiltration ping tool',
    author='Renato Almeida de Oliveira',
    author_email="renato.almeida.oliveira@gmail.com",
    url='https://github.com/renatoalmeidaoliveira/Pinger',
    packages=find_packages(),
    install_requires=[
        'cryptography',
        'scapy',
    ],
    entry_points={
        'console_scripts': [
            'exping = exping.entry:main',
        ]
    },
)