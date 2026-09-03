import os
import sys
import html
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION", "centralus")
SPEECH_VOICE = os.getenv("SPEECH_VOICE", "en-US-Ava:DragonHDLatestNeural")

OUTPUT_FILE = Path(__file__).parent / "output.mp3"


def main():
    if not SPEECH_KEY:
        print("Missing SPEECH_KEY.")
        print("Create a .env file and add your Azure Speech key.")
        sys.exit(1)

    text = input("Enter the text to convert to speech: ").strip()

    if not text:
        print("No text provided.")
        return

    url = (
        f"https://{SPEECH_REGION}.tts.speech.microsoft.com"
        "/cognitiveservices/v1"
    )

    headers = {
        "Ocp-Apim-Subscription-Key": SPEECH_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
        "User-Agent": "AzureSpeechTTSDemo",
    }

    safe_text = html.escape(text)

    ssml = f"""
<speak version="1.0" xml:lang="en-US">
    <voice name="{SPEECH_VOICE}">
        {safe_text}
    </voice>
</speak>
""".strip()

    try:
        response = requests.post(
            url,
            headers=headers,
            data=ssml.encode("utf-8"),
            timeout=60,
        )

        response.raise_for_status()

        OUTPUT_FILE.write_bytes(response.content)

        print("\nSpeech generated successfully.")
        print(f"Voice: {SPEECH_VOICE}")
        print(f"Audio saved to: {OUTPUT_FILE}")

    except requests.exceptions.HTTPError:
        print(f"\nAzure Speech API returned HTTP {response.status_code}")
        print(response.text)
    except requests.exceptions.RequestException as ex:
        print(f"\nRequest failed: {ex}")


if __name__ == "__main__":
    main()
