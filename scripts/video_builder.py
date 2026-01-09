"""Video builder scaffold.

This file is intentionally minimal. You can later implement using ffmpeg or moviepy.
"""

from __future__ import annotations

from pathlib import Path


def build_video(*, background_image: Path, narration_wav: Path, out_mp4: Path) -> None:
    # Placeholder: implement with ffmpeg/moviepy.
    raise NotImplementedError("Implement video build with ffmpeg or moviepy")
