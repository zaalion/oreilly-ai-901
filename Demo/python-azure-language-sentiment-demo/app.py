import os
import sys
import requests
from dotenv import load_dotenv

# Load values from a local .env file if present.
load_dotenv()

API_VERSION = "2026-05-01"

def main():
    endpoint = os.getenv("LANGUAGE_ENDPOINT")
    key = os.getenv("LANGUAGE_KEY")

    if not endpoint or not key:
        print("Missing Azure Language configuration.")
        print("Create a .env file with:")
        print("LANGUAGE_ENDPOINT=https://<your-resource-endpoint>")
        print("LANGUAGE_KEY=<your-key>")
        sys.exit(1)

    sentence = input("Enter a sentence to analyze: ").strip()

    if not sentence:
        print("No sentence provided.")
        return

    url = f"{endpoint.rstrip('/')}/language/:analyze-text?api-version={API_VERSION}"

    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/json",
    }

    payload = {
        "kind": "SentimentAnalysis",
        "parameters": {
            "modelVersion": "latest"
        },
        "analysisInput": {
            "documents": [
                {
                    "id": "1",
                    "language": "en",
                    "text": sentence
                }
            ]
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        document = result["results"]["documents"][0]
        scores = document["confidenceScores"]

        print("\nSentiment analysis result")
        print("-------------------------")
        print(f"Sentiment: {document['sentiment']}")
        print(f"Positive : {scores['positive']:.2f}")
        print(f"Neutral  : {scores['neutral']:.2f}")
        print(f"Negative : {scores['negative']:.2f}")

    except requests.exceptions.HTTPError:
        print(f"\nAzure API returned HTTP {response.status_code}")
        try:
            print(response.json())
        except ValueError:
            print(response.text)
    except requests.exceptions.RequestException as ex:
        print(f"\nRequest failed: {ex}")


if __name__ == "__main__":
    main()
