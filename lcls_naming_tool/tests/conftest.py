import os

parent = os.path.join(os.path.dirname(__file__), "..")

os.environ["LCLS_NAMING_TOOL_TAXONS_DIR"] = parent + "/taxons"
