import os
from dotenv import load_dotenv
from nicegui import ui, app
from database import Base, engine
from views.auth_view import show_login, logout

load_dotenv()

# Crée les tables
Base.metadata.create_all(bind=engine)

# Ajoute les fichiers statiques
app.add_static_files('/static', 'static')
ui.add_head_html('<link rel="stylesheet" href="/static/css/style.css">')


@ui.page('/')
def home():
    if 'user_id' in app.storage.user:
        ui.navigate.to('/dashboard')
    else:
        show_login()


@ui.page('/dashboard')
def dashboard():
    from views.user_view import user_aggrid_table  # Import local pour éviter les cycles

    if 'user_id' not in app.storage.user:
        ui.notify('Accès refusé, veuillez vous connecter')
        ui.navigate.to('/')
        return

    ui.label('Dashboard sécurisé').classes('text-h5 q-my-md')
    user_aggrid_table()  # Appel à ta nouvelle table
    ui.button('Se déconnecter', on_click=logout).classes('q-mt-md')


# Démarrer l'application
storage_secret = os.getenv('STORAGE_SECRET')
ui.run(port=8081, storage_secret=storage_secret)
