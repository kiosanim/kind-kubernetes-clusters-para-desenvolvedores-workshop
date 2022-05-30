import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app_environment import APP_ENVIRONMENT
from routes.random_prospects_routes import api_router

app = FastAPI()
origins = ["*"]
if APP_ENVIRONMENT.ENVIRONMENT is not None and APP_ENVIRONMENT.ENVIRONMENT.startswith("production"):
    app = FastAPI(docs_url=None, redoc_url=None)
else:
    app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=api_router)

if __name__ == '__main__':
    uvicorn.run("app:app", host="0.0.0.0", port=APP_ENVIRONMENT.PORT, reload=True, workers=1)
