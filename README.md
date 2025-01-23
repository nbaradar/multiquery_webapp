# MultiQuery Web App &nbsp;![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![React](https://img.shields.io/badge/react-blue?&logo=react) ![Status](https://img.shields.io/badge/Status-Building-Red) 

**MultiQuery** is a prototype application (expansion of [Proof of Concept](https://github.com/nbaradar/multiquery_poc)) designed to integrate multiple Large Language Model (LLM) providers, including ChatGPT, Grok, and Gemini. The project provides a unified interface for querying LLMs, storing and managing query history in a MongoDB database, and exporting results in various formats. This application serves as the foundations of the MutliQuery/Context Store/User Interface SubSystems for building ContextCore.

---

## Features

### Frontend (React)
- **Dynamic Provider Selection**:
  - A dropdown menu allows users to toggle LLM providers (e.g., ChatGPT, Gemini, Grok).
- **Chat Management**:
  - A panel on the left lists chats, enabling easy navigation between different conversations.
- **Query Display**:
  - Displays the user query along with tags representing the selected LLM providers.
- **Result Window**:
  - Dynamically updates with cards showing results from each selected LLM provider.
- **Input Section**:
  - Contains a text input field for user queries, a dropdown to select providers, and a submit button.

### Backend (FastAPI)
- **Endpoint to Query Providers**:
  - `/query`: Accepts user prompts and dynamically calls the selected providers based on query parameters.
- **Dynamic Query Handling**:
  - Supports configurable parameters such as `llm_provider`, `temperature`, and more.
- **MongoDB Integration**:
  - Stores query results and chat history in a MongoDB database.
- **Error Handling**:
  - Handles API errors gracefully and logs them for debugging.

---

## Installation

### Prerequisites
- Node.js
- Python 3.8+
- MongoDB

### Frontend Setup
1. Navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

### Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Usage

1. Start the backend server at `http://127.0.0.1:8000`.
2. Start the frontend server at `http://localhost:3000`.
3. Open the app in your browser at `http://localhost:3000`.
4. Select LLM providers using the dropdown menu.
5. Enter a query and click **Submit**.
6. View the results from each provider displayed in the result window.

---

## API Endpoints

### POST `/query`
- **Description**: Sends the user query to the selected LLM providers and retrieves their responses.
- **Request Body**:
  ```json
  {
    "prompt": "Who are you?"
  }
  ```
- **Query Parameters**:
  - `llm_provider` (comma-separated list of providers, e.g., `ChatGPT,Gemini`)
  - `temperature` (optional, e.g., `0.7`)
- **Response**:
  ```json
  {
    "query": "Who are you?",
    "responses": {
      "ChatGPTProvider": "I am an AI language model...",
      "GeminiProvider": "I am a large language model...",
      "GrokProvider": "I am Grok, a chatbot created by xAI..."
    }
  }
  ```

---

## UI as of Jan 
![image](https://github.com/user-attachments/assets/7fbf72e7-0297-4ca1-aa07-82c146577367)

---

## Roadmap

### Upcoming Features
1. **Chat History**:
   - Save and reload previous conversations from the database.
2. **Advanced Query Configurations**:
   - Add support for more LLM parameters (e.g., max tokens, model selection).
3. **Enhanced UI**:
   - Refine the result card designs and improve responsiveness.
4. **Authentication**:
   - Allow users to log in and manage their preferences.
