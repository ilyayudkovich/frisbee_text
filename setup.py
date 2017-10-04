#!usr/bin/env python
from setuptools import setup, find_packages
from setuptools.command.install import install
import setup_mod

with open('requirements.txt', 'r') as requirements_file:
    requirements = list(requirements_file)

class PostInstallCommand(install):
	def run(self):
		setup_mod.main()

setup(
	name="FrisbeeText",
	version="0.0.1",
	packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                    "tests"]),
	scripts=['setup_mod.py'],
	cmdclass={
		'install':PostInstallCommand
	},
	install_requires=requirements,
	entry_points={
		'console_scripts': [
			'FrisbeeText = main_mod:main',
		]
	},
	author="Ilya Yudkovich",
	author_email="yudkovich.i@husky.neu.edu",
	description="Texting for Ultimate",
	url='https://github.com/iyud/frisbee_text'
)