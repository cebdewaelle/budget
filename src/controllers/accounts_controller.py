from fastapi import HTTPException
from sqlalchemy.orm import Session
from nicegui import app
from database import SessionLocal
from models.account import Account
from datetime import date, datetime


def get_user_id() -> int:
    """Récupère l'ID de l'utilisateur connecté."""
    user_id = app.storage.user.get('user_id')
    if not user_id:
        raise HTTPException(status_code=401, detail="Utilisateur non connecté")
    return user_id


def get_all_accounts() -> list[dict]:
    """Récupère tous les comptes de l'utilisateur connecté."""
    user_id = get_user_id()
    db: Session = SessionLocal()
    accounts = db.query(Account).filter_by(user_id=user_id).all()
    db.close()
    return [account_to_dict(account) for account in accounts]


def get_account(account_id: int) -> dict | None:
    """Récupère un seul compte par ID (et vérifie qu'il appartient à l'utilisateur)."""
    user_id = get_user_id()
    db: Session = SessionLocal()
    account = db.query(Account).filter_by(id=account_id, user_id=user_id).first()
    db.close()
    if account:
        return account_to_dict(account)
    return None


def create_account(data: dict) -> dict:
    """Crée un nouveau compte pour l'utilisateur connecté."""
    user_id = get_user_id()
    db: Session = SessionLocal()
    account = Account(
        name=data.get('name', ''),
        balance=data.get('balance', 0.0),
        date_balance=date.today(),
        type_account=data.get('type_account', ''),
        in_budget=data.get('in_budget', True),
        user_id=user_id,
    )
    db.add(account)
    db.commit()
    db.refresh(account)
    db.close()
    return account_to_dict(account)


def update_account(account_id: int, data: dict) -> dict:
    session = SessionLocal()
    account = session.query(Account).filter_by(id=account_id, user_id=app.storage.user.get('user_id')).first()
    if not account:
        session.close()
        raise Exception('Compte non trouvé')

    account.name = data.get('name', account.name)
    account.balance = data.get('balance', account.balance)

    # ✅ Conversion sécurisée de la date
    raw_date = data.get('date_balance', account.date_balance)
    if isinstance(raw_date, str):
        try:
            account.date_balance = datetime.strptime(raw_date, '%Y-%m-%d').date()
        except ValueError:
            raise Exception('Format de date invalide. Attendu: YYYY-MM-DD')
    elif isinstance(raw_date, date):
        account.date_balance = raw_date

    account.type_account = data.get('type_account', account.type_account)
    account.in_budget = data.get('in_budget', account.in_budget)

    session.commit()
    result = {
        'id': account.id,
        'name': account.name,
        'balance': account.balance,
        'date_balance': account.date_balance.isoformat(),
        'type_account': account.type_account,
        'in_budget': account.in_budget
    }
    session.close()
    return result


def delete_account(account_id: int) -> bool:
    """Supprime un compte (si appartenant à l'utilisateur connecté)."""
    user_id = get_user_id()
    db: Session = SessionLocal()
    account = db.query(Account).filter_by(id=account_id, user_id=user_id).first()
    if not account:
        db.close()
        raise HTTPException(status_code=404, detail="Compte non trouvé")
    db.delete(account)
    db.commit()
    db.close()
    return True


def account_to_dict(account: Account) -> dict:
    """Convertit un objet SQLAlchemy Account en dictionnaire."""
    return {
        'id': account.id,
        'name': account.name,
        'balance': account.balance,
        'date_balance': account.date_balance.isoformat() if account.date_balance else None,
        'type_account': account.type_account,
        'in_budget': account.in_budget,
        'user_id': account.user_id,
    }
