# Architecture

React/Vite renders the investigation workspace and calls FastAPI. The analysis service combines message patterns, context detection, claim extraction, URL structure checks, and a deterministic risk engine. Environment variables reserve an OpenAI-compatible provider integration point; no API key is committed.
