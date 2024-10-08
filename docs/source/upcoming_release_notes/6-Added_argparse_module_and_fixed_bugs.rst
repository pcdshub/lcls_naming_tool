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
- Moved version = get_version() to if args.version, so it's called only when user needs it.
- Fixed bug in unit test to test get_version() correctly.
- Added the LCLS_NAMING_TOOL_TAXONS_DIR environmental variable. Also set this for entire test session.
- Fixed inconsistencies in taxon JSON files.
- Updated web app title with SLAC red hex value.
- Updated app.py to load taxons whenever user validates a new name (to ensure they have the latest taxon JSONs).
- Added .pre-commit-config.yaml file.
- Updated README with instructions for installing the lcls_naming_tool module.


Maintenance
-----------
- N/A

Contributors
------------
- janeliu-slac
