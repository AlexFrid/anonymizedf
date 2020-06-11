# Let users know if they're missing any of our hard dependencies
# code adapted from pandas package
hard_dependencies = ("pandas", "faker")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
