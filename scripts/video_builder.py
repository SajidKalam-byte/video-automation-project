import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

VOICE = ROOT / "voice.wav"
BG = ROOT / "assets" / "background.jpg"
OUT = ROOT / "final.mp4"

def build_video():
    if not VOICE.exists():
        raise FileNotFoundError("Missing voice.wav")

    if not BG.exists():
        raise FileNotFoundError("Missing assets/background.jpg")

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1",
        "-i", str(BG),
        "-i", str(VOICE),
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-s", "1080x1920",
        str(OUT)
    ]

    subprocess.run(cmd, check=True)
    print("✅ final.mp4 created")

if __name__ == "__main__":
    build_video()
