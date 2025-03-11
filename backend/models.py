from sqlalchemy import Column, String, Boolean
from database import Base

class URLMapping(Base):
    __tablename__ = "url_mappings"

    id = Column(String, primary_key=True, index=True)
    source_url = Column(String, nullable=False)
    safe_url = Column(String, nullable=False)
    real_url = Column(String, nullable=False)
    force_safe = Column(Boolean, default=False)

class User(Base):
    __tablename__ = "users"

    username = Column(String, primary_key=True, index=True)
    password = Column(String, nullable=False)  # Hashed in DB
    is_admin = Column(Boolean, default=False)