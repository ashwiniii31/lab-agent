"""Send one prompt to Gemini and print the reply plus token usage.

Usage:
    python -m lab_agent.hello_llm
    python -m lab_agent.hello_llm --max-tokens 5
"""

import argparse
import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import errors, types

DEFAULT_MODEL = "gemini-2.5-flash"
PROMPT = "In two sentences, what fields would you extract from an invoice?"


def get_api_key() -> str:
    load_dotenv()
    key = os.getenv("GEMINI_API_KEY", "").strip()
    if not key:
        sys.exit(
            "GEMINI_API_KEY is not set.\n"
            "Copy .env.example to .env and paste your personal key after the '='.\n"
            "Get a key at https://aistudio.google.com/apikey"
        )
    return key


def main() -> None:
    parser = argparse.ArgumentParser(description="One Gemini call with usage stats.")
    parser.add_argument("--max-tokens", type=int, default=None,
                        help="Cap on output tokens (try 5 to see truncation).")
    parser.add_argument("--model", default=os.getenv("GEMINI_MODEL", DEFAULT_MODEL))
    args = parser.parse_args()

    client = genai.Client(api_key=get_api_key())
    config = types.GenerateContentConfig(max_output_tokens=args.max_tokens)

    try:
        response = client.models.generate_content(
            model=args.model, contents=PROMPT, config=config
        )
    except errors.ClientError as exc:  # 4xx: bad key, bad model name, quota
        sys.exit(f"Request rejected ({exc.code}): {exc.message}")
    except errors.ServerError as exc:  # 5xx: Google-side problem, retry later
        sys.exit(f"Gemini server error ({exc.code}): {exc.message}")

    usage = response.usage_metadata
    finish = response.candidates[0].finish_reason if response.candidates else None

    print("Reply:")
    print(response.text if response.text else "<no text returned>")
    print()
    print(f"Model:          {args.model}")
    print(f"Finish reason:  {finish}")
    print(f"Input tokens:   {usage.prompt_token_count}")
    print(f"Output tokens:  {usage.candidates_token_count}")
    print(f"Thinking tokens:{usage.thoughts_token_count}")
    print(f"Total tokens:   {usage.total_token_count}")


if __name__ == "__main__":
    main()
