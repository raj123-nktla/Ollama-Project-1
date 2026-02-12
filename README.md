# Ollama-Project-1
Here is a **350-character description**:  Offline AI-powered Cold Outreach Generator built with Streamlit, FastAPI, and Ollama. The system uses a local LLM to generate personalized cold emails and LinkedIn DMs from prospect profile text. It ensures privacy by running fully offline and focuses on intelligent, human-like messages.
# 🚀 Offline LLM-Powered Hyper-Personalized Cold Outreach Engine

An AI-powered cold outreach system built using **Ollama (local LLM)** that generates hyper-personalized emails without relying on external APIs.

This project runs completely offline and enables scalable, privacy-focused outreach generation for recruiters, founders, and sales teams.

---

## 📌 Problem Statement

Cold emails often:
- Sound generic
- Lack personalization
- Depend on paid API services
- Compromise data privacy

This project solves these problems using a **locally hosted LLM via Ollama** to generate high-quality personalized outreach messages.

---

## 🧠 Features

- ✅ Runs fully offline using Ollama
- ✅ Hyper-personalized email generation
- ✅ Context-aware prompt engineering
- ✅ Bulk outreach generation support
- ✅ Privacy-first architecture
- ✅ No OpenAI API required

---

## 🛠 Tech Stack

- Python: Streamlit UI 
- Ollama (Local LLM)
- FastAPI(Backend API)
- Ollama: Mistral model

---

## ⚙️ How It Works

1. User inputs:
   - Target name
   - Company
   - Role
   - Context / LinkedIn summary

2. Backend constructs a structured prompt.

3. Ollama processes the prompt locally using a selected model (e.g., Mistral / Llama3).

4. Personalized outreach email is generated.

5. Output is returned via REST API.

---

## 🏗 Architecture

User Input → Flask Backend → Prompt Builder → Ollama (Local LLM) → Generated Email → Response

---

## 🚀 Installation & Setup

### 1️⃣ Install Ollama
Download from:
https://ollama.com

Pull a model:
