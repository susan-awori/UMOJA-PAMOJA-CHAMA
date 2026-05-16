# Umoja Pamoja AI Arbitrator

An AI-powered arbitration assistant built for chama groups to resolve disputes fairly using the chama’s own bylaws, contribution records, and M-Pesa statements.

---

## Problem We Are Solving

Many chama groups experience disagreements about:

- Late contributions
- Merry-go-round payouts
- Missing payments
- Welfare claims
- Fine calculations
- Conflicting financial records

Most disputes become emotional because records are scattered across WhatsApp chats, PDFs, spreadsheets, and M-Pesa statements.

Our solution is an AI arbitration agent that acts like a neutral digital mediator.

Instead of relying on memory or arguments, the agent:
- Reads the chama bylaws
- Checks contribution records
- Verifies M-Pesa statements
- Explains decisions using the chama’s own rules
- Supports both Kiswahili and Sheng for natural conversations

### Example

> “Mama Njuguna paid on May 7th instead of May 5th. What happens?”

The agent checks the bylaws and responds with:
- the relevant section,
- the applicable fine,
- and the reasoning behind the decision.

This reduces conflict, improves transparency, and helps chama leaders make fair decisions quickly.

---

# Features

- AI-powered dispute mediation
- Retrieval-Augmented Generation (RAG)
- Supports:
  - English
  - Kiswahili
  - Sheng
- Bylaw citation engine
- M-Pesa transaction verification
- Contribution tracking
- Structured + unstructured data retrieval
- Cloud deployment with Google Cloud
- Built with Google AI ecosystem tools

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Google AI Studio | Gemini development/testing |
| Gemini 3 Flash | Multilingual reasoning |
| Vertex AI Agent Builder | Agent orchestration |
| ADK (Agent Development Kit) | Multi-agent architecture |
| Python | Backend logic |
| RAG | Context retrieval |
| Antigravity | Workflow orchestration |
| Google Cloud | Deployment & storage |

---

# Architecture Overview

## System Architecture

```text
                   ┌─────────────────────┐
                   │   User Query        │
                   │(English/Kiswahili)  │
                   └─────────┬───────────┘
                             │
                             ▼
                ┌─────────────────────────┐
                │  Gemini Arbitration AI  │
                │   (Gemini 3 Flash)      │
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
│ Vector Search     │          │ M-Pesa Statements   │
│ Vertex AI Search  │          │ Contribution Logs   │
└───────────────────┘          └─────────────────────┘
