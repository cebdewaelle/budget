from nicegui import ui
from views.user_view import show_dashboard  # On suppose qu’il existe
from views.page_budget import show_budget


def main_layout():
    dark = ui.dark_mode(value=True)

    with ui.header(elevated=True).style('background-color: #1976d2; color: white').classes('items-center justify-between'):
        with ui.row():
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            ui.label('Budget').classes('text-h6')
        with ui.row():
            ui.button('Dark', on_click=dark.toggle).props('flat color=white')

    with ui.column().classes('q-pa-md fit') as content_container:
        ui.label('Bienvenue dans l’app Budget 👋').classes('text-h5')

    with ui.left_drawer(top_corner=False, bottom_corner=False).style('background-color: #90caf9') as left_drawer:
        ui.link('Dashboard', '').on('click', lambda _: load_content('dashboard'))
        ui.link('Budget', '').on('click', lambda _: load_content('budget'))
        ui.link('Reports', '').on('click', lambda _: load_content('reports'))
        ui.link('Accounts', '').on('click', lambda _: load_content('accounts'))

    with ui.footer().style('background-color: #1976d2; color: white'):
        ui.label('Footer')

    # ➤ Fonction de mise à jour du contenu
    def load_content(page: str):
        content_container.clear()
        if page == 'budget':
            ui.label('📊 Contenu de la page Budget').classes('text-h6')
        elif page == 'reports':
            ui.label('📈 Contenu des rapports').classes('text-h6')
        elif page == 'accounts':
            ui.label('💼 Contenu des comptes').classes('text-h6')

    load_content('dashboard')  # page d’accueil

    content_container = ui.column().classes('q-pa-md').style('min-height: 400px')

    def show_page(name: str):
        content_container.clear()
        if name == 'dashboard':
            with content_container:
                show_dashboard(content_container)
        elif name == 'budget':
            with content_container:
                show_budget(content_container)
        elif name == 'reports':
            with content_container:
                ui.label('Rapports à venir...').classes('text-h6')
        elif name == 'accounts':
            with content_container:
                ui.label('Comptes utilisateurs').classes('text-h6')



