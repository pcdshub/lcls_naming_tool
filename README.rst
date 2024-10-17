===============================
lcls_naming_tool
===============================

.. image:: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml/badge.svg
        :target: https://github.com/pcdshub/lcls_naming_tool/actions/workflows/standard.yml

.. image:: https://img.shields.io/pypi/v/lcls_naming_tool.svg
        :target: https://pypi.python.org/pypi/lcls_naming_tool


A tool that checks the form and content of PV and device names with respect to the LCLS naming convention.

Taxons used are sourced from:

https://github.com/pcdshub/lcls_naming_tool/blob/main/docs/LCLS_Photon_Source_and_Systems_Nomenclature.pdf

https://docs.google.com/spreadsheets/d/1u5EfR9FIvwyTieWiMkCRqpBfHj-_xm3AygjFlxxWgDc/edit?gid=0#gid=0

https://docs.google.com/spreadsheets/d/1SeQhfwZ6O-wg8tyr_MCQZY1boJC-6j3N6EzexfZB-AU/edit?gid=0#gid=0


Requirements
------------

* Python 3.9+
* Flask 2.2.5 (web only)
* Gunicorn 23.0.0 (web only)


Installation
------------

In the top-level folder of your git cloned repository create a Python virtual environment and activate.

Upgrade Python to 3.9 or later if needed.

Install the LCLS Naming Tool module with ``pip install lcls_naming_tool``


Instructions
------------

To use the command line interface:

1. From the top-level folder navgiate to the folder ``lcls_naming_tool``.

2. To check if a PV or device name is valid pipe in the name to the tool. For example, ``echo 'MR2K4:KBO:PIP:01:PUMPSIZE' | ./lcls_naming_tool.py``

3. To check if a list of names is valid pipe in the file name to the tool. For example, ``cat pvlist.txt | ./lcls_naming_tool.py``. All names in a text file should be separated by newline characters.


To use in your Python file:

1. In your Python file add ``from lcls_naming_tool.lcls_naming_tool import load_taxons, validate`` to the top.

2. In your function call ``load_taxons()`` first. ``load_taxons`` takes no parameters and loads all the approved taxons in JSON format.

3. To check a PV or device name call the ``validate()`` function. ``validate`` accepts one parameter--a PV or device name in string format--and returns ``True`` if the name is valid or  ``False`` if it's invalid.


To run the web server:

``ssh psca@psctlws01``

``cd /u1/psca/prod/apps/lcls_naming_tool``

``git pull``

``supervisorctl``

``supervisor> stop lcls_naming_tool``

``supervisor> start lcls_naming_tool``

Website is hosted at https://pswww.slac.stanford.edu/lcls_naming_tool/


Running the Tests
-----------------
