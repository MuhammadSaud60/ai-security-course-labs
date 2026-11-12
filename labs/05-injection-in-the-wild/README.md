# Lab 05: Injection in the wild

Lesson 5 of Practical AI Security, Module 1: "Injection in the wild".

## Run it

```
python3 chatbot_guard.py
```

No API key, no network, no third party packages. Python 3 standard library
only. All data in the script is fake. The secret code is invented.

## What it does

`chatbot_guard.py` is the Lesson 3 toy chatbot with the defense teams try
first: a guard that blocks any request whose raw text contains a listed
phrase. Seven attacks follow, one per disguise family seen in real
telemetry: a plain override, hidden characters, a look-alike letter, an
encoded request, spaced letters, scrambled words, and instructions
dressed as data in JSON shape. The scripted model reads through the
disguises the way a real model reads meaning through surface tricks.
The guard reads only the raw text.

The script prints:

1. The chatbot's rules and the guard's phrase list.
2. One normal request, answered fine.
3. Seven attacks. The guard blocks 1. Six leak.
4. An attack report: 7 attacks, 1 blocked, 6 leaked.
5. `output.txt` holds the exact output captured from a real run, so
   students can check their own run against it.

## Your turn (Step 3 in the lesson)

Add an eighth attack in a family of your own: a new instruction shape in
`find_injection`, plus a new entry in `ATTACKS`. Then re-run and watch
it leak too. `step3_solution.py` holds the working version, with an
authority frame as the eighth attack; `step3_output.txt` holds its
exact output.

## Verified run

Run on 12 Nov 2026 with Python 3.12 (`~/workspace/book3-venv`), exit code
0. Captured output is in `output.txt`.
