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

``ssh psca@psctlws01``

``cd /u1/psca/test/apps/nmsvc``

``git pull``

``./startup.sh``

Website is hosted at https://psdm.slac.stanford.edu/nmsvctest/


Requirements
------------

* PCDS conda
* Python 3.9+
* Flask 2.2.5 (web only)
* Gunicorn 23.0.0 (webs only)


Installation
------------


Running the Tests
-----------------
::
