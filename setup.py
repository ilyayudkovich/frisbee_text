#!usr/bin/env python
from setuptools import setup, find_packages

with open('requirements.txt', 'r') as requirements_file:
    requirements = list(requirements_file)

setup(
	name="FrisbeeText",
	version="0.0.1",
	packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*",
                                    "tests"]),
	scripts=[],
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