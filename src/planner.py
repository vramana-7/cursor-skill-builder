"""Tiny local planner used for daily workflow drills."""

import sys

PRIORITY_FALLBACKS = [
    "Define this week priority",
    "Pick one actionable project task",
    "Protect one focus block on calendar",
]
DEFAULT_NEXT_ACTION = "Block 25 minutes now and start Priority 1."
DEFAULT_RISK_LINE = (
    "Overplanning without execution. Mitigation: start with one 25-minute block."
)


def _parse_context_lines(context: str) -> list[str]:
    return [line.strip("- ").strip() for line in context.splitlines() if line.strip()]


def _build_priority_lines(items: list[str]) -> list[str]:
    top = items[:3]
    result = ["Top Priorities:"]
    for index in range(3):
        text = top[index] if index < len(top) else PRIORITY_FALLBACKS[index]
        result.append(f"{index + 1}) {text}")
    return result


def _build_top_win_line(items: list[str]) -> str:
    win_target = items[0] if items else "Finish Priority 1"
    return f"If completed, this week is a win: {win_target}"


def build_weekly_plan(context: str) -> str:
    lines = _parse_context_lines(context)
    if not lines:
        return "No context provided."

    plan = [
        *_build_priority_lines(lines),
        "",
        "Top Win:",
        _build_top_win_line(lines),
        "",
        "Next Action:",
        DEFAULT_NEXT_ACTION,
        "",
        "Top Risk:",
        DEFAULT_RISK_LINE,
    ]
    return "\n".join(plan)


def main() -> None:
    print("Paste your weekly context (finish with Ctrl-D on macOS/Linux):")
    context = sys.stdin.read()
    print("\n" + build_weekly_plan(context))


if __name__ == "__main__":
    main()
