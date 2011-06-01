""" Setup module
"""
from setuptools import setup, find_packages
import os
from os.path import join

name = 'eea.signals'
path = name.split('.') + ['version.txt']
version = open(join(*path)).read().strip()

setup(name='eea.signals',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='signals publication environment',
      author='European Environment Agency',
      author_email='webadmin@eea.europa.eu',
      url='http://svn.eionet.europa.eu/projects/Zope',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'eea.jquery',
          'Products.LinguaPlone'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
