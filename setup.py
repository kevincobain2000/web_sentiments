import os
from setuptools import setup, find_packages

setup(
    name = 'web_sentiments', 
    version='0.1',
    author='KATHURIA Pulkit',
    author_email='pulkit@jaist.ac.jp',
    #packages= find_packages(''), 
    #scripts = ['scripts/senti_classifier'],
    package_dir = {'':'src'},
    #package_data = {'': ['data/*.txt','data/*.p'],
    #},
    #include_package_data = True,
    url= 'http://www.jaist.ac.jp/~s1010205/sentiment_twitter',
    license='LICENSE.txt',
    description='Sentiment Classification using Twitter tweets',
    long_description=open('README').read(),
    install_requires = ['sentiment_classifier >= 0.5','nltk','argparse','numpy','python_twitter','gdata'],
    classifiers=['Development Status :: 4 - Beta','Natural Language :: English',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence'],
    
)

