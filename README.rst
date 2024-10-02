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

1. In your current working directory type ``source /cds/group/pcds/pyps/conda/venvs/lcls_naming_tool/bin/activate``

2. To check if a PV or device name is valid pipe in the name to the tool. For example, ``$ echo "MR2K4:KBO:PIP:01:PUMPSIZE" | ./lcls_naming_tool.py``

3. To check if a list of names is valid pipe in the file name to the tool. For example, ``$ cat pvlist.txt | ./lcls_naming_tool.py`` (names should be separated by newline characters.)

4. To view the current version add ``-v`` or ``--version``. For example, ``$ echo "MR2K4:KBO:PIP:01:PUMPSIZE" | ./lcls_naming_tool.py --version``


Use in a Python script:

1. In your current working directory set up the environment: 

``source /cds/group/pcds/pyps/conda/venvs/lcls_naming_tool/bin/activate``

``git clone git@github.com:pcdshub/lcls_naming_tool.git``

``export PYTHONPATH=$PWD/lcls_naming_tool/lcls_naming_tool``

2. To call the LCLS Naming Tool module ``from lcls_naming_tool import load_taxons, validate``

5. In your ``main`` function ``load_taxons()`` should be called first. It takes no parameters and loads all the approved taxons in JSON format. The function ``validate()`` takes a PV or device name in string format as a parameter and returns ``True`` for a valid name or ``False`` for an invalid name.


To run the web server:

``ssh psca@psctlws01``

``cd /u1/psca/prod/apps/lcls_naming_tool``

``git pull``

``supervisorctl``

``supervisor> stop lcls_naming_tool``

``supervisor> start lcls_naming_tool``

Website is hosted at https://pswww.slac.stanford.edu/lcls_naming_tool/


Requirements
------------

* Python 3.9+
* Flask 2.2.5 (web only)
* Gunicorn 23.0.0 (web only)


Installation
------------


Running the Tests
-----------------

