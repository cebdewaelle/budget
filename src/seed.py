from sqlalchemy import inspect
from database import SessionLocal, engine
from models.user import User, Base
from utils.security import hash_password
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def reset_user_table():
    """Supprime et recrée la table 'users' si elle contient déjà des données"""
    session = SessionLocal()
    try:
        user_count = session.query(User).count()
        if user_count > 0:
            logger.info(f"⚠ {user_count} utilisateur(s) trouvés. Suppression de la table 'users'...")
            User.__table__.drop(bind=engine)
            User.__table__.create(bind=engine)
            logger.info("✔ Table 'users' réinitialisée.")
        else:
            logger.info("ℹ La table 'users' est déjà vide.")
    finally:
        session.close()

def seed_users():
    """Ajoute des utilisateurs d'exemple"""
    session = SessionLocal()
    try:
        users = [
            User(firstname="Alice", lastname="Wonderland", email="alice@example.com", password=hash_password("test")),
            User(firstname="Bob", lastname="Sponge", email="bob@example.com", password=hash_password("test")),
            User(firstname="Charlie", lastname="Factory", email="charlie@example.com", password=hash_password("test")),
        ]
        session.add_all(users)
        session.commit()
        logger.info("✔ Nouveaux utilisateurs insérés.")
    finally:
        session.close()

def initialize_database():
    """Crée toutes les tables si elles n'existent pas"""
    Base.metadata.create_all(bind=engine)
    logger.info("✔ Tables créées (si elles n'existaient pas déjà).")

if __name__ == "__main__":
    initialize_database()
    reset_user_table()
    seed_users()
