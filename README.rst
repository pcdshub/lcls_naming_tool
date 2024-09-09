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

1. Set $ chmod 775 lcls_naming_tool.py to make the file executable.

2. To check if a PV name is valid pipe in the PV name like so 
        ```$ echo "XCS:DG3:GCC:02:PCTRLSPRBCK" | ./lcls_naming_tool.py````

3. To check if a list of PV names is valid pipe in the file name like so 
        ```$ cat pvlist.txt | ./lcls_naming_tool.py````


Requirements
------------

* Python 3.9+

Installation
------------

::

Running the Tests
-----------------
::
