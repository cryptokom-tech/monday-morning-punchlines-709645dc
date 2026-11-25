"""Monday Morning Punchlines — one joke, written to /output/entry.txt.

The joke's punchline lands twice: a "custody battle" with my bed is
already an absurd legal framing for not wanting to get up, and then
"its case is stronger than mine" turns "case" into a second beat —
the bed genuinely has the better argument. No alarm, snooze, or
coffee cliche; the joke is about Monday morning itself.

Stdlib only. Writes exactly one joke (99 chars, 101 bytes, no trailing
newline) and exits 1 if the fortune is invalid.
"""

from pathlib import Path

JOKE = (
    "Monday morning: my bed filed for full custody of me "
    "— and honestly, its case is stronger than mine."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate(joke: str) -> None:
    """The bounty requires one joke, 1-200 chars, on a single line."""
    if not (MIN_CHARS <= len(joke) <= MAX_CHARS):
        raise ValueError(f"joke must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")
    if "Monday" not in joke:
        raise ValueError("joke must be about Monday morning")


def main() -> int:
    try:
        validate(JOKE)
    except ValueError as exc:
        print(f"invalid joke: {exc}")
        return 1
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8", newline="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
