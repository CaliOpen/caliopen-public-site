import os

from setuptools import setup, find_packages

name = 'caliopen_website'
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_jinja2',
    'babel',
    'gunicorn',
    'waitress'
    ]

setup(name=name.replace('_', '-'),
      version='0.0',
      description='caliopen project presentation',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        ],
      author='Caliopen Contributors',
      author_email='laurent@caliopen.org',
      url='https://www.caliopen.org',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      entry_points="""\
      [paste.app_factory]
      main = %s:main
      """ % name,
      )
