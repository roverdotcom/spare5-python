from setuptools import setup
from setuptools import find_packages


setup(
    name="spare5",
    version='0.1',
    description="Spare 5 Python API client",
    license="MIT",
    author="John Williams, Philip Kimmey",
    author_email="john@rover.com, philip@rover.com",
    packages=find_packages(),
    keywords=['spare5'],
    install_requires=[],
    classifiers=[
        'Environment :: Other Environment',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries'
    ],
)
