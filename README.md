# 🚀 AI Code Reviewer Agent

A high-performance code analysis tool that leverages **GPT-4o (via Scaledown API)** to provide instant feedback on code logic, performance, and potential bugs.

---

## 🏗️ System Architecture & Data Flow

Below is the stable ASCII architecture of how the Agent processes your code:

```text
       ┌──────────────┐         ┌────────────────┐         ┌──────────────────┐
       │   Frontend   │  POST   │  FastAPI       │  Auth   │  Scaledown AI    │
       │  (Port 8080) ├────────▶│  Backend       ├────────▶│  (GPT-4o Model)  │
       │              │ /review │  (Port 8000)   │ Token   │                  │
       └──────┬───────┘         └───────┬────────┘         └────────┬─────────┘
              │                         │                           │
              │      JSON Response      │       Review Data         │
              └◀────────────────────────┴◀──────────────────────────┘
```
Below is the high-level architecture of how the Agent processes your code:

**[User]** ➔ 💻 **Frontend** (Port 8080) ➔ 🔌 **FastAPI Backend** (Port 8000) ➔ 🤖 **Scaledown AI**

* **Client Side:** A clean UI captures code and handles asynchronous requests to the server.
* **Server Side:** FastAPI manages security headers, measures API latency (Runtime), and communicates with AI.
* **AI Engine:** Uses Scaledown's optimized endpoints to generate exactly 3 high-impact suggestions.
* **Feedback Loop:** Results are parsed and rendered with color-coded logic (Red for Errors, Green for Tips).

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | FastAPI (Python) |
| **Frontend** | Vanilla JavaScript, HTML5, CSS3 |
| **AI Model** | GPT-4o via Scaledown API |
| **Environment** | Python `http.server` & `uvicorn` |

---

## 🚀 Step-by-Step Installation

### 1. Setup Backend
1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```
2.  Install the necessary libraries:
    ```bash
    pip install -r requirements.txt
    ```
3.  Add your credentials to a `.env` file:
    ```text
    GITHUB_TOKEN=your_token_here
    SCALEDOWN_API_URL=https://api.scaledown.ai/v1
    ```
4.  Run the server:
    ```bash
    python -m uvicorn main:app --reload
    ```

### 2. Setup Frontend
1.  Open a new terminal and enter the frontend directory:
    ```bash
    cd frontend
    ```
2.  Start the local server:
    ```bash
    python -m http.server 8080
    ```
3.  Access the tool at: `http://localhost:8080`

---

## ✨ Key Features
* ⚡ **Performance Metrics:** Real-time runtime tracking for every review.
* ❌ **Smart Bug Detection:** Visual alerts for syntax and logical errors.
* ✅ **Optimized Tips:** 3 expert-level suggestions per review to improve code quality.

---

## 📂 Project Structure
* `backend/`: FastAPI logic and AI integration.
* `frontend/`: User interface and API client logic.
* `docs/`: Technical documentation and design deep-dives.
* `.gitignore`: Prevents sensitive `.env` files from being public.
