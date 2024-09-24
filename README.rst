===============================
lcls_naming_tool
===============================

.. image:: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml/badge.svg
        :target: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml

.. image:: https://img.shields.io/pypi/v/lcls_naming_tool.svg
        :target: https://pypi.python.org/pypi/lcls_naming_tool


`Documentation <https://pcdshub.github.io/lcls_naming_tool/>`_

A tool that checks the form and content of PV and device names with respect to the LCLS naming convention.

Taxons used are sourced from:

https://github.com/pcdshub/lcls_naming_tool/blob/main/docs/LCLS_Photon_Source_and_Systems_Nomenclature.pdf

https://docs.google.com/spreadsheets/d/1u5EfR9FIvwyTieWiMkCRqpBfHj-_xm3AygjFlxxWgDc/edit?gid=0#gid=0

https://docs.google.com/spreadsheets/d/1SeQhfwZ6O-wg8tyr_MCQZY1boJC-6j3N6EzexfZB-AU/edit?gid=0#gid=0


Instructions
------------

Use at the command line:

1. Activate the custom virtual environment with ``source /cds/group/pcds/pyps/conda/venvs/lcls_naming_tool/bin/activate``

2. To check if a PV or device name is valid pipe in the name like so ``$ echo "MR2K4:KBO:PIP:01:PUMPSIZE" | ./lcls_naming_tool.py``

3. To check if a list of names is valid pipe in the file name like so ``$ cat pvlist.txt | ./lcls_naming_tool.py`` (names should be separated by newline characters.)

4. To view the current version add ``-v`` or ``--version`` like so ``$ echo "MR2K4:KBO:PIP:01:PUMPSIZE" | ./lcls_naming_tool.py -v``

To run Flask and Gunicorn web server:

``ssh psca@psctlws01``

``cd /u1/psca/test/apps/nmsvc``

``git pull``

``./startup.sh``

Website is hosted at https://psdm.slac.stanford.edu/lcls_naming_tool/


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
