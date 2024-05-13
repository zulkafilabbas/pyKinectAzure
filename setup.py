from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='pykinect_azure',
    version='0.0.5',
    license='MIT',
    description='Python library to run Kinect Azure DK SDK functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Zulkafil Abbas (Fork) <- Ibai Gorordo (Original)',
    url='https://github.com/zulkafilabbas/pyKinectAzure',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
    ],
)