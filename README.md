# Umoja Pamoja AI Arbitrator

> An AI-powered arbitration assistant designed for chama groups to resolve disputes fairly using the chama’s own bylaws, contribution records, and M-Pesa statements.

---

# Table of Contents

1. Problem Statement
2. Solution Overview
3. Key Features
4. Tech Stack
5. System Architecture
6. Agent Architecture
7. Data Pipelines
8. How the System Works
9. Example Use Cases
10. Project Structure
11. Local Setup
12. Deployment
13. API & Interaction
14. RAG Implementation
15. Multilingual Support
16. Data Handling Policy
17. AI Neutrality Policy
18. Challenges Solved
19. Future Improvements
20. Team Members
21. Screenshots & Demo
22. License
23. Acknowledgements

---

# 1. Problem Statement

Many chama groups face conflicts involving:

- Late contributions
- Missing payments
- Welfare fund claims
- Merry-go-round payouts
- Financial inconsistencies
- Penalty calculations

These disputes are usually handled manually through:
- WhatsApp chats
- Phone calls
- Spreadsheets
- PDFs
- M-Pesa statements

This often leads to:
- Emotional arguments
- Lack of transparency
- Bias accusations
- Poor record keeping
- Delayed resolutions

Most chama leaders do not have a centralized system that can:
- verify contributions,
- check rules,
- and make fair decisions quickly.

---

# 2. Solution Overview

Umoja Pamoja AI Arbitrator is an AI-powered dispute resolution assistant built for chama groups.

The system:
- Reads chama bylaws
- Understands disputes in English, Kiswahili, and Sheng
- Verifies M-Pesa transactions
- Checks contribution records
- Calculates fines
- Provides grounded rulings using the chama’s own constitution

The AI acts as a neutral digital mediator.

---

# 3. Key Features

## Core Features

- AI-powered arbitration
- Multilingual support
- Bylaw citation engine
- Financial verification
- Contribution tracking
- Fine calculation
- RAG-powered retrieval
- Structured + unstructured search
- Explainable AI decisions

---

## Supported Languages

- English
- Kiswahili
- Sheng

---

## AI Capabilities

The agent can:
- Retrieve bylaws
- Check transaction history
- Detect arrears
- Verify payout eligibility
- Explain penalties
- Provide evidence-backed decisions

---

# 4. Tech Stack

| Technology | Purpose |
|---|---|
| Gemini 3 Flash | Multilingual reasoning |
| Google AI Studio | Prompt engineering & testing |
| Vertex AI Agent Builder | Agent orchestration |
| ADK (Agent Development Kit) | Multi-agent workflow |
| Python | Backend logic |
| Antigravity | Workflow orchestration |
| Vertex AI Search | Vector retrieval |
| RAG | Knowledge grounding |
| Google Cloud Run | Deployment |
| Google Cloud Storage | Document storage |

---

# 5. System Architecture

## High-Level Architecture

```text
                   ┌─────────────────────┐
                   │     User Query      │
                   │ English/Kiswahili   │
                   │      / Sheng        │
                   └─────────┬───────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │  Gemini Arbitration AI  │
                │     Gemini 3 Flash      │
                └─────────┬───────────────┘
                          │
        ┌─────────────────┴─────────────────┐
        ▼                                   ▼

┌───────────────────┐           ┌────────────────────┐
│ Bylaw RAG Agent   │           │ Financial Records  │
│ (Unstructured)    │           │ Agent (Structured) │
└─────────┬─────────┘           └─────────┬──────────┘
          │                               │
          ▼                               ▼

┌───────────────────┐          ┌─────────────────────┐
│ Vertex AI Search  │          │ M-Pesa Statements   │
│ Vector Retrieval  │          │ Contribution Logs   │
└───────────────────┘          └─────────────────────┘
```

---

# 6. Agent Architecture

The system uses a multi-agent architecture built using ADK.

---

## 6.1 Arbitration Agent

### Responsibilities

- Understand disputes
- Detect language context
- Coordinate retrieval
- Generate rulings
- Explain decisions
- Cite bylaws

### Powered By

