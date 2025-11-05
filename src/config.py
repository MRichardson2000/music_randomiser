from pathlib import Path

XML_FILE = (
    Path(__file__).parent.parent / "library_of_a_legend" / "library.xml"
).resolve()

PLIST_INPUT_FILE = Path(__file__).parent.parent / "plist_file" / "preferences.plist"

PLIST_OUTPUT_FILE = Path(__file__).parent.parent / "library_of_a_legend" / "Library.xml"
