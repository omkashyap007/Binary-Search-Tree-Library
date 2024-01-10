from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='bstq',
  version='1.0.0',
  description='Comphrensive Library for Binary Search Trees.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Om Kashyap',
  author_email='omkashyapcric@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='bst,binary search tree,binarytree,binary tree', 
  packages=find_packages(),
  install_requires=[''] 
)