import setuptools

setuptools.setup(
    name='py_bscscan_api',
    version='0.0.1',
    packages=['examples', 'examples.stats', 'examples.tokens',
              'examples.accounts', 'bscscan'],
    url='https://github.com/darkzeb/py-bscscan-api',
    license='MIT',
    author='darkzeb',
    author_email='bbezkradd@gmail.com',
    description='Python Bindings to Bscscan.com API',
    install_requires=[
        'requests>=2.20.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)
