"""Generate a short-form script text file.

This is a minimal scaffold: you can later swap in an LLM call or a topic list.
"""

from __future__ import annotations

from pathlib import Path


DEFAULT_OUT_DIR = Path("scripts")


def generate(topic: str) -> str:
    # Placeholder implementation.
    # Keep this function pure so it can be tested.
    return (
        f"{topic} can surprise you.\n\n"
        "Here is a tight 45–60 second script scaffold.\n"
        "Add a hook, 3 facts, a twist, and a question.\n"
    )


def main() -> None:
    topic = "AI + Tech Fact"
    script_text = generate(topic)

    DEFAULT_OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = DEFAULT_OUT_DIR / "generated_script.txt"
    out_file.write_text(script_text, encoding="utf-8")

    print(f"Wrote: {out_file}")


if __name__ == "__main__":
    main()
