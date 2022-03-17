from setuptools import find_packages
from setuptools import setup
import os

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setup(
    name='Face Blur',
    version='1.0.0',
    description='Camera app for vluring face',
    author='Rostyslav Mosorov',
    author_email='rmosorov@icloud.com',
    license='MIT License',
    url='https://github.com/rostekus/face_blur_cv2',
    install_requires=install_requires,
    packages=find_packages(where='', exclude='tests*'),
    package_dir={'': ''}

)
