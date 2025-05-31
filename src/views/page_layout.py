from nicegui import ui
from views.user_view import show_dashboard  # On suppose qu’il existe

def main_layout():
    dark = ui.dark_mode(value=True)

    with ui.header(elevated=True).style('background-color: #1976d2; color: white').classes('items-center justify-between'):
        with ui.row():
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            ui.label('Mon Appli').classes('text-h6')
        with ui.row():
            ui.button('Dark', on_click=dark.toggle).props('flat color=white')

    with ui.left_drawer(top_corner=False, bottom_corner=False).style('background-color: #90caf9') as left_drawer:
        ui.link('Dashboard', '').on('click', lambda _: show_page('dashboard'))
        ui.link('Budget', '').on('click', lambda _: show_page('budget'))
        ui.link('Reports', '').on('click', lambda _: show_page('reports'))
        ui.link('Accounts', '').on('click', lambda _: show_page('accounts'))

    content_container = ui.column().classes('q-pa-md').style('min-height: 400px')

    with ui.footer().style('background-color: #1976d2; color: white'):
        ui.label('Footer')

    def show_page(name: str):
        content_container.clear()
        if name == 'dashboard':
            show_dashboard(content_container)
        elif name == 'budget':
            show_budget(content_container)
        elif name == 'reports':
            with content_container:
                ui.label('Rapports à venir...').classes('text-h6')
        elif name == 'accounts':
            with content_container:
                ui.label('Comptes utilisateurs').classes('text-h6')

    show_page('dashboard')  # page d’accueil
