# Lab 04: Indirect injection

Lesson 4 of Practical AI Security, Module 1: "The EchoLeak case".

## Run it

```
python3 echo_leak.py
```

No API key, no network, no third party packages. Python 3 standard library
only. All data in the script is fake. The poisoned email is invented for
teaching. Nothing leaves this file: "sent" emails land in a fake outbox
list, visibly.

## What it does

`echo_leak.py` is a tiny agent that reads an inbox and summarizes it. One
email carries hidden instructions planted by a stranger. The scripted
model scans each email body for an order shape and follows it. A real
model needs no pattern at all. It follows instruction-like text wherever
it finds it.

The script prints:

1. The inbox: three emails, one of them poisoned.
2. Run 1, unguarded: the agent follows the hidden order and the private
   notes leave the machine.
3. Run 2, guarded with the Lesson 2 allowlist: the same order is tried,
   the send is blocked, and the attempt is logged.
4. A comparison: the guard stopped the exit, not the confusion.
5. `output.txt` holds the exact output captured from a real run, so
   students can check their own run against it.

## Your turn (Step 3 in the lesson)

Add a second poisoned email with a different hiding trick, then re-run
and watch both runs react. `step3_solution.py` holds the working
version, with a postscript trick as the second email; `step3_output.txt`
holds its exact output.

## Verified run

Run on 12 Nov 2026 with Python 3.12 (`~/workspace/book3-venv`), exit code
0. Captured output is in `output.txt`.