- Gemini 3 Flash
- Vertex AI Agent Builder

---

## 6.2 Bylaw RAG Agent

Handles unstructured documents.

### Responsibilities

- Retrieve relevant bylaws
- Semantic search
- Context grounding
- Section citation

### Data Sources

- PDF bylaws
- Constitution documents
- Rules documents

### Technologies

- RAG
- Vector embeddings
- Vertex AI Search

---

## 6.3 Financial Records Agent

Handles structured financial data.

### Responsibilities

- Verify contributions
- Query M-Pesa statements
- Calculate fines
- Check arrears
- Validate payout eligibility

### Data Sources

- Excel ledgers
- JSON transaction data
- CSV contribution records

---

# 7. Data Pipelines

---

## 7.1 Unstructured Data Pipeline

### Input

- PDF bylaws
- DOCX constitutions
- Rules documents

### Processing Flow

```text
PDF/DOCX
   ↓
Document Parsing
   ↓
Semantic Chunking
   ↓
Embedding Generation
   ↓
Vertex AI Search
```

### Why RAG?

RAG ensures the AI:
- retrieves exact rules,
- reduces hallucinations,
- and grounds decisions in evidence.

---

## 7.2 Structured Data Pipeline

### Input

- M-Pesa statements
- Contribution spreadsheets
- Transaction logs

### Processing Flow

```text
PDF/Excel
    ↓
Data Cleaning
    ↓
Normalization
    ↓
JSON/CSV Conversion
    ↓
Structured Datastore
```

### Example Normalized Transaction

```json
{
  "transaction_id": "SBR45TK9LM",
  "date": "2026-01-15T14:32:00Z",
  "member_phone": "254712345678",
  "member_name": "MAMA NJUGUNA",
  "amount": 1500.00,
  "type": "Contribution"
}
```

---

# 8. How the System Works

## Step-by-Step Workflow

### Step 1 — User Submits Dispute

Example:

> "Mama Njuguna alichelewa kulipa. Kuna fine?"

---

### Step 2 — Arbitration Agent Interprets Intent

The system:
- detects language,
- understands the dispute,
- identifies required data.

---

### Step 3 — Retrieval Agents Are Called

The AI calls:
- Bylaw RAG Agent
- Financial Records Agent

---

### Step 4 — Evidence Retrieval

The system retrieves:
- bylaws,
- transactions,
- contribution history.

---

### Step 5 — Gemini Generates Ruling

The response includes:
- decision,
- explanation,
- evidence,
- bylaw references.

---

# 9. Example Use Cases

---

## Example 1 — Late Contribution

### User

> "Mama Njuguna paid on May 7th instead of May 5th. Is there a penalty?"

### AI Response

> According to Section 5.1 of the Umoja Pamoja Chama bylaws, any member who fails to contribute by the 5th day incurs a KES 500 late fine.

---

## Example 2 — Suspended Member

### User

> "Can Baba Silas receive the merry-go-round payout if he has arrears?"

### AI Response

> No. Section 3.3 states that members with unpaid arrears are not eligible for payouts.

---

## Example 3 — Kiswahili Query

### User

> "Nilichelewa mchango. Fine ni ngapi?"

### AI Response

> Fine ya kuchelewa kuchanga ni KES 500 kulingana na Section 5.1 ya bylaws.

---

## Example 4 — Sheng Query

### User

> "Mbona nilinyimwa payout?"

### AI Response

> System imeonyesha kuna arrears kwa contributions zako. Section 3.3 inasema member mwenye arrears hawezi pata payout.

---

# 10. Project Structure

```text
├── app/
│   ├── agents/
│   │   ├── arbitration_agent.py
│   │   ├── bylaw_agent.py
│   │   └── finance_agent.py
│   │
│   ├── ingestion/
│   │   ├── chunking.py
│   │   ├── parser.py
│   │   └── normalization.py
│   │
│   ├── rag/
│   │   ├── embeddings.py
│   │   ├── retrieval.py
│   │   └── datastore.py
│   │
│   ├── routes/
│   │   └── api.py
│   │
│   └── utils/
│
├── data/
│   ├── bylaws/
│   ├── statements/
│   └── ledgers/
│
├── screenshots/
├── requirements.txt
├── README.md
└── app.py
```

