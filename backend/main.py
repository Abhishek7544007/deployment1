from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend on Render:
origins = [
    "http://localhost:3000",
    "https://deployment1-frontend.onrender.com",
    "*",  # remove * in production
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Allowed origins
    allow_credentials=True,
    allow_methods=["*"],         # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],         # Authorization, Content-Type...
)
app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}
