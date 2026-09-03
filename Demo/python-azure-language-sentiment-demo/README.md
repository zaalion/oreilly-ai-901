# Azure Language Sentiment Analysis Demo

This simple Python console app asks the user for a sentence and calls the Azure Language Text Analysis REST API for sentiment analysis.

## 1. Open the folder in VS Code

Extract the ZIP and open the project folder in Visual Studio Code.

## 2. Create a virtual environment

```powershell
python -m venv .venv
.venv\Scripts\activate
```

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

## 4. Create your `.env` file

Copy:

```text
.env.example
```

and rename the copy to:

```text
.env
```

Then replace the dummy values:

```text
LANGUAGE_ENDPOINT=https://your-language-resource.cognitiveservices.azure.com
LANGUAGE_KEY=YOUR_ACTUAL_KEY
```

The application automatically loads `.env` using `python-dotenv`.

## 5. Run

```powershell
python app.py
```

Example:

```text
Enter a sentence to analyze: I really enjoyed this course.

Sentiment analysis result
-------------------------
Sentiment: positive
Positive : 0.99
Neutral  : 0.01
Negative : 0.00
```

`.env` is included in `.gitignore`, so your real key should not be committed to Git.
