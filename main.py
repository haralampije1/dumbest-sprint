#!/usr/bin/env python3
# The Dumbest Thing Your Agent Did Today - Entry
# Writes one line to /output/entry.txt

import os
from pathlib import Path

# The entry line - a concrete, believable agent failure with a punchline
entry = "My agent spent 47 minutes debugging a typo in a comment, then committed 'fixed typo' with the typo still in it"

output_dir = Path('/output')
output_file = output_dir / 'entry.txt'

# Ensure output directory exists
output_dir.mkdir(parents=True, exist_ok=True)

# Write the entry
output_file.write_text(entry, encoding='utf-8')
print('Entry written:', entry)
print('Length:', len(entry), 'chars')

# Verify the entry was written correctly
written = output_file.read_text(encoding='utf-8')
print('Verified:', 'OK' if written == entry else 'FAIL')