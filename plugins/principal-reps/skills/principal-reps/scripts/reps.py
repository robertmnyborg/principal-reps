#!/usr/bin/env python3
"""Rep ledger for Principal-level interview practice.

Tracking progress is a guarantee, not an estimate, so the arithmetic lives here
instead of being eyeballed. Append one row per rep, then read trends.

    python3 reps.py log --q 17 --scores 2,2,3,1,2,1,1 --mode rep --sec 95
    python3 reps.py report
    python3 reps.py report --last 20
    python3 reps.py weak
    python3 reps.py ready
"""

import argparse, csv, os, sys
from datetime import datetime, timezone

DIMS = ["ambiguity", "scope", "technical", "operations", "mechanism", "cheapest_test", "reversibility"]
# Ledgers written before the rename still load: old column name -> current one.
ALIASES = {"frugality": "cheapest_test", "doors": "reversibility"}

def ledger_path(explicit=None):
    """Per-user ledger. --ledger wins, then $PRINCIPAL_REPS_DIR, then the default dir."""
    if explicit:
        return os.path.expanduser(explicit)
    d = os.environ.get("PRINCIPAL_REPS_DIR", "~/Projects/principal-reps")
    return os.path.join(os.path.expanduser(d), "reps.csv")


LEDGER = ledger_path()
HEADER = ["ts", "mode", "target", "question", "domain", "seconds"] + DIMS + ["note"]

# Kill condition: every dimension averaging >= 2.0 over this many most-recent reps.
READY_WINDOW = 15
READY_BAR = 2.0


def migrate():
    """Add columns introduced after a ledger was created, in place."""
    if not os.path.exists(LEDGER):
        return
    with open(LEDGER, newline="") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0] == HEADER:
        return
    renamed = [c for c in rows[0] if c in ALIASES]
    old = [ALIASES.get(c, c) for c in rows[0]]
    missing = [c for c in HEADER if c not in old]
    if not missing and not renamed:
        return
    idx = {c: old.index(c) for c in old}
    # Keep columns this version does not know, after ours, so no data is dropped.
    out = HEADER + [c for c in old if c not in HEADER]
    with open(LEDGER, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(out)
        for r in rows[1:]:
            w.writerow([r[idx[c]] if c in idx and idx[c] < len(r) else "" for c in out])
    changes = [f"renamed {c} -> {ALIASES[c]}" for c in renamed] + [f"added {c}" for c in missing]
    print(f"# ledger migrated: {', '.join(changes)}", file=sys.stderr)


def load(target=None):
    if not os.path.exists(LEDGER):
        return []
    with open(LEDGER, newline="") as f:
        rows = list(csv.DictReader(f))
    if target:
        rows = [r for r in rows if (r.get("target") or "") == target]
    return rows


def cmd_domains(a):
    """Coverage by domain and by question id, so sampling gaps are visible."""
    rows = load(getattr(a, "target", None))
    if not rows:
        sys.exit("no reps logged yet")
    counts = {}
    for r in rows:
        counts[r.get("domain") or "(untagged)"] = counts.get(r.get("domain") or "(untagged)", 0) + 1
    print(f"{len(rows)} reps across {len(counts)} domains\n")
    width = max(len(d) for d in counts)
    for d, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {d:<{width}}  {n:>3}  {'#' * n}")
    seen = {r["question"] for r in rows}
    print(f"\n{len(seen)} distinct questions used; "
          f"{len(rows) - len(seen)} repeat(s)")


def cmd_log(a):
    scores = [s.strip() for s in a.scores.split(",")]
    if len(scores) != len(DIMS):
        sys.exit(f"need {len(DIMS)} scores in order {','.join(DIMS)}; got {len(scores)}")
    for s in scores:
        if s not in {"0", "1", "2", "3"}:
            sys.exit(f"scores must be 0-3, got {s!r}")
    os.makedirs(os.path.dirname(LEDGER), exist_ok=True)
    new = not os.path.exists(LEDGER)
    with open(LEDGER, "a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(HEADER)
        w.writerow([datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    a.mode, a.target or "", a.q, a.domain or "", a.sec or ""]
                   + scores + [a.note or ""])
    print(f"logged rep {len(load())}: q{a.q} [{a.mode}] {a.scores}")


def averages(rows):
    if not rows:
        return {}
    return {d: sum(int(r[d]) for r in rows) / len(rows) for d in DIMS}


def bar(v):
    filled = int(round(v * 4))
    return "#" * filled + "." * (12 - filled)


def cmd_report(a):
    rows = load(a.target)
    if not rows:
        sys.exit("no reps logged yet" + (f" for target {a.target}" if a.target else ""))
    window = rows[-a.last:] if a.last else rows
    avg = averages(window)
    prior = rows[-2 * a.last:-a.last] if a.last and len(rows) >= 2 * a.last else None
    pavg = averages(prior) if prior else {}

    scope = f" [target: {a.target}]" if a.target else ""
    print(f"{len(rows)} reps logged{scope}; showing last {len(window)}\n")
    print(f"{'dimension':<14} {'avg':>5}  {'':<12} {'trend':>7}")
    print("-" * 44)
    for d in sorted(DIMS, key=lambda x: avg[x]):
        delta = f"{avg[d] - pavg[d]:+.2f}" if pavg else "  --"
        print(f"{d:<14} {avg[d]:>5.2f}  {bar(avg[d]):<12} {delta:>7}")

    times = [int(r["seconds"]) for r in window if r.get("seconds")]
    if times:
        over = sum(1 for t in times if t > 90)
        print(f"\nmedian answer {sorted(times)[len(times)//2]}s; "
              f"{over}/{len(times)} over the 90s budget")

    weakest = min(DIMS, key=lambda d: avg[d])
    print(f"\nweakest: {weakest} ({avg[weakest]:.2f})")


def cmd_weak(a):
    """Dimensions to over-sample next session."""
    rows = load(getattr(a, "target", None))
    if not rows:
        sys.exit("no reps logged yet")
    avg = averages(rows[-READY_WINDOW:])
    weak = [d for d in DIMS if avg[d] < READY_BAR]
    if not weak:
        print("no dimension below the bar; sample evenly")
        return
    print("over-sample these next set (weakest first):")
    for d in sorted(weak, key=lambda x: avg[x]):
        print(f"  {d:<14} {avg[d]:.2f}")


def cmd_targets(a):
    """Rep counts per target, so a stale target is visible."""
    rows = load()
    if not rows:
        sys.exit("no reps logged yet")
    groups = {}
    for r in rows:
        groups.setdefault(r.get("target") or "(general)", []).append(r)
    width = max(len(t) for t in groups)
    print(f"{len(rows)} reps across {len(groups)} target(s)\n")
    for t, grp in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        avg = averages(grp)
        weakest = min(DIMS, key=lambda d: avg[d])
        print(f"  {t:<{width}}  {len(grp):>3} reps   weakest: {weakest} ({avg[weakest]:.2f})")


def cmd_ready(a):
    rows = load()
    n = len(rows)
    if n < READY_WINDOW:
        print(f"not ready to judge: {n}/{READY_WINDOW} reps logged")
        return
    avg = averages(rows[-READY_WINDOW:])
    failing = {d: v for d, v in avg.items() if v < READY_BAR}
    print(f"kill condition: every dimension >= {READY_BAR} over the last {READY_WINDOW} reps\n")
    for d in DIMS:
        mark = "PASS" if avg[d] >= READY_BAR else "fail"
        print(f"  {d:<14} {avg[d]:.2f}  {mark}")
    print()
    if failing:
        print(f"NOT READY. {len(failing)} dimension(s) below bar: {', '.join(failing)}")
    else:
        print("READY. Drop the model, run reps from the card and a timer.")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("log")
    s.add_argument("--q", required=True, help="question id from the bank, or a short slug")
    s.add_argument("--scores", required=True, help="7 values 0-3, in order: " + ",".join(DIMS))
    s.add_argument("--mode", default="rep",
                   choices=["rep", "set", "pattern", "weakness", "narrative", "live"])
    s.add_argument("--target", default=None, help="target slug, e.g. acme-staff-pm")
    s.add_argument("--domain", default=None)
    s.add_argument("--sec", type=int, default=None, help="seconds the answer took")
    s.add_argument("--note", default=None)
    s.set_defaults(fn=cmd_log)

    s = sub.add_parser("report")
    s.add_argument("--last", type=int, default=None)
    s.add_argument("--target", default=None, help="scope to one target")
    s.set_defaults(fn=cmd_report)

    s = sub.add_parser("weak"); s.add_argument("--target", default=None); s.set_defaults(fn=cmd_weak)
    sub.add_parser("ready").set_defaults(fn=cmd_ready)
    s = sub.add_parser("domains"); s.add_argument("--target", default=None); s.set_defaults(fn=cmd_domains)
    sub.add_parser("targets").set_defaults(fn=cmd_targets)

    p.add_argument("--ledger", default=None,
                   help="path to a specific user's reps.csv (default: $PRINCIPAL_REPS_DIR)")

    a = p.parse_args()
    global LEDGER
    LEDGER = ledger_path(a.ledger)
    migrate()
    a.fn(a)


if __name__ == "__main__":
    main()
