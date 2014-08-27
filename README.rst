caliopen-public-site
====================

This is the source code of the CaliOpen public website.


Installation
------------

- Make a virtualenv
- Activate venv
- ``python setup.py develop``
- ``pip install waitress``
- ``bower install``
- ``pserve development.ini``
- Open ``localhost:6543``

Update of translation
---------------------

If you want to update translation resources, make update
in .po file and then run a ``python setup.py compile_catalog``
to update the related .mo file