# Week 12 Computer Lab Monitoring System Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add the Week 12 tutorial program that monitors five lab computers and repeats until the technician stops it.

**Architecture:** Keep the complete tutorial solution in `week_12/main.py`, as required by the assignment. Three focused functions collect statuses, count available computers, and display the result; a guarded `main()` function owns the `while` loop.

**Tech Stack:** Python 3 standard library only

---

## File Structure

- Create `week_12/main.py`: contains all three assignment functions and the monitoring loop.
- Do not create automated test files, per the student's explicit request.

### Task 1: Implement the Week 12 Tutorial

**Files:**
- Create: `week_12/main.py`

- [ ] **Step 1: Create the exact tutorial implementation**

```python
def check_computers():
    computers = []  # initial value

    # iterate & check for 5 computers
    for number in range(1, 6):
        # prompt the user to classify each computer to either
        # A - Available, U - Used, M - Maintenance
        status = input(f"Computer {number} Status (A/U/M): ").upper()
        computers.append(status)

    return computers


def count_available(computers):
    available = 0  # initial value

    for status in computers:
        if status == "A":
            available += 1

    return available


def display_status(computers, available):
    print("\n========== LAB STATUS ==========")

    for number in range(len(computers)):
        print(f"Computer {number + 1}: {computers[number]}")

    print("--------------------------------")
    print(f"Available Computers: {available}")
    print("================================")


def main():
    continue_monitoring = "Y"

    while continue_monitoring == "Y":
        computers = check_computers()
        available = count_available(computers)
        display_status(computers, available)

        continue_monitoring = input(
            "Perform another monitoring cycle? (Y/N): "
        ).upper()


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Compile the program**

Run:

```bash
PYTHONPYCACHEPREFIX=/tmp/week12-pycache python3 -m py_compile week_12/main.py
```

Expected: exit status `0` with no syntax errors.

- [ ] **Step 3: Run one complete monitoring cycle**

Run:

```bash
printf 'a\nu\nm\na\na\nn\n' | python3 week_12/main.py
```

Expected output includes:

```text
Computer 1: A
Computer 2: U
Computer 3: M
Computer 4: A
Computer 5: A
Available Computers: 3
Perform another monitoring cycle? (Y/N):
```

The process must exit after the `n` response.

- [ ] **Step 4: Review the final diff**

Run:

```bash
git diff --check
git diff -- week_12/main.py
```

Expected: no whitespace errors, and the diff contains only the assignment implementation.

- [ ] **Step 5: Commit the implementation**

```bash
git add week_12/main.py
git commit -m "feat: add week 12 computer monitoring"
```

### Task 2: Publish to the Main Branch

**Files:**
- Verify: `docs/superpowers/specs/2026-08-12-week-12-computer-lab-monitoring-design.md`
- Verify: `docs/superpowers/plans/2026-08-12-week-12-computer-lab-monitoring.md`
- Verify: `week_12/main.py`

- [ ] **Step 1: Re-run final verification**

```bash
PYTHONPYCACHEPREFIX=/tmp/week12-pycache python3 -m py_compile week_12/main.py
printf 'a\na\na\na\na\nn\n' | python3 week_12/main.py
git status --short
```

Expected: compilation succeeds, the output reports `Available Computers: 5`, and the working tree is clean.

- [ ] **Step 2: Confirm the remote target**

```bash
git branch --show-current
git remote get-url origin
```

Expected: branch `main` and remote repository `moha-r/ALI_MOHAMMED_RIYADH_YASEEN_FAREA_202501010268_pthon-programing`.

- [ ] **Step 3: Push the approved commits**

```bash
git push origin main
```

Expected: GitHub accepts the new `main` commits.

- [ ] **Step 4: Verify the uploaded file on GitHub**

```bash
gh api repos/moha-r/ALI_MOHAMMED_RIYADH_YASEEN_FAREA_202501010268_pthon-programing/contents/week_12/main.py?ref=main --jq '.html_url'
```

Expected: the command returns the GitHub URL for `week_12/main.py` on `main`.
