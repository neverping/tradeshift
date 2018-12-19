from setuptools import setup

setup(
    name='tradeshift',
    packages=['triangle'],
    version='0.0.1',
    author='Willian Braga da Silva',
    author_email='neverping@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Triangle',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: FPL 1.0.0',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description='Tradeshift Triangle Code Challenge',
    extras_require={
        'dev': [
            'pytest>=3',
        ]
    },
    license='Free Public License 1.0.0 ',
    long_description=open('README.rst').read(),
    platforms='any',
    python_requires='>=2.7',
    tests_require=['pytest', 'pytest-runner'],
    url='https://github.com/neverping',
    zip_safe=True,
)