#create db engin and session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.api.core.config import setting

engine=create_engine(setting.DATABASE_URL,
                    pool_pre_ping=True,
                    pool_size=10,
                    max_overflow=20,
                    )

sessionLocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()