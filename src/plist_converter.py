import plistlib
from pathlib import Path
from src.config import PLIST_INPUT_FILE, PLIST_OUTPUT_FILE
from typing import Union


def plist_converter(
    input_file: Path = PLIST_INPUT_FILE, output_file: Path = PLIST_OUTPUT_FILE
) -> Union[None, str]:
    """Didn't work as intended but I'll keep anyway"""
    try:
        with open(input_file, "rb") as file:
            plist_data = plistlib.load(file)
        with open(output_file, "wb") as file:
            plistlib.dump(plist_data, file, fmt=plistlib.FMT_XML)
    except Exception as e:
        return f"Failed to convert due to {e}"


def main() -> None:
    plist_converter()


if __name__ == "__main__":
    main()
