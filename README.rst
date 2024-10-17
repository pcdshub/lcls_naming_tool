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

Upgrade Python to 3.9+ if needed.

Install the LCLS Naming Tool module with ``pip install lcls_naming_tool``


Installation for Web
------------

After following the installation instructions above, install Flask and gunicorn:

``pip install Flask``

``pip install gunicorn``

In the top-level folder of your git cloned repo create a start.sh bash file with the following lines:

``export HOME_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )"``

``export PYTHONPATH="${HOME_DIR}/lcls_naming_tool"``

``cd "${HOME_DIR}/lcls_naming_tool/web"``

``exec gunicorn app:app -b 0.0.0.0:8080 \``


Instructions for the CLI Tool
------------

From the top-level folder navigate to the folder ``lcls_naming_tool``.

There are two ways to check if a PV or device name is valid. It can be piped in or use the argparse command line syntax.

``echo 'MR2K4:KBO:PIP:01:PUMPSIZE' | ./lcls_naming_tool.py``

``python lcls_naming_tool.py 'MR2K4:KBO:PIP:01:PUMPSIZE'``


Similarly, there are two ways to check names in a file. It can be piped in or use the argparse command line syntax. All names in a text file should be separated by newline characters.

``cat pvlist.txt | ./lcls_naming_tool.py``

``python lcls_naming_tool.py -f pvlist.txt`` (add a flag ``-f`` to indicate this is a file)


Instructions for Use in a File
------------

To use in your Python file:

1. At the top of your Python file add ``from lcls_naming_tool.lcls_naming_tool import load_taxons, validate``.

2. In your file call ``load_taxons()`` first. ``load_taxons`` will load all the approved taxons in JSON format and make it available to the ``validate`` function.

3. To check a PV or device name call the ``validate()`` function. ``validate`` accepts one parameter--a PV or device name in string format--and returns ``True`` if the name is valid or ``False`` if it's invalid.


Instructions for Web
------------

To run the web server on your local machine:

From the top-level folder type ``./start.sh``

View the web app on your local computer at http://localhost:8080


To run the web server (ECS only):

``ssh psca@psctlws01``

``cd /u1/psca/prod/apps/lcls_naming_tool``

``git pull``

``supervisorctl``

``supervisor> stop lcls_naming_tool``

``supervisor> start lcls_naming_tool``

Website is hosted at https://pswww.slac.stanford.edu/lcls_naming_tool/
