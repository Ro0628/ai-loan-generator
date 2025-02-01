
---
```go

```
---

ai-loan-generator/
│── src/                 # Business logic and models (optional)
│── app/                 # FastAPI application
│   ├── main.py          # Entry point for FastAPI
│   ├── routers/         # API route files (modular approach)
│   │   ├── loans.py
│   │   ├── users.py
│   ├── models/          # Pydantic models for request/response
│   │   ├── loan.py
│   ├── services/        # Business logic (optional)
│   │   ├── ai_agent.py  # AI model logic
│── tests/               # Unit tests
│── requirements.txt     # Dependencies
│── README.md            # Project description
│── .gitignore

