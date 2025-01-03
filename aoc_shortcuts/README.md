Install with:

```
pip install --upgrade pip
pip install --editable /path/to/AdventOfCode/aoc_shortcuts
```

(The upgrade of the `pip` module should only really be needed for versions below `21.3`,
to support editable installs with `pyproject.toml` package format).

Alternatively, copy `aoc_shortcuts.py` file to the solution script’s directory, or add
`aoc_shortcuts` directory to `PYTHONPATH`.

To resolve any package dependencies that might have been recently added to
`pyproject.toml`, run:

```
pip install --upgrade --editable /path/to/AdventOfCode/aoc_shortcuts
```
