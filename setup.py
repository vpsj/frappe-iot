from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in link_bundling/__init__.py
from link_bundling import __version__ as version

setup(
	name="link_bundling",
	version=version,
	description="You can bundle all your links and URLs in one place!",
	author="Vedant",
	author_email="vpsjdon@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
