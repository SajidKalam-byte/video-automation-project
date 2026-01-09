"""Convert plain script text to basic SSML for TTS."""

from __future__ import annotations

import re


def to_ssml(text: str) -> str:
    # Minimal SSML: escape &, <, > and add breaks between sentences.
    escaped = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .strip()
    )

    # Insert short breaks after sentence endings.
    escaped = re.sub(r"([.!?])\s+", r"\1<break time=\"250ms\"/> ", escaped)

    return f"<speak>{escaped}</speak>"
