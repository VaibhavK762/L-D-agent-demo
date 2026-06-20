# L&D AI Agent Demo

## Overview

This project is a simple Agentic AI prototype developed for Learning & Development (L&D) use cases.

The agent answers employee queries by selecting the appropriate knowledge source and using an LLM to generate context-aware responses. Unlike a traditional chatbot that relies only on model knowledge, this agent retrieves information from company-specific data sources before generating a response.

---
## Video



## Features

### Skills Knowledge Base

* Stores role-to-skill mappings in a CSV file.
* Answers questions related to required skills and learning paths.

Examples:

* What skills are required for a Data Analyst?
* How do I become an AI Engineer?

### Onboarding Knowledge Base

* Uses an onboarding guide document as a knowledge source.
* Answers questions related to onboarding, benefits, policies, training, and employee procedures.

Examples:

* What happens during the first 90 days?
* When will I receive my first salary?
* What benefits are available to employees?

### Agentic Workflow

The agent:

1. Receives a user query.
2. Determines the relevant knowledge source.
3. Retrieves information from the selected source.
4. Provides the retrieved context to the LLM.
5. Generates a contextualized response.



## Architecture

        ```text
        User Query
             |
             v
         L&D AI Agent
             |
             v
        Tool Selection
             |
 +-----------+-----------+
 |                       |
 v                       v
Skills DB         Onboarding Guide
 |                       |
 +-----------+-----------+
             |
             v
          Groq LLM
             |
             v
       Final Response
```

---

## Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.3 70B Versatile
* Pandas
* Python Dotenv

---

## Project Structure

```text
Ai_agents/
│
├── app.py
├── agent.py
├── workflow.py
├── tools.py
├── evaluator.py
├── requirements.txt
├── .env
│
└── knowledge/
    ├── skills.csv
    └── onboarding.txt
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/VaibhavK762/L-D-agent-demo.git
cd L-D-agent-demo
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

### Linux / WSL

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
streamlit run app.py
```

The application will be available locally at:

```text
http://localhost:8501
```

---

## Example Queries

### Skills Queries

```text
What skills are required for a Data Analyst?
```

```text
How do I become an AI Engineer?
```

### Onboarding Queries

```text
What happens during the first 90 days?
```

```text
What benefits are available to employees?
```

```text
When will I receive my first salary?
```

```text
Is safety induction mandatory?
```

---

## Current Limitations

* Tool selection is rule-based using keyword matching.
* Limited knowledge sources.
* No semantic search or vector database integration.
* Designed as a functional prototype rather than a production-ready system.

---

## Future Improvements

* LLM-based tool routing.
* Semantic search using embeddings.
* Vector database integration.
* Support for multiple company documents.
* Personalized learning recommendations.
* Workflow automation and task management.

---

## Learning Outcomes

This project demonstrates:

* Agentic AI concepts
* Tool usage and routing
* Knowledge retrieval
* Context-aware response generation
* Practical L&D AI applications
