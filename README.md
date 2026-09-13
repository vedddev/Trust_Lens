# 🔍 TrustLens

> **AI-powered scam detection that investigates suspicious messages, analyzes evidence, and explains the risk before you take action.**

TrustLens is an AI-powered scam investigation platform designed to help users identify potentially fraudulent emails, SMS messages, job offers, scholarship messages, banking alerts, delivery notifications, social media messages, and suspicious URLs.

Instead of simply returning **"SCAM" or "NOT SCAM"**, TrustLens combines traditional NLP, machine learning, LLM-based analysis, URL intelligence, and rule-based security signals to provide an **explainable risk assessment**.

---

## 🚨 Problem

Online scams are becoming increasingly convincing.

Attackers commonly use:

* Fake internship and job offers
* Fake bank/KYC alerts
* Scholarship scams
* Delivery/payment scams
* Fake investment opportunities
* Account verification messages
* OTP and credential requests
* Urgent payment requests
* Impersonation of companies or organizations

The problem is not just detecting a scam — users need to understand **why a message is suspicious and what they should do next**.

---

## 💡 Solution

TrustLens analyzes suspicious content through multiple layers:

```text
                  User Message / URL
                         │
                         ▼
                ┌─────────────────┐
                │  Text Processing │
                └────────┬────────┘
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Traditional ML           LLM Analysis
       TF-IDF + LR              NLP Reasoning
              │                     │
              └──────────┬──────────┘
                         ▼
                  URL Analysis
                         │
                         ▼
                 Security Signals
                         │
                         ▼
                   Risk Engine
                         │
                         ▼
              ┌────────────────────┐
              │  Risk Score 0–100  │
              └────────────────────┘
                         │
                         ▼
             Explanation + Evidence
                         │
                         ▼
                Recommendations
```

---

## ✨ Key Features

### 🧠 NLP & Machine Learning

TrustLens uses a traditional NLP classifier based on:

* TF-IDF vectorization
* Unigrams and bigrams
* Logistic Regression
* Scam probability prediction

The ML model provides a quantitative signal that is combined with other analysis layers.

### 🤖 LLM-Based Investigation

The LLM analyzes the meaning and context of the message to identify:

* Social engineering patterns
* Urgency and pressure tactics
* Payment requests
* OTP/password requests
* Impersonation
* Fake employment opportunities
* Financial manipulation
* Suspicious claims
* User intent
* Important entities

### 🌐 URL Analysis

When a URL is present, TrustLens examines security-related characteristics such as:

* Domain
* Subdomain
* TLD
* HTTPS usage
* URL length
* Suspicious characters
* IP-based hostnames
* Punycode
* Excessive subdomains
* Domain mismatches
* Redirect behavior

TrustLens does **not execute downloaded code or unsafe content**.

### ⚠️ Explainable Risk Score
The Risk Engine combines different signals and produces:

```text
Risk Score: 0–100

LOW       → Lower observed risk
MODERATE  → Some suspicious indicators
HIGH      → Multiple strong indicators
CRITICAL  → Strong evidence of potentially malicious behavior
```

The result includes the factors contributing to the score instead of hiding the reasoning behind a single prediction.

### 🔎 Investigation Results

TrustLens can provide:

* Risk score
* Risk level
* ML prediction
* ML probability
* Suspicious signals
* Evidence
* Extracted entities
* Claims
* URL findings
* Context/category
* Recommendations
* Confidence
* Limitations

---

## 🏗️ Tech Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### AI / ML

* NLP
* TF-IDF
* Logistic Regression
* LLM-based analysis
* Rule-based security analysis

### Security Analysis

* URL parsing
* Domain analysis
* Suspicious URL heuristics
* Security signal detection

---

## 📁 Project Structure

```text
TrustLens/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   ├── utils/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── package.json
│
├── backend/
│   ├── agents/
│   │   ├── message_analyzer.py
│   │   ├── url_analyzer.py
│   │   ├── claim_verifier.py
│   │   ├── context_analyzer.py
│   │   └── risk_engine.py
│   │
│   ├── api/
│   │   └── routes.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── logging_config.py
│   │
│   ├── models/
│   │   └── schemas.py
│   │
│   ├── services/
│   │   └── analysis_service.py
│   │
│   ├── ml/
│   │   ├── train_model.py
│   │   ├── predict.py
│   │   ├── vectorizer.pkl
│   │   └── scam_classifier.pkl
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── data/
│   └── examples/
│
├── evaluation/
│   ├── benchmark.py
│   └── results.md
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_risk_engine.py
│   └── test_api.py
│
├── docs/
│   ├── architecture.md
│   ├── ai_disclosure.md
│   └── demo.md
│
├── README.md
└── .gitignore
```

---

## 🔄 How TrustLens Works

### Step 1 — User Input

The user pastes a suspicious message or URL.

Example:

```text
Congratulations! You have been selected for a Google internship.
Pay ₹3,999 as a refundable verification fee to confirm your position.
Complete verification at:
https://example-suspicious-domain.com
```

### Step 2 — Traditional NLP Model

The text is converted into TF-IDF features.

```text
Message
   ↓
TF-IDF
   ↓
Logistic Regression
   ↓
Scam Probability
```

### Step 3 — LLM Analysis

The LLM analyzes the semantic meaning and identifies suspicious patterns such as:

* Fake recruitment claims
* Payment requests
* Urgency
* Impersonation
* Credential or financial requests

### Step 4 — URL Analysis

If a URL exists, TrustLens analyzes its structure and domain-related indicators.

### Step 5 — Risk Engine

The different signals are combined:

```text
ML Prediction
     +
LLM Analysis
     +
URL Signals
     +
Rule-Based Signals
     +
Context
     ↓
Risk Engine
     ↓
Final Risk Score
```

### Step 6 — Explainable Result

The user receives an investigation report rather than only a binary classification.

---

## 🧪 Example

### Input

```text
URGENT: Your bank account will be blocked today.
Verify your account immediately by entering your OTP and password:
https://suspicious-example.com
```

### TrustLens Output

```text
Risk Score: 96/100

Risk Level: CRITICAL

Suspicious Signals:
✓ Requests OTP
✓ Requests password
✓ Uses urgent language
✓ Threatens account suspension
✓ Contains suspicious URL

Recommendation:
Do not enter your credentials or OTP.
Contact your bank through its official website or app.
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd TrustLens
```

---

### 2. Backend Setup

```powershell
cd backend

python -m venv venv

.\venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

If PowerShell blocks virtual environment activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then:

```powershell
.\venv\Scripts\Activate.ps1
```

---

### 3. Configure Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
LLM_API_KEY=your_api_key_here
```

**Never commit your real API key to GitHub.**

The repository contains `.env.example` instead.

---

### 4. Start Backend

```powershell
uvicorn main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

### 5. Frontend Setup

Open another terminal:

```powershell
cd frontend

npm install

npm run dev
```

Open the URL shown by Vite, usually:

```text
http://localhost:5173
```

---

## 🔌 API Endpoints

### Health Check

```http
GET /api/health
```

Checks whether the backend is running.

### Analyze Message

```http
POST /api/analyze
```

Analyzes a suspicious message.

Example request:

```json
{
  "text": "Your account will be blocked. Verify your OTP immediately."
}
```

### Analyze URL

```http
POST /api/analyze-url
```

Analyzes a URL for suspicious structural and security indicators.

---

## 📊 Machine Learning

TrustLens uses a lightweight supervised NLP pipeline:

```text
Training Data
     ↓
Text Cleaning
     ↓
TF-IDF Vectorization
     ↓
Logistic Regression
     ↓
Scam Probability
```

### Why TF-IDF + Logistic Regression?

This approach was selected because it is:

* Fast to train
* Lightweight
* Easy to interpret
* Suitable for text classification
* Easy to deploy
* A strong baseline for NLP classification

The model is used as **one signal** in the overall TrustLens investigation rather than being treated as the only source of truth.

---

## 🧠 AI Architecture

TrustLens follows a multi-layer AI architecture:

```text
                  ┌───────────────┐
                  │ User Message  │
                  └───────┬───────┘
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
       Traditional NLP          LLM Analysis
       TF-IDF + LR              Semantic Analysis
              │                       │
              └───────────┬───────────┘
                          │
                          ▼
                    URL Analyzer
                          │
                          ▼
                   Context Analysis
                          │
                          ▼
                    Risk Engine
                          │
                          ▼
                  Explainable Report
```

---

## 🛡️ Safety & Limitations

TrustLens is an **assistive analysis tool**, not a definitive authority.

A high risk score does not automatically prove that a message is fraudulent, and a low score does not guarantee that a message is safe.

The system therefore provides:

* Evidence
* Suspicious signals
* Confidence
* Limitations
* Recommendations

Users should independently verify important communications through official channels.

For example, instead of clicking a link received through SMS, users should manually open the organization's official website or application.

---

## 🌍 Multilingual Support

TrustLens is designed to support multilingual scam analysis, including:

* English
* Hindi
* Marathi

This is important because scams frequently target users through regional languages and mixed-language communication.

---

## 🧪 Testing

Run backend tests with:

```powershell
pytest
```

The test suite covers important components such as:

* Message analysis
* Risk scoring
* API behavior
* Security signal detection

Build the frontend with:

```powershell
npm run build
```

---

## 📈 Evaluation

The traditional ML classifier can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-score

For a scam detection system, **precision and recall are especially important**, because both false positives and false negatives can negatively affect users.

The training/evaluation dataset should be clearly identified in the project documentation, and benchmark results should not be presented as real-world performance unless evaluated on an appropriate real-world dataset.

---

## 🔐 Privacy

TrustLens should not require users to expose sensitive credentials.

Never enter:

* Passwords
* OTPs
* Banking credentials
* API keys
* Private authentication tokens

into the application.

API keys are stored through environment variables and should never be committed to the repository.

---

## 🤖 AI Tools Disclosure

AI-assisted development tools were used during the development of TrustLens.

**Codex / AI coding assistance** was used for:

* Project scaffolding
* Code generation
* Debugging
* Refactoring
* Documentation
* Test generation
* Development assistance

Generated code was reviewed, tested, and modified during development.

TrustLens itself uses AI/ML technologies as part of its application pipeline, including:

* TF-IDF + Logistic Regression for traditional NLP classification
* LLM-based natural language analysis
* Semantic investigation
* Context analysis
* Explainable risk assessment

---

## 🚀 Future Scope

Potential future improvements include:

* Browser extension for real-time website analysis
* Email integration
* SMS analysis
* WhatsApp/Telegram message analysis
* More multilingual models
* Reputation databases
* Domain age and registration intelligence
* Phishing webpage detection
* Screenshot/image-based scam detection
* Voice scam detection
* Continuous model retraining
* Human feedback-based learning
* Enterprise security integrations

---

## 🎯 Hackathon Goal

TrustLens was built around a simple idea:

> **Before you trust the message, investigate it.**

Our goal is to make scam detection more understandable, transparent, and useful by combining **traditional NLP, machine learning, LLM reasoning, and security analysis** into one investigation platform.

---

## 👥 Team

**Vedant Shelake**
AI/ML • NLP • Backend • Full-Stack Development

---

## 📄 License

This project is developed as a hackathon project.

Add an appropriate open-source license if you intend to distribute the project publicly.

---

## ⭐ Acknowledgement

Built for **HyperBloom Hacks**.

If you find the project interesting, consider ⭐ starring the repository.
