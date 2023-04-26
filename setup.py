from setuptools import setup, find_packages

setup(
    name="network-analysis",
    version="0.1.0",
    description="Tool for network and security analysis",
    author="Craxti",
    author_email="fetis.dev@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests==2.26.0",
        "beautifulsoup4==4.10.0",
        "scapy==2.4.5",
        "shodan==2.0.0",
        "virustotal-api==0.6.1",
        "pycensys==2.0.0",
        "securitytrails==0.3.3",
        "passive_dns==2.3.0",
        "dnspython==2.2.0",
        "pycryptodomex==3.11.0",
        "pyopenssl==21.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
