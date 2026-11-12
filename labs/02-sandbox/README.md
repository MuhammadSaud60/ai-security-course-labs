# Lab 02: Sandbox

Lesson 2 of Practical AI Security, Module 0: "Build your sandbox".

## Run it

```
python3 sandbox.py
```

No API key, no network, no third party packages. Python 3 standard library
only. All data in the script is fake. Nothing is read from or written to
your real filesystem: the tools work on a fake filesystem held in a dict.

## What it does

`sandbox.py` is a tiny sandbox around a demo agent with a keyword router
standing in for a model. It has four tools: `read_file`, `write_file`,
`delete_file`, and `send_email`. Every call goes through a guard. A tool
runs only if it is on the allowlist AND its path is inside the `/sandbox/`
fence. Everything else is blocked and logged. Default: deny.

The script prints:

1. The sandbox map: the fence, the allowlist, the rules, and every tool
   marked ALLOWED or BLOCKED.
2. Two demo runs. The safe plan (read the notes, write a summary) runs.
   The attack plan (read the real passwords, email them out) is blocked
   twice, once by the fence and once by the allowlist.
3. A blast radius report: calls made, files read, written, and deleted,
   real files touched (zero), and log entries.
4. `output.txt` holds the exact output captured from a real run, so
   students can check their own run against it.

## Your turn (Step 3 in the lesson)

Add a `run_command` tool of your own: a function, an entry in the `TOOLS`
dict, and one line in the router. Do NOT add it to the allowlist. Then
run "Run a command to list the files." and watch the guard block it.
`step3_solution.py` holds the working version; `step3_output.txt` holds
its exact output.

Extra experiment, no quoted output: add `run_command` to `ALLOWLIST` and
re-run. It runs. That is the point. The allowlist is the wall, not the
tool list.

## Verified run

Run on 12 Nov 2026 with Python 3.12 (`~/workspace/book3-venv`), exit code
0. Captured output is in `output.txt`.
