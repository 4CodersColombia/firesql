from distutils.core import setup
import setuptools


setup(
    name='firesql',
    version='0.1.1',
    include_package_data=True,
    description='Library to use databases sql or not-sql',
    author='Andres Gonzalez',
    author_email='andres@4coders.co',
    license="GPLv3",
    # use the URL to the github repo
    url='https://github.com/4CodersColombia/firesql',
    download_url='https://github.com/4CodersColombia/firesql/tarball/0.1',
    keywords=['sql', 'no-sql'],
    classifiers=['Programming Language :: Python :: 3.9',],
    packages = setuptools.find_packages(),
    install_requires=[
          'pymysql',
      ],
)

