from pathlib import Path
import subprocess

PROJECT_ROOT = Path(__file__).resolve().parents[1]

BACKGROUND = PROJECT_ROOT / "assets" / "background.jpg"
VOICE = PROJECT_ROOT / "voice.wav"
MUSIC = PROJECT_ROOT / "assets" / "music.mp3"
OUTPUT = PROJECT_ROOT / "final.mp4"


def build_video():
    if not BACKGROUND.exists():
        raise FileNotFoundError(f"Missing background: {BACKGROUND}")
    if not VOICE.exists():
        raise FileNotFoundError(f"Missing voice.wav")
    if not MUSIC.exists():
        raise FileNotFoundError(f"Missing music.mp3")

    cmd = [
        "ffmpeg", "-y",
        "-loop", "1", "-i", str(BACKGROUND),
        "-i", str(VOICE),
        "-i", str(MUSIC),
        "-filter_complex",
        "[2:a]volume=0.12,asetpts=N/SR/TB[music];"
        "[1:a][music]amix=inputs=2:dropout_transition=2,aresample=async=1[a]",
        "-map", "0:v",
        "-map", "[a]",
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        "-s", "1080x1920",
        str(OUTPUT)
    ]

    subprocess.run(cmd, check=True)
    print("✅ final.mp4 created")


if __name__ == "__main__":
    build_video()
