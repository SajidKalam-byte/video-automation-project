from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent
SCRIPT_TXT = SCRIPTS_DIR / "generated_script.txt"
SCRIPT_SSML = SCRIPTS_DIR / "script.ssml"


def text_to_ssml(text: str) -> str:
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    ssml = ["<speak>"]

    for line in lines:
        ssml.append(
            f'<prosody rate="104%" pitch="+2st" volume="+5dB">'
            f"{line}"
            f"</prosody><break time='300ms'/>"
        )

    ssml.append("</speak>")
    return "\n".join(ssml)


def main():
    if not SCRIPT_TXT.exists():
        raise FileNotFoundError("generated_script.txt not found")

    text = SCRIPT_TXT.read_text(encoding="utf-8")
    ssml = text_to_ssml(text)

    SCRIPT_SSML.write_text(ssml, encoding="utf-8")
    print("✅ script.ssml created")


if __name__ == "__main__":
    main()
