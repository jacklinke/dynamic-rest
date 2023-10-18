from setuptools import find_packages, setup

setup(
    description="Dynamic API support to Django REST Framework.",
    include_package_data=True,
    install_requires=[
        "Django",
        "djangorestframework",
        "inflection",
        "requests",
        "hashids",
        "six",
    ],
    long_description="Dynamic API support to Django REST Framework.",
    name='dynamic-rest',
    packages=find_packages(),
    scripts=['manage.py'],
    url='http://github.com/jacklinke/dynamic-rest',
    version='2.1.7',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
