from distutils.core import setup

setup(
  name = 'principal-fft',
  packages = ['principalfft'],
  version = '1.0.6',
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
  ]
)