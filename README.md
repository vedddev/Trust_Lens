# TrustLens

**Know before you trust.** An explainable AI-ready investigation platform for suspicious messages, job offers, scholarship notices, social posts, and URLs.

## What it does

TrustLens combines deterministic social-engineering signals with contextual analysis to produce a calibrated risk score, evidence excerpts, extracted entities, unverified claims, recommended actions, confidence, and limitations. It supports English, Hindi, and Marathi detection architecture and avoids definitive accusations without reliable verification.

## Stack

React + Vite + Axios + Lucide React frontend; FastAPI + Pydantic backend; configurable OpenAI-compatible provider settings; pytest; JSON example datasets.

## Run locally

```bash
cd backend
python -m venv venv
venv\Scripts\pip install -r requirements.txt
venv\Scripts\uvicorn backend.main:app --reload --port 8000

cd ../frontend
npm install
npm run dev
```

Copy `.env.example` to `.env`; set `AI_API_KEY`, `AI_BASE_URL`, `AI_MODEL`, and `FRONTEND_URL` when enabling a provider. API routes: `GET /api/health`, `POST /api/analyze`, `POST /api/analyze-url`.

## Testing and evaluation

Run `pytest` after installing requirements. The small included demo dataset is under `data/examples`; benchmark results are deliberately not pre-filled. See [architecture](docs/architecture.md), [demo](docs/demo.md), and [AI disclosure](docs/ai_disclosure.md).
