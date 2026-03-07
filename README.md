# Ebobot — Robot Psychology Hotline

An interactive art installation simulating a psychological crisis hotline — but the caller is a robot.

Gallery visitors play the role of a hotline operator while a voice chatbot impersonates distressed fictional robot characters (Terminator, Verter, Elektronik, and others).

## Quick Start

### Backend

```bash
cd backend
uv run uvicorn app.main:app --reload
```

API available at http://localhost:8000

### Frontend (development)

```bash
cd frontend
npm install
npm run dev
```

Dev server at http://localhost:5173 (proxies API to backend)

### Production

```bash
cd frontend && npm run build
cd ../backend && uv run uvicorn app.main:app
```

Everything served from http://localhost:8000
