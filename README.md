# MultiQuery Web App &nbsp;![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Status](https://img.shields.io/badge/Status-POC-orange)

**MultiQuery** is a prototype application designed to integrate multiple Large Language Model (LLM) providers, including ChatGPT, Grok, and Gemini. The project provides a unified interface for querying LLMs, storing and managing query history in a MongoDB database, and exporting results in various formats. This application serves as the foundation for building a unified context management system.

---

## **Features**

- **Query Multiple LLM Providers**: Send prompts to multiple providers simultaneously and retrieve results.
- **Concurrency**: Execute LLM queries efficiently using asynchronous operations.
- **Query History**: Store and retrieve query history from a MongoDB database.
- **Export Options**: Export query results in JSON or Markdown formats.
- **FastAPI Backend**: A scalable and modular backend architecture using FastAPI.
- **Pluggable LLM Providers**: Easily add or remove support for new providers.

---

## **Project Structure**

```
/Users/naderbaradar/development_workspace/multiquery_webapp
├── README.md
├── multiquery
│   ├── api
│   │   ├── __init__.py
│   │   └── endpoints
│   │       ├── __init__.py
│   │       ├── export.py
│   │       ├── history.py
│   │       └── query.py
│   ├── app.py
│   ├── config
│   │   └── config.yaml
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── services
│   │       ├── __init__.py
│   │       └── llm_service.py
│   ├── llm_providers
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── chatgpt.py
│   │   ├── gemini.py
│   │   └── grok.py
│   └── utils
│       ├── __init__.py
│       ├── config_loader.py
│       ├── json_exporter copy.py
│       ├── json_exporter.py
│       └── mongodb_client.py
└── output
```

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-username/multiquery.git
cd multiquery
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate   # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Configure the Application**
Update the `multiquery/config/config.yaml` file with your API keys and MongoDB configuration:
```yaml
database:
  uri: "mongodb://localhost:27017"
  name: "MultiQuery"
  collection: "result"
```

---

## **Usage**

### **1. Start the Backend**
**Preferred Method:**
Run with `uvicorn`
```bash
uvicorn multiquery.app:app --reload
```

Run the FastAPI application:
```bash
python multiquery/app.py
```

The backend will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

### **2. Test the Endpoints**
#### Query LLMs
Send a POST request to the `/query` endpoint:
```bash
curl -X POST "http://127.0.0.1:8000/query/" \
    -H "Content-Type: application/json" \
    -d '{"prompt": "What is the capital of France?"}'
```
#### Retrieve Query History
Fetch stored queries from the `/history` endpoint:
```bash
curl -X GET "http://127.0.0.1:8000/history/"
```

---

## **Export Options**

### Export to JSON
Save query results to MongoDB and optionally export to a JSON file using the `--export-json` flag.

### Export to Markdown
Use the `--export` flag to save query results as a Markdown file for sharing and documentation.

---

## **Future Enhancements**

- **Web UI**: Integrate a React-based frontend for a seamless user experience.
- **Authentication**: Add user authentication and provider-specific API key management.
- **Context Management**: Enable session-based contextual querying.
- **Dashboard**: Provide insights and analytics for LLM queries.

---
