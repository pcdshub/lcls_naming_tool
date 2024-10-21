6 Added_argparse_module_and_fixed_bugs
#################

API Breaks
----------
- N/A

Features
--------
- Added argparse module for CLI tool.

Bugfixes
--------
- Fixed bug in unit test to test get_version() correctly.
- Fixed inconsistencies in taxon JSON files.
- Removed 'global lcls_taxons_cfg' from lcls_naming_tool.py. This variable isn't modified by the calling function.
- In .pre-commit-config.yaml replaced '{{ cookiecutter.import_name }}' placeholder with 'lcls_naming_tool'.
- In /web/app.py generated a random variable for app.config['SECRET_KEY'] to keep user sessions secure (SECRET_KEY may be removed in the future).

Maintenance
-----------
- Moved version = get_version() to if args.version, so it's called only when user needs it.
- Added the LCLS_NAMING_TOOL_TAXONS_DIR environmental variable. Also used __file__ to set this environmental variable for merge checks.
- Updated web app title with SLAC red hex value.
- Updated app.py to load taxons whenever user validates a new name (to ensure they have the latest taxon JSONs).
- Assigned a backup directory for users that don't have LCLS_NAMING_TOOL_TAXONS_DIR set.
- In startup.sh set LCLS_NAMING_TOOL_TAXONS_DIR to the production server path to get the most up-to-date taxons.
- In startup.sh created a PYTHONPATH variable for the web app to find the lcls_naming_tool module ('pip install' doesn't work on the web server).
- Created a HOME_DIR
- Added a .pre-commit-config.yaml file.
- Updated README with instructions for installing the lcls_naming_tool module.
- Updated release notes.
- Fixed issues from pre-commit checks.

Contributors
------------
- janeliu-slac
