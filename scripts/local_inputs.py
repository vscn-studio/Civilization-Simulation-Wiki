"""Machine-specific inputs are environment settings, never published paths."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def required_dir(variable):
    value = os.environ.get(variable)
    if not value:
        raise SystemExit('Set {} to the input directory before extraction.'.format(variable))
    directory = Path(value).resolve()
    if not directory.is_dir():
        raise SystemExit('{} must be an existing directory.'.format(variable))
    return directory


def source_dir(variable, sibling):
    return Path(os.environ.get(variable, str(ROOT.parent / sibling)))
