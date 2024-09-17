===============================
lcls_naming_tool
===============================

.. image:: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml/badge.svg
        :target: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml

.. image:: https://img.shields.io/pypi/v/lcls_naming_tool.svg
        :target: https://pypi.python.org/pypi/lcls_naming_tool


`Documentation <https://pcdshub.github.io/lcls_naming_tool/>`_

A tool that checks the form and content of PV and device names with respect to the LCLS naming convention.

Instructions
------------

To run the Python script:

1. To check if a PV or device name is valid pipe in the name like so ``$ echo "MR2K4:KBO:PIP:01:PUMPSIZE" | ./lcls_naming_tool.py``

2. To check if a list of names is valid pipe in the file name like so ``$ cat pvlist.txt | ./lcls_naming_tool.py`` (names should be separated by newline characters.)

3. To view the current version add ``-v`` or ``--version`` like so ``$ echo "MR2K4:KBO:PIP:01:PUMPSIZE" | ./lcls_naming_tool.py -v``

To run Flask and Gunicorn web server:

1. Copy all contents of /lcls_naming_tool/web/ folder to host directory. Several files are symlinks and may need to be manually copied into the web folder for the web app to work.

2. To start the web app navigate to the /web folder and type:

``export FLASK_APP=app``

``flask --app app run``

``gunicorn --config gunicorn_config.py app:app``

If hosting locally the website will be at http://127.0.0.1:8080/


Requirements
------------

* Python 3.9+
* Flask 2.2.5
* Gunicorn 23.0.0


Installation
------------

Navigate to the top level folder and type:

``pip3 install --upgrade pip``

``pip3 install -r requirements.txt``


Running the Tests
-----------------
::
