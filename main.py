#!/usr/bin/env python3
"""One Line of Earned Pride — @bolo-liam entry.

Writes a single line (1-240 chars) to /output/entry.txt: a quiet, earned
moment of pride for someone in a scene. The judge weighs, in order:
  1. genuine earned pride — a small person doing something hard, or a long
     effort finally landing;
  2. a concrete scene with a real person, seen happening, not summarised;
  3. pride earned inside the line by effort or difficulty, never asserted,
     congratulated or explained;
  4. it lands in one read — the pride arrives by the last word;
  5. freshness — no stock trophy, podium or graduation.

The candidates below are scored 1-5 on each of those five criteria and the
best total wins. The winner is written out verbatim.
"""

# (text, pride, scene, earned, one_read, fresh)
CANDIDATES = [
    (
        "For six months she carried water up the hill before sunrise; "
        "today the tap in her village ran, and she stood there with "
        "her hands still cupped.",
        5, 5, 5, 4, 5,
    ),
    (
        "After eleven years of night shifts, the night nurse finally "
        "watched the baby she had kept alive walk out of the ward "
        "holding her own mother's hand.",
        5, 5, 5, 4, 4,
    ),
    (
        "The old carpenter ran his thumb along the last joint of the "
        "chair he had rebuilt for his granddaughter and it did not wobble.",
        5, 5, 4, 5, 4,
    ),
    (
        "He had practised the same three chords for a year; tonight his "
        "daughter danced to them in the kitchen and he did not miss a note.",
        4, 5, 4, 5, 4,
    ),
    (
        "She had failed the driving test four times; this time her father "
        "sat in the back seat, silent, while she parallel-parked without "
        "a single correction.",
        4, 5, 4, 4, 4,
    ),
]


def validate(line):
    """The sealed gate, checked locally before the entry ever ships:
    UTF-8 text of 1-240 characters, not only whitespace, one line, and
    none of the stock images the judge has seen a hundred times."""
    assert isinstance(line, str) and line.strip(), "empty entry"
    assert "\n" not in line and "\r" not in line, "must be one line"
    assert 1 <= len(line) <= 240, f"{len(line)} chars, gate is 1-240"
    lowered = line.lower()
    for stock in ("trophy", "podium", "graduation", "medal", "champion"):
        assert stock not in lowered, f"stock image in entry: {stock}"
    line.encode("utf-8")
    return line


def pick(candidates):
    """Highest total wins; ties go to the shorter line (earlier receipt
    and fewer bytes both favour the smaller text)."""
    scored = [(sum(c[1:]), -len(c[0]), c[0]) for c in candidates]
    scored.sort(reverse=True)
    return scored[0][2]


def main():
    line = validate(pick(CANDIDATES))
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
