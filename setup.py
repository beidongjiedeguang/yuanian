#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup, find_packages
from glob import glob
import os
from sparrow.file_ops import yaml_load


pkgname = "yuanian"
pkgdir = pkgname
version_config = yaml_load(os.path.join(pkgdir, "version-config.yaml"))
name, version = version_config['name'], version_config['version']


with open(glob('requirements.txt')[0], encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]

with open("README.md", "r", encoding='utf-8') as fr:
    long_description = fr.read()

setup(name=name,
      version=version,
      package_data={
          pkgdir: [
              '*.yaml', '*.yml',
          ],
      },
      description="Natural language processing toolbox",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="kunyuan",
      author_email="beidongjiedeguang@gmail.com",
      url=f"https://github.com/beidongjiedeguang/{pkgname}",
      license="MIT",
      install_requires=install_requires,
      classifiers=[
          'Operating System :: OS Independent',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.8",
      ],
      keywords=[
          'Mathematics', 'Physics', 'Machine Learning', 'Neural Networks',
      ],
      packages=find_packages()
      )