---

# 11. Local Setup

## Prerequisites

Install:
- Python 3.11+
- Google Cloud SDK
- Virtualenv

---

## Clone Repository

```bash
git clone https://github.com/your-team/chama-ai-arbitrator.git

cd chama-ai-arbitrator
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create `.env`

```env
GOOGLE_PROJECT_ID=your-project-id
GOOGLE_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```

---

## Run Locally

```bash
python app.py
```

or

```bash
uvicorn main:app --reload
```

---

# 12. Deployment

## Google Cloud Deployment

### Cloud Run

```bash
gcloud run deploy chama-ai-arbitrator
```

---

## Google Cloud Services Used

- Cloud Run
- Cloud Storage
- Vertex AI
- Vertex AI Search
- Agent Builder

---

# 13. API & Interaction

## Web Interface

```text
https://your-deployed-app-url
```

---

## Example API Request

```json
{
  "query": "Mama Njuguna alichelewa kuchanga"
}
```

---

## Example API Response

```json
{
  "decision": "KES 500 fine",
  "evidence": "Section 5.1",
  "reasoning": "Late contribution after May 5th"
}
```

---

# 14. RAG Implementation

## Why We Used RAG

Without RAG:
- AI may hallucinate rules
- Responses become unreliable

With RAG:
- Responses are grounded
- Rules are retrievable
- Citations are explainable

---

## Chunking Strategy

We used:
- semantic chunking,
- section-based chunking,
- overlapping retrieval windows.

This prevents:
- context mixing,
- legal ambiguity,
- incomplete citations.

---

# 15. Multilingual Support

The system supports:
- English
- Kiswahili
- Sheng

Gemini 3 Flash was selected because of:
- multilingual understanding,
- conversational flexibility,
- contextual reasoning.

---

# 16. Data Handling Policy

This system processes sensitive financial information.

## Data Protection Principles

We:
- avoid exposing raw statements,
- use secure cloud infrastructure,
- restrict unnecessary access,
- retrieve only relevant records.

---

## Sensitive Data Protection

Protected data includes:
- phone numbers,
- transactions,
- financial records,
- member contribution history.

---

# 17. AI Neutrality Policy

The arbitration system is strictly neutral.

The AI:
- does not take sides,
- does not infer emotions,
- does not manipulate outcomes.

All rulings are based strictly on:
- bylaws,
- financial records,
- and verifiable evidence.

The AI does not:
- promote political opinions,
- discriminate against members,
- override chama rules,
- fabricate evidence.

---

# 18. Challenges Solved

## Technical Challenges

- Multilingual interpretation
- Sheng understanding
- Financial verification
- Hallucination prevention
- Retrieval accuracy
- Hybrid search architecture

---

## Product Challenges

- Making AI decisions explainable
- Building user trust
- Designing for non-technical users
- Handling sensitive disputes responsibly

---

# 19. Future Improvements

- Real-time M-Pesa API integration
- WhatsApp chatbot
- Voice arbitration
- Fraud detection
- Analytics dashboard
- Multi-chama support
- Mobile application
- Member authentication

---

# 20. Team Members

| Name | Role |
|---|---|
| [Victor, Susan] | AI/ML Engineer |
| [Steve] | Backend Developer |
| [Susan, Steve, Victor] | Cloud Engineer |
| [Susan] | Documentation & UX Strategy |
| [Caleb, Lazarus] | Data Engineering |

---

# 21. Screenshots & Demo

## Demo Video

```text
_
```

---

## Screenshots

### Dashboard
_To be.._

### Arbitration Chat
_To be.._

### Retrieval Testing
_To be.._

---

# 22. License

MIT License

---

# 23. Acknowledgements

Built using:
- Google Cloud
- Gemini
- Vertex AI
- Google AI Studio
- ADK
- Antigravity

---

# Final Note

This project demonstrates how AI can strengthen trust, transparency, and accountability in community financial systems by combining multilingual AI, retrieval systems, and verifiable evidence-driven arbitration.
