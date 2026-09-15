# Autonomous AI Coding Agent

An autonomous software engineering agent built in Python. The agent leverages the Gemini API via the OpenAI-compatible interface, implementing Tool Calling and a closed agent feedback loop. It inspects local files, analyzes source code, applies targeted modifications, and validates changes by running tests autonomously.

---

## Overview

Modern coding agents act as decision-making engines rather than simple text generators. This agent receives user prompts, plans tool calls via JSON Schema declarations, executes safe filesystem and Python operations locally, and feeds back execution output until the task passes verification.

---

## Key Capabilities

* **Workspace Exploration:** Traverses project directories and lists files with metadata.
* **Code Inspection:** Reads file contents to diagnose bugs and trace call stacks.
* **Targeted File Writing:** Safely modifies or creates files without corrupting surrounding logic.
* **Automated Verification:** Runs test scripts and reads exit codes and stderr/stdout outputs to confirm fixes.
* **Autonomous Termination:** Stops the agent loop and returns a final explanation once all tests pass.

---

## Available Agent Tools

| Tool | Description |
| :--- | :--- |
| `get_files_info` | Lists files and subdirectories with size and directory flags. |
| `get_file_content` | Reads and returns full textual file contents. |
| `write_file` | Writes or overwrites text content to a relative file path. |
| `run_python_file` | Executes Python scripts locally with optional arguments. |

All operations enforce workspace path containment via canonical path verification to prevent directory traversal outside the target folder.

---

## Project Structure

```text
ai-agent/
├── calculator/
│   ├── pkg/
│   │   ├── calculator.py
│   │   └── render.py
│   ├── main.py
│   └── tests.py
├── functions/
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── call_function.py
├── config.py
├── main.py
├── prompts.py
├── pyproject.toml
└── .env.example
```

---

## Getting Started

### Prerequisites

* Python 3.10+
* [uv](https://github.com/astral-sh/uv)
* Gemini API Key (`GEMINI_API_KEY`)

### Installation

1. Clone the repository:
```bash
git clone [https://github.com/ERB3K/ai-agent.git](https://github.com/ERB3K/ai-agent.git)
cd ai-agent
```

2. Create and configure environment variables:
```bash
cp .env.example .env
```

Add your API key inside `.env`:
```env
GEMINI_API_KEY="your-gemini-api-key"
```

3. Synchronize dependencies:
```bash
uv sync
```

---

## Usage

### Inspect Codebase
```bash
uv run main.py "Explain how the calculator renders its output"
```

### Verbose Mode
Observe intermediate tool calls and model reasoning in real time:
```bash
uv run main.py --verbose "Run tests.py and report the result"
```

### Autonomous Debugging
```bash
uv run main.py --verbose "Fix the bug: 3 + 7 * 2 shouldn't be 20."
```

---

## Security Notice

This agent executes local Python code and performs filesystem writes. Never point the working directory to root or sensitive system paths.
