import argparse
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI
from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")

    parser = argparse.ArgumentParser(description="AI Agent CLI")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the AI")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    args = parser.parse_args()

    client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]

    for _ in range(20):
        response = client.chat.completions.create(
            model="gemini-3.5-flash-lite",
            messages=messages,
            tools=available_functions,
            temperature=0,
        )

        message = response.choices[0].message
        messages.append(message)

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose=args.verbose)
                if not result_message.get("content"):
                    raise Exception(
                        f"Empty content returned from function {tool_call.function.name}"
                    )
                if args.verbose:
                    print(f"-> {result_message['content']}")
                messages.append(result_message)
        else:
            if message.content:
                print(message.content)
            return

    print("Error: Agent reached maximum iterations without completing the task.")
    sys.exit(1)


if __name__ == "__main__":
    main()