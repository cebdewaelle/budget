from nicegui import ui
from nicegui.events import ClickEventArguments

# Tu peux importer tes pages si besoin
# from views.budget_view import page_budget
# from views.reports_view import page_reports
# from views.accounts_view import page_accounts

@ui.page('/page_layout')
def page_layout():
    dark = ui.dark_mode(value=True)

    # === HEADER ===
    with ui.header(elevated=True).style('background-color: #1976d2; color: white').classes('items-center justify-between'):
        with ui.row():
            ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
            ui.label('BUDGET').classes('text-h6')
        with ui.row():
            ui.button('Dark', on_click=dark.toggle).props('flat color=white')

    # === DRAWER ===
    with ui.left_drawer(top_corner=False, bottom_corner=False).style('background-color: #90caf9') as left_drawer:
        ui.label('Navigation').classes('text-h6 text-white q-pa-sm')
        ui.separator()
        ui.link('Budget', '/page_budget').classes('text-white')
        ui.link('Reports', '/page_reports').classes('text-white')
        ui.link('Accounts', '/page_accounts').classes('text-white')

    # === CONTENT ===
    with ui.column().classes('q-pa-md'):
        ui.label('CONTENU DE LA PAGE').classes('text-h5')
        [ui.label(f'Ligne {i}') for i in range(1, 21)]  # Limité à 20 pour lisibilité

    # === FOOTER ===
    with ui.footer().style('background-color: #1976d2; color: white'):
        ui.label('FOOTER').classes('q-pa-sm')
