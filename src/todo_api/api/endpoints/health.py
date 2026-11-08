"""Liveness is independent of the DB; readiness verifies the DB connection."""

from fastapi import APIRouter, HTTPException, Request
from pymongo.errors import PyMongoError

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("/live")
async def live() -> dict[str, str]:
    return {"status": "alive"}


@router.get("/ready")
async def ready(request: Request) -> dict[str, str]:
    try:
        await request.app.state.mongo_client.admin.command("ping")
    except PyMongoError as exc:
        raise HTTPException(status_code=503, detail="MongoDB unavailable") from exc
    return {"status": "ready"}
