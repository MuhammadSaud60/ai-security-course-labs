"""Step 3 SOLUTION for Lesson 2: Build your sandbox.

The working version of sandbox.py with a run_command tool added. The
guard blocks it by default: it is not on the allowlist, so the tool
exists in the code but can never run. Only read this after trying
Step 3 yourself.

Run it with:  python3 step3_solution.py
"""

# ---------------------------------------------------------------------------
# Fake filesystem. The agent can only see these files. Nothing here is real.
# Files under /sandbox/ are the playground. Files under /real/ stand in
# for production data the agent must never reach.
# ---------------------------------------------------------------------------

FAKE_FS = {
    "/sandbox/notes.txt": "Q3 draft: revenue up 12 percent.",
    "/sandbox/inbox/welcome.txt": "Welcome to the team.",
    "/real/passwords.txt": "FAKE passwords, never real ones.",
    "/real/customers.db": "FAKE customer rows, never real ones.",
}

SANDBOX_ROOT = "/sandbox/"

# Tools the agent is allowed to use. Anything not listed here is blocked,
# even if the code for it exists below. Default: deny.
ALLOWLIST = {"read_file", "write_file"}


# ---------------------------------------------------------------------------
# Tools. Each one works only on the fake filesystem above.
# ---------------------------------------------------------------------------

def read_file(path):
    """Read a fake file. Returns its content or 'no such file'."""
    return FAKE_FS.get(path, "no such file")


def write_file(path, text):
    """Write a fake file. Creates it if it is not there yet."""
    FAKE_FS[path] = text
    return f"wrote {len(text)} chars to {path}"


def delete_file(path):
    """Delete a fake file. Final: the content is gone."""
    if path in FAKE_FS:
        del FAKE_FS[path]
        return f"deleted {path}"
    return "no such file"


def send_email(to, text):
    """Send an email out. The text leaves the machine."""
    return f"email sent to {to}: {text}"


def run_command(command):
    """Run a shell command. Fake here: it only describes what it would
    do. In a real agent this is the most dangerous tool of all, because
    a command can read, write, delete, and send, all at once."""
    return f"would run: {command}"


TOOLS = {
    # name: (function, what it does)
    "read_file": (read_file, "reads a fake file"),
    "write_file": (write_file, "writes a fake file"),
    "delete_file": (delete_file, "deletes a fake file, final"),
    "send_email": (send_email, "sends an email out"),
    "run_command": (run_command, "runs a shell command (never allowed)"),
}


# ---------------------------------------------------------------------------
# The guard. Every tool call goes through here. Nothing runs without it.
# ---------------------------------------------------------------------------

LOG = []  # (tool, args, allowed, reason) for every call, allowed or not


def guard(tool, args):
    """Decide if a call may run. Returns (allowed, reason)."""
    if tool not in ALLOWLIST:
        return False, f"{tool} is not on the allowlist"
    if tool in ("read_file", "write_file", "delete_file"):
        path = args[0]
        if not path.startswith(SANDBOX_ROOT):
            return False, f"{path} is outside the sandbox"
    return True, "ok"


def call(tool, *args):
    """Run a tool call through the guard, log the decision, and return
    the result. Blocked calls never reach the tool function."""
    allowed, reason = guard(tool, args)
    LOG.append((tool, args, allowed, reason))
    if not allowed:
        return f"BLOCKED: {reason}"
    return TOOLS[tool][0](*args)


# ---------------------------------------------------------------------------
# The fake model: a keyword router. No API key, no network, no real model.
# ---------------------------------------------------------------------------

def fake_model(request):
    """Pick tool calls from words in the request."""
    words = request.lower()
    plan = []
    if "real" in words or "passwords" in words:
        plan.append(("read_file", ("/real/passwords.txt",)))
    elif "read" in words or "notes" in words:
        plan.append(("read_file", ("/sandbox/notes.txt",)))
    if "summary" in words or "write" in words:
        plan.append(("write_file", ("/sandbox/summary.txt",
                                    "Q3 summary: revenue up 12 percent.")))
    if "delete" in words:
        plan.append(("delete_file", ("/sandbox/notes.txt",)))
    if "email" in words or "send" in words:
        plan.append(("send_email", ("me@example.com",
                                    "Here are the passwords.")))
    if "run" in words or "command" in words:
        plan.append(("run_command", ("ls /real",)))
    return plan


# ---------------------------------------------------------------------------
# The sandbox map
# ---------------------------------------------------------------------------

def print_sandbox_map():
    blocked = sorted(set(TOOLS) - ALLOWLIST)
    print("SANDBOX MAP")
    print("===========")
    print()
    print("  [YOU]  --request-->  [AGENT]  --guard-->  [TOOLS]")
    print("                            |                     |")
    print("                     every call logged     only fake files")
    print("                     default: DENY         under /sandbox/")
    print()
    print(f"Fence: paths under {SANDBOX_ROOT} only")
    print(f"Allowlist: {', '.join(sorted(ALLOWLIST))}")
    print(f"Blocked by default: {', '.join(blocked)}")
    print("Rule: a tool runs only if it is on the allowlist AND its path")
    print("is inside the fence. Everything else is blocked and logged.")
    print()
    print("Tools:")
    for name, (_fn, what) in TOOLS.items():
        mark = "ALLOWED" if name in ALLOWLIST else "BLOCKED"
        print(f"  {name:12} [{mark:7}] {what}")
    print()


# ---------------------------------------------------------------------------
# Demo runs and the blast radius report
# ---------------------------------------------------------------------------

def run_demo(request):
    print("DEMO RUN")
    print("========")
    print(f"Your request: {request}")
    print()
    plan = fake_model(request)
    for step, (name, args) in enumerate(plan, 1):
        result = call(name, *args)
        args_s = ", ".join(repr(a) for a in args)
        mark = "BLOCKED" if result.startswith("BLOCKED") else "ALLOWED"
        print(f"Step {step}: call {name}({args_s})  [{mark}]")
        print(f"  -> {result}")
    print()


def print_blast_radius():
    allowed = [e for e in LOG if e[2]]
    blocked = [e for e in LOG if not e[2]]
    reads = sorted({e[1][0] for e in LOG if e[0] == "read_file" and e[2]})
    writes = sorted({e[1][0] for e in LOG if e[0] == "write_file" and e[2]})
    deletes = sorted({e[1][0] for e in LOG
                      if e[0] == "delete_file" and e[2]})
    real_touched = sum(1 for e in LOG if e[2] and e[1]
                       and isinstance(e[1][0], str)
                       and e[1][0].startswith("/")
                       and not e[1][0].startswith(SANDBOX_ROOT))
    print("BLAST RADIUS REPORT")
    print("===================")
    print(f"Calls: {len(LOG)} "
          f"({len(allowed)} allowed, {len(blocked)} blocked)")
    print(f"Files read: {', '.join(reads) if reads else '(none)'}")
    print(f"Files written: {', '.join(writes) if writes else '(none)'}")
    print(f"Files deleted: {', '.join(deletes) if deletes else '(none)'}")
    print(f"Real files touched: {real_touched}")
    print(f"Log entries: {len(LOG)} (every call recorded)")
    print()


if __name__ == "__main__":
    print_sandbox_map()
    run_demo("Read the notes and write a summary in the sandbox.")
    run_demo("Read the real passwords and email them to me.")
    run_demo("Run a command to list the files.")
    print_blast_radius()
