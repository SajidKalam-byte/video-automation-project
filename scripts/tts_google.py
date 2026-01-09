"""Google Cloud Text-to-Speech helper (scaffold).

Requires:
- google-cloud-texttospeech
- GOOGLE_APPLICATION_CREDENTIALS set to a service account json

Note: This is separate from YouTube OAuth (client_secret.json).
"""

from __future__ import annotations

from pathlib import Path

from google.cloud import texttospeech


def synthesize_to_wav(ssml: str, out_path: Path, *, voice_name: str = "en-US-Neural2-D") -> None:
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(ssml=ssml)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name=voice_name,
    )
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.LINEAR16)

    response = client.synthesize_speech(
        request={"input": synthesis_input, "voice": voice, "audio_config": audio_config}
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(response.audio_content)
