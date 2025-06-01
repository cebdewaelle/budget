from nicegui import ui
from controllers import accounts_controller as ctrl
from datetime import date


def show_accounts():
    dark = ui.dark_mode(value=True)

    try:
        accounts = ctrl.get_all_accounts()
    except Exception as e:
        ui.notify(f'Erreur : {str(e)}', color='negative')
        return

    columns = [
        {'field': 'id', 'headerName': 'ID'},
        {'field': 'name', 'headerName': 'Nom', 'editable': True},
        {'field': 'balance', 'headerName': 'Solde', 'editable': True, 'type': 'numericColumn'},
        {'field': 'date_balance', 'headerName': 'Date du solde', 'editable': True},
        {'field': 'type_account', 'headerName': 'Type', 'editable': True},
        {'field': 'in_budget', 'headerName': 'Inclus dans le budget', 'editable': True},
    ]


    def refresh():
        aggrid.options['rowData'] = ctrl.get_all_accounts()
        aggrid.update()


    def add_account():
        try:
            new = ctrl.create_account({
                'name': 'Nouveau compte',
                'balance': 0.0,
                'date_balance': date.today(),
                'type_account': 'Courant',
                'in_budget': True
            })
            ui.notify(f'Compte créé: {new["name"]}')
            refresh()
        except Exception as err:
            ui.notify(f'Erreur: {err}', color='negative')


    async def on_edit(e):
        data = e.args['data']
        try:
            ctrl.update_account(data['id'], data)
            ui.notify('Compte mis à jour')
        except Exception as err:
            ui.notify(f'Erreur: {err}', color='negative')


    async def delete_selected():
        selected = await aggrid.get_selected_rows()
        for row in selected:
            try:
                ctrl.delete_account(row['id'])
            except Exception as err:
                ui.notify(f'Erreur: {err}', color='negative')
        refresh()
        ui.notify('Compte(s) supprimé(s)')


    aggrid = ui.aggrid({
        'columnDefs': columns,
        'rowData': accounts,
        'rowSelection': 'multiple',
        'stopEditingWhenCellsLoseFocus': True,
        'domLayout': 'autoHeight',
    }).on('cellValueChanged', on_edit).classes('ag-theme-balham-dark')


    ui.button('New account', on_click=add_account).props('color=primary')
    ui.button('Delete selection', on_click=delete_selected).props('color=negative')
