from setuptools import setup
import os, shutil

version = '0.1'

setup(version=version,
      name='kestrel',
      description = "kestrel",
      scripts = [
            "bin/kestrel_crontab.sh",
            "bin/kestrel_newconf.py",
            "bin/kestrel_sieve.py",
      ],
      long_description="""kestrel""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      include_package_data = True,
      keywords='',
      author='Ian Dennis Miller',
      author_email='ian@iandennismiller.com',
      url='http://www.iandennismiller.com',
      install_requires = [
            "sievelib==0.8",
            "Jinja2==2.7.1",
      ],
      license='MIT',
      zip_safe=False,
)