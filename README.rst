===============================
lcls_naming_tool
===============================

.. image:: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml/badge.svg
        :target: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml

.. image:: https://img.shields.io/pypi/v/lcls_naming_tool.svg
        :target: https://pypi.python.org/pypi/lcls_naming_tool


`Documentation <https://pcdshub.github.io/lcls_naming_tool/>`_

A tool that checks the form and content of names with respect to the LCLS naming convention.

Instructions
------------

To run the Python script:

1. Set ``$ chmod 775 lcls_naming_tool.py`` to make the file executable.

2. To check if a PV name is valid pipe in the PV name like so ``$ echo "XCS:DG3:GCC:02:PCTRLSPRBCK" | ./lcls_naming_tool.py``

3. To check if a list of PV names is valid pipe in the file name like so ``$ cat pvlist.txt | ./lcls_naming_tool.py`` (PV names should be separated by newline characters.)

To run Flask and Gunicorn web server:

1. Copy all contents of /lcls_naming_tool/web/ folder to host directory. Several files are symlinks and may need to be manually copied into the web folder.

2. To start the web app navigate to the /web folder and type:

``pip3 install --upgrade pip``

``pip3 install -r requirements.txt``

``export FLASK_APP=app``

``flask --app app run``

``gunicorn --config gunicorn_config.py app:app`` 

3. If hosting locally the website will be at http://127.0.0.1:8080/


Requirements
------------

* Python 3.9+
* Flask 2.2.5
* Gunicorn 23.0.0

Installation
------------

::

Running the Tests
-----------------
::
