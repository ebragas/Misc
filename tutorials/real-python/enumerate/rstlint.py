# !/bin/python
"""Sample from Real Python"""

def check_whitespace(lines):
    """Check for whitespace and line length issues."""
    for lno, line in enumerate(lines):
        if "\r" in line:
            yield lno + 1, "\\r in line"
        if "\t" in line:
            yield lno + 1, "OMG TABS!!!1"
        if line[:-1].rstrip(" \t") != line[:-1]:
            yield lno + 1, "trailing whitespace"

