# Azure Speech Text-to-Speech REST API Demo

A simple Python console application that:

1. asks the user to enter text,
2. calls the Azure Speech Text-to-Speech REST API,
3. receives MP3 audio,
4. saves the audio as `output.mp3` in the project folder.

The application uses the Azure Speech service available through Microsoft Foundry Tools.

## Project files

```text
azure-speech-tts-demo/
├── app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

After you run the application successfully, this file is created:

```text
output.mp3
```

## 1. Open the project in VS Code

Extract the ZIP file and open the project folder in Visual Studio Code.

## 2. Create a virtual environment

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## 4. Create the `.env` file

Copy `.env.example` and rename the copy to `.env`.

Example:

```text
SPEECH_KEY=YOUR_AZURE_SPEECH_KEY
SPEECH_REGION=centralus
SPEECH_VOICE=en-US-Ava:DragonHDLatestNeural
```

Replace `YOUR_AZURE_SPEECH_KEY` with your actual Azure Speech resource key.

If your resource is not in Central US, change `SPEECH_REGION`.

You can also replace `SPEECH_VOICE` with another voice returned by the Azure Speech List Voices API.

## 5. Run

```powershell
python app.py
```

Example:

```text
Enter the text to convert to speech: Welcome to Microsoft Foundry.

Speech generated successfully.
Voice: en-US-Ava:DragonHDLatestNeural
Audio saved to: C:\...\azure-speech-tts-demo\output.mp3
```

## REST API used

For Central US:

```http
POST https://centralus.tts.speech.microsoft.com/cognitiveservices/v1
```

Headers:

```http
Ocp-Apim-Subscription-Key: <your-key>
Content-Type: application/ssml+xml
X-Microsoft-OutputFormat: audio-16khz-128kbitrate-mono-mp3
User-Agent: AzureSpeechTTSDemo
```

The request body is SSML. The API returns the generated audio as binary data, which the application writes directly to `output.mp3`.

## Security

The `.env` file is excluded by `.gitignore`. Do not commit your real Speech key to source control.
