from setuptools import setup, find_packages
import ttt

setup(name="ttt",
      version=ttt.__version__,
      description="Tic Tac Toe for ZZ",
      packages=find_packages(),
      install_requires=open("requirements.txt").readlines(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Programming Language :: Python :: 3.6",
          "License :: MIT"])
