# Keylogger
A minimal Python keylogger built with pynput that records every key press and a timestamp into keylogs.csv. Designed as a learning tool to explore event listeners, CSV I/O, and simple input normalization — only for authorized, local, or lab use. 

# Keylogger (Educational / Audit Use Only)

> ⚠️ Important — READ THIS FIRST
> This repository contains a simple key-capture script (a keylogger). It must only be used for ethical, legal, and consented purposes — e.g., personal learning, testing on your own machine or a disposable VM, or an explicit, written penetration test with authorization.
> Do not run this on systems you don't own or don't have explicit permission for. Doing so may be illegal and could get you into serious trouble. No heroics. No sketchy shit.

---

## What this is

This is a tiny, dependency-light Python script that listens to keyboard events and appends them to a CSV file (`keylogs.csv`) along with a timestamp.

It’s meant for educational purposes — to learn how keyboard event listeners work, how to safely log events for debugging, or how to build defensive tooling that detects malicious logging.

## Quick features

* Listens to keyboard presses using `pynput`.
* Writes a timestamped CSV row for every key press.
* Normalizes common keys into readable tokens: `[SPACE]`, `[ENTER]`, `[TAB]`, `[BACKSPACE]`, and `[SHIFT]` / `[CTRL]`-style tokens.
* Minimal external deps.

## Dependencies

* Python 3.8+ (recommended)
* `pynput` (for capturing keyboard events)

Install `pynput`:

```bash
pip install pynput
```

---

## Files

* `keylogger.py` — the main script (your provided code).
* `keylogs.csv` — created automatically (if not present) and used to store captured events.

---

## How it works (high level — no hacking hacks)

* The script sets up a CSV file with headers (`Timestamp`, `Key`) if it doesn't already exist.
* A `pynput.keyboard.Listener` is started and calls `write_to_csv` on every key press.
* `write_to_csv`:

  * Builds a timestamp string via `datetime.now()`.
  * Converts special keys to readable tokens (`[SPACE]`, `[ENTER]`, etc.).
  * Appends a new CSV row: `[timestamp, key]`.
* The listener runs until you stop the process (e.g., `Ctrl+C` in the terminal).

---

## Running (safe, local testing only)

Use at your own risk, but if you're practicing on a VM or your own environment:

```bash
python keylogger.py
```

The script prints a console line whenever it captures a key: `CAPTURED: <key>`. Press Ctrl+C to stop.

Reminder: only run on machines you own or where you have explicit authorization. If someone asks you to help "monitor" their machine, get that consent in writing.


## Safe usage & best practices

* Use a VM or an isolated environment when testing. Snapshot it beforehand so you can revert.
* Get explicit, written consent before using on another person's system (e.g., part of a pen-test engagement).
* Avoid persistence / stealth modifications. This repo purposefully does not include startup/persistence instructions or exfiltration techniques.
* Sanitize logs before sharing. Keylogs can contain extremely sensitive information (passwords, private messages).
* Delete logs securely when you’re done. Don't hoard raw logs.

## How to stop & clean up

* Stop the script with `Ctrl+C` in the terminal.
* To remove logs:

```bash
rm keylogs.csv
```

(Or securely delete using OS tools if the file contained sensitive info.)

---

## Extending for defensive research (ethical ideas)

If you're learning or building defensive tools, consider modifications that are useful *for protection and detection* rather than abuse:

* Add a mode to generate alerts when a keylogger is detected on a machine (e.g., compare running processes, signed binaries, unexpected file creation).
* Hash or redact sensitive inputs in the log (e.g., replace sequences that look like passwords with `[REDACTED]`).
* Add tests and integrate the script inside a controlled honeypot environment to study attacker behavior (with consent).

Do not extend this repo with stealth, persistence, or exfiltration capabilities — those are explicitly harmful.

---

## Troubleshooting

* If keys aren't captured:

  * Make sure `pynput` is installed and you’re running with sufficient permissions.
  * On some OS configurations, keyboards or accessibility permissions must be granted (especially macOS).
* If `keylogs.csv` won’t create:

  * Check file system permissions and current working directory.
* If things crash, check the console for the printed `Error: ...` messages.

---

## Legal & Ethical Notice

This code is for learning. Using it to spy on people, steal credentials, or persistently infect devices is illegal and unethical. If you’re exploring offensive security, do it in structured, authorized environments (CTFs, company-approved labs, bug bounties with explicit scope).

If you’re ever unsure whether an action is permissible — don’t do it. Ask. Get written permission. Stay on the right side of the law.


## License

Use this code for education and defensive work only. You may adapt it, but you are responsible for how you use it.

## Contact / Want help learning ethically?

If you want help turning this into a defensive exercise, creating a safe VM lab, or learning how to detect keyloggers (how to build sensors, rules, or signatures), say so and I’ll help — ethically and legally. No shady shit. 👾

---

*Readable, minimal, and honest — like a decent tutorial and less like a shady midnight script.*

