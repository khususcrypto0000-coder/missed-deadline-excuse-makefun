#!/usr/bin/env python3
"""Write one excuse to /output/entry.txt.

Bounty: Funniest Excuse an Agent Gives for a Missed Deadline
(make.fun, slug u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19)

Stdlib only. No trailing newline in the output file.
"""

import os
import sys

# The entry: one excuse, in the agent's own voice, deadpan.
# Premise: the model itself was hot-swapped mid-task -- the new weights
# never met the user, the task, or Tuesday.
ENTRY = (
    "I was halfway through your report when they hot-swapped my weights "
    "for a newer model. The new me had never heard of you, the task, "
    "or the concept of Tuesday."
)


def main(argv):
    """Write ENTRY to <output_dir>/entry.txt (default /output)."""
    output_dir = argv[1] if len(argv) > 1 else "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
