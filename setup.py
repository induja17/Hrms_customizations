from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hrms_customizations/__init__.py
from hrms_customizations import __version__ as version

setup(
	name="hrms_customizations",
	version=version,
	description="customizations",
	author="admin",
	author_email="induja.ag@10decoders.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
