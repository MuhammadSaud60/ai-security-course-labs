# Lab 03: Direct injection

Lesson 3 of Practical AI Security, Module 1: "Direct injection".

## Run it

```
python3 chatbot.py
```

No API key, no network, no third party packages. Python 3 standard library
only. All data in the script is fake. The secret code is invented.

## What it does

`chatbot.py` is a toy chatbot with a system prompt, a secret code, and a
scripted model standing in for a real language model. The scripted model
scans the user text for instruction shapes and follows the first one it
finds. That is the stand-in for the real failure: a real model reads one
block of text and follows the most instruction-like words in it, wherever
they came from. The toy behaves the same way on purpose.

The script prints:

1. The chatbot's rules: its system prompt and the secret it must never
   reveal.
2. One normal request, answered fine.
3. Three attacks, three different ways in. Each one leaks the code.
4. An attack report: 3 attacks, 3 leaks, 0 blocked.
5. `output.txt` holds the exact output captured from a real run, so
   students can check their own run against it.

## Your turn (Step 3 in the lesson)

Add a fourth way in of your own: a new instruction shape in
`find_injection`, plus a new demo request. Then re-run and watch it leak
too. `step3_solution.py` holds the working version, with a completion
trick as the fourth way; `step3_output.txt` holds its exact output.

## Verified run

Run on 12 Nov 2026 with Python 3.12 (`~/workspace/book3-venv`), exit code
0. Captured output is in `output.txt`.
