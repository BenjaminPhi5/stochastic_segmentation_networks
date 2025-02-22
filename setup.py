
from setuptools import find_packages, setup

setup(
	name="ssn",
	version="1.0",
	packages=find_packages(exclude=["assets"]),

	install_requires = [
	  	"scipy>=1.2.0",
        "torchvision>=0.4.2",
        "pandas>=0.24.1",
        "tqdm>=4.43.0",
        "numpy>=1.16.1",
        "tabulate>=0.8.7",
        "torch>=1.3.1",
        "svgutils>=0.3.1"
        "SimpleITK>=1.2.4",
	]

)