from fastapi import FastAPI

from app.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description="Backend API for Loan Prediction System",
        version="1.0.0",
        debug=settings.debug,
    )

    @app.get("/", tags=["Root"])
    def read_root():
        return {
            "app": settings.app_name,
            "status": "running",
            "environment": settings.environment,
        }

    @app.get("/health", tags=["Health"])
    def health_check():
        return {
            "status": "healthy",
            "environment": settings.environment,
        }

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )
