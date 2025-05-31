from nicegui import ui


def show_budget(container):
    with container:
        ui.label('Budget mensuel').classes('text-h5')

