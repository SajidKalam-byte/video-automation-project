from pathlib import Path
from google.cloud import texttospeech

ROOT = Path(__file__).resolve().parent.parent
SSML_FILE = ROOT / "scripts" / "script.ssml"
OUT_WAV = ROOT / "voice.wav"


def main():
    if not SSML_FILE.exists():
        raise FileNotFoundError("script.ssml missing")

    client = texttospeech.TextToSpeechClient()

    ssml_text = SSML_FILE.read_text(encoding="utf-8")

    synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Neural2-D"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        speaking_rate=1.02
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    OUT_WAV.write_bytes(response.audio_content)
    print("✅ voice.wav created")


if __name__ == "__main__":
    main()
