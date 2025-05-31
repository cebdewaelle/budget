import os
from dotenv import load_dotenv
from nicegui import ui, app
from database import Base, engine
from views.auth_view import show_login, logout
from views.page_layout import main_layout


load_dotenv()

# Crée les tables
Base.metadata.create_all(bind=engine)

# Ajoute les fichiers statiques
app.add_static_files('/static', 'static')
ui.add_head_html('<link rel="stylesheet" href="/static/css/style.css">')


@ui.page('/')
def start():
    ui.navigate.to('/app')  # Redirection vers notre layout


@ui.page('/app')
def app_page():
    main_layout()  # Lance ton layout SPA ici


# Démarrer l'application
storage_secret = os.getenv('STORAGE_SECRET')
ui.run(port=8081, storage_secret=storage_secret)
