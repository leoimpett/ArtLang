from setuptools import setup

setup(name='artlang',
      version='0.1',
      description='A user-friendly image processing librairy for art historians.',
      url='https://github.com/leoimpett/ArtLang',
      author='Robin Leurent',
      author_email='unknown',
      license='Cette œuvre est mise à disposition sous licence Attribution 3.0 Suisse. Pour voir une copie de cette licence, visitez http://creativecommons.org/licenses/by/3.0/ch/ ou écrivez à Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.',
      packages = ['to be determined'],
      install_requires=[
          'numpy',
          'bokeh',
          'matplotlib',
          'scikit-image',
          'scikit-learn',
          'tqdm',
          'scipy',
          'pandas',
          'easygui',
          'requests',
          'wget'
      ]
)
          