"""Tiny local planner used for daily workflow drills."""

import sys


def build_weekly_plan(context: str) -> str:
    lines = [line.strip("- ").strip() for line in context.splitlines() if line.strip()]
    if not lines:
        return "No context provided."

    top = lines[:3]
    plan = [
        "Top Priorities:",
        f"1) {top[0] if len(top) > 0 else 'Define this week priority'}",
        f"2) {top[1] if len(top) > 1 else 'Pick one actionable project task'}",
        f"3) {top[2] if len(top) > 2 else 'Protect one focus block on calendar'}",
        "",
        "Top Win:",
        f"If completed, this week is a win: {top[0] if len(top) > 0 else 'Finish Priority 1'}",
        "",
        "Next Action:",
        "Block 25 minutes now and start Priority 1.",
        "",
        "Top Risk:",
        "Overplanning without execution. Mitigation: start with one 25-minute block.",
    ]
    return "\n".join(plan)


def main() -> None:
    print("Paste your weekly context (finish with Ctrl-D on macOS/Linux):")
    context = sys.stdin.read()
    print("\n" + build_weekly_plan(context))


if __name__ == "__main__":
    main()
