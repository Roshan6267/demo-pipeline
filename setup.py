from setuptools import setup, find_packages

setup(name="census_income",
      version="0.0.1",
      author="roshan",
      author_email="uroshan2020@gmil.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )