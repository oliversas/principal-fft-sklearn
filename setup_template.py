from distutils.core import setup

setup(
  name = 'principal-fft',
  packages = ['principalfft'],
  version = 'VERSION',
  license='MIT',
  description = 'Extract principal FFT components for features generation',
  author = 'Simone Salerno',
  author_email = 'eloquentarduino@gmail.com',
  url='https://github.com/oliversas/principal-fft-sklearn',
  keywords = [
    'ML',
    'scikit-learn',
    'machine learning'
  ],
  install_requires=[
    'numpy',
    'scikit-learn'
  ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)