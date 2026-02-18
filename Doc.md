# 📘 Technical Documentation - Code Reviewer Agent

This document outlines the internal logic and configuration of the AI Code Reviewer Agent.

## 🛠️ Internal Architecture

The project is built on an **Asynchronous Client-Server model**.

### 1. Data Handling (Frontend)
The frontend uses the `fetch` API to send code snippets to the backend. It includes a specific logic to parse "ERROR:" and "TIP:" prefixes to apply dynamic CSS styling.

### 2. AI Orchestration (Backend)
The FastAPI backend acts as a proxy. It performs the following steps:
1. Starts a timer using `time.time()`.
2. Loads `GITHUB_TOKEN` from environment variables.
3. Sends a strictly formatted prompt to the Scaledown API.
4. Calculates the final latency (runtime) before sending the response back.

## 🤖 AI Prompting Logic
We use a **System Role** to constrain the AI's behavior:
- **Format:** Plain text only (No markdown backticks).
- **Limit:** Exactly 3 actionable points.
- **Categorization:** Must start with 'ERROR:' or 'TIP:'.

## ⚙️ Environment Variables
| Variable | Purpose |
| :--- | :--- |
| `GITHUB_TOKEN` | Required for authenticating with Scaledown/GitHub Models. |
| `SCALEDOWN_API_URL` | The endpoint for the AI model processing. |
## 🔄 Execution Flow Detail

1. **Input Validation:** User code is captured and sent via Fetch API.
2. **Authentication:** Backend validates the request and attaches the `GITHUB_TOKEN`.
3. **AI Inference:** The Scaledown API processes the code based on strict system instructions.
4. **Latency Measurement:** The backend tracks the round-trip time (Runtime) in milliseconds.
5. **Categorized Display:** The UI parses the response and applies conditional formatting (Red/Green).
