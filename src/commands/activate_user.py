from app.models import User
from app.database import db_session

def run(user_email):
    user = db_session.query(User).filter_by(email=user_email).first()
    if user:
        user.is_active = True
        db_session.commit()
