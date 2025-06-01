import os
from dotenv import load_dotenv
from nicegui import ui, app
from database import Base, engine
from utils.auth import protected_route, public_route
from views.auth_view import show_login, show_logout
from views.page_budget import show_budget
from views.page_reports import show_reports
from views.page_accounts import show_accounts
from views.user_view import show_dashboard
from router import Router

load_dotenv()

# Crée les tables
Base.metadata.create_all(bind=engine)

# Ajoute les fichiers statiques
app.add_static_files('/static', 'static')
ui.add_head_html('<link rel="stylesheet" href="/static/css/style.css">')

# Instanciation du router global
router = Router()

# Définir ici les pages protégées (qui nécessitent une connexion)
protected_routes = ['/dashboard', '/budget', '/reports', '/accounts']

@router.add('/')
def main_route():
    show_login()

@router.add('/budget')
@protected_route
def budget_route():
    show_budget()

@router.add('/reports')
@protected_route
def reports_route():
    show_reports()

@router.add('/accounts')
@protected_route
def accounts_route():
    show_accounts()

@router.add('/dashboard')
@protected_route
def dashboard_route():
    show_dashboard()

@router.add('/login')
def login_route():
    show_login()

@router.add('/logout')
def logout_route():
    show_logout()


@ui.page('/')
@ui.page('/{_:path}')  # Capturer toutes les autres routes
def show_main():
    dark = ui.dark_mode(value=True)

    with ui.header(elevated=True).style('background-color: #1976d2; color: white').classes('items-center justify-between'):
        with ui.row():
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            ui.label('Budget').classes('text-h6')
        with ui.row():
            ui.button('Dark', on_click=dark.toggle).props('flat color=white')
            if 'user_id' in app.storage.user:
                ui.button('Logout', on_click=lambda: router.open('/logout')).props('flat color=white')
            else:
                ui.button('Login', on_click=lambda: router.open('/')).props('flat color=white')

    with ui.left_drawer(top_corner=False, bottom_corner=False).style('background-color: #90caf9') as left_drawer:
        if 'user_id' in app.storage.user:
            ui.button('Budget', on_click=lambda: router.open('/budget')).classes('w-64')
            ui.button('Reports', on_click=lambda: router.open('/reports')).classes('w-64')
            ui.button('Accounts', on_click=lambda: router.open('/accounts')).classes('w-64')
            ui.button('Dashboard', on_click=lambda: router.open('/dashboard')).classes('w-64')

    # Frame de contenu dynamique (pages)
    with ui.column().classes('w-full'):
        with ui.element('div').classes('q-pa-md q-gutter-md fit'):
            router.frame().classes('w-full h-full')


# Démarrer l'application
storage_secret = os.getenv('STORAGE_SECRET')
ui.run(port=8081, storage_secret=storage_secret)
