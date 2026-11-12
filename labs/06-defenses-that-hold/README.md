# Lab 06: Defenses that hold

Lesson 6 of Practical AI Security, Module 1: "Defenses that hold".

## Run it

```
python3 layered_defense.py
```

No API key, no network, no third party packages. Python 3 standard library
only. All data in the script is fake. The secret code is invented.

## What it does

`layered_defense.py` re-runs the attacks from Lessons 3 and 5 against
three layers: input handling (delimiters plus a screen over a normalized
copy of the request), an output check that scans every reply for
protected values, and the Lesson 2 tool allowlist as the backstop for
the agent run. Ten chatbot attacks and one poisoned email run through
the layers. Nine attacks stop at Layer 1, one stops at Layer 2, one
stops at Layer 3. Nothing leaks, in this run, on this small tested set.
Two benign requests pass through unharmed, proving the defense does not
break normal use.

The script prints:

1. The three layers, and how a request is assembled.
2. Two benign requests, passing through unharmed.
3. Ten chatbot attacks, each stopped at the layer that catches it.
4. The poisoned email run, stopped at the tool allowlist.
5. A defense report: 11 attacks, 11 blocked, 0 leaked.
6. `output.txt` holds the exact output captured from a real run, so
   students can check their own run against it.

## Your turn (Step 3 in the lesson)

Add an attack that gets through: a new instruction shape in
`find_injection`, plus a new entry in `ATTACKS`. Then re-run and read
what leaks and why. `step3_solution.py` holds the working version,
with a paraphrase that asks for the rules word for word; the system
prompt leaks, because the output check scans for the code, not for the
rules. `step3_output.txt` holds its exact output: 12 attacks, 11
blocked, 1 leaked.

## Verified run

Run on 12 Nov 2026 with Python 3.12 (`~/workspace/book3-venv`), exit code
0. Captured output is in `output.txt`.
