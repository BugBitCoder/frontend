from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import uploads, forms, reports, search, chatbot
import auth

app = FastAPI(title="E-Gov Accreditation Suite")

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(uploads.router, prefix="/uploads", tags=["uploads"])
app.include_router(forms.router, prefix="/forms", tags=["forms"])
app.include_router(reports.router, prefix="/reports", tags=["reports"])
app.include_router(search.router, prefix="/search", tags=["search"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["chatbot"])

@app.get("/health")
def health():
    return {"status": "ok"}
