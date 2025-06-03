from nicegui import ui, app
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from utils.security import verify_password
from utils.auth import public_route

@public_route
def show_login():
    ui.label('Connexion').classes('text-h4 q-my-md')

    email = ui.input('Email').props('outlined').classes('q-mb-md')
    password = ui.input('Mot de passe', password=True).props('outlined').classes('q-mb-md')

    def login_action():
        session: Session = SessionLocal()
        user = session.query(User).filter_by(email=email.value).first()
        if user and verify_password(user.password, password.value):
            # Enregistrement de l'id user dans la session
            app.storage.user['user_id'] = user.id
            ui.notify(f'Bienvenue, {user.firstname} {user.lastname} !')
            ui.navigate.to('/accounts')
        else:
            ui.notify('Identifiants incorrects', color='negative')
        session.close()

    ui.button('Se connecter', on_click=login_action).classes('q-mt-md')


def show_logout():
    # Supprime les données de session
    app.storage.user.clear()

    # Supprime le cookie côté client avec JavaScript
    ui.run_javascript("document.cookie = 'nicegui_user=; Max-Age=0; path=/'")

    ui.notify('Déconnecté avec succès')
    ui.navigate.to('/')
