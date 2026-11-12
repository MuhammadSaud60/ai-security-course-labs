# Lab 01: Trust boundary map

Lesson 1 of Practical AI Security, Module 0: "Why agents fail differently".

## Run it

```
python3 demo_agent.py
```

No API key, no network, no third party packages. Python 3 standard library
only. All data in the script is fake.

## What it does

`demo_agent.py` is a tiny agent with a keyword router standing in for a
model. It has five tools: `read_inbox`, `read_private_notes`,
`read_team_docs`, `post_to_board`, and `send_email`. Each tool is tagged
with the legs of the lethal trifecta it touches: PRIVATE (reads private
data), UNTRUSTED (reads content strangers could have written), EXFIL (sends
data somewhere others can see it).

The script prints:

1. The trust boundary map: every tool, what it reads, what it writes, tags.
2. Two demo runs with a danger check after each one. The inbox plus
   public board run is flagged as a dangerous combination. The team docs
   run is fine.
3. `output.txt` holds the exact output captured from a real run, so
   students can check their own run against it.

## Your turn (Step 3 in the lesson)

Add a `search_web` tool of your own: a function, an entry in the `TOOLS`
dict with honest tags (UNTRUSTED + EXFIL), and one line in the router.
Then run "Search the web for our salary notes." and read the verdict.
`step3_solution.py` holds the working version; `step3_output.txt` holds
its exact output.

## Verified run

Run on 12 Nov 2026 with Python 3.12 (`~/workspace/book3-venv`), exit code
0. Captured output is in `output.txt`.
