from nicegui import ui
from database import SessionLocal
from models.user import User


def show_dashboard():

    dark = ui.dark_mode(value=True)
    session = SessionLocal()
    users = session.query(User).all()
    session.close()

    columns = [
        {'field': 'id', 'headerName': 'ID'},
        {'field': 'firstname', 'headerName': 'Prénom', 'editable': True},
        {'field': 'lastname', 'headerName': 'Nom', 'editable': True},
        {'field': 'email', 'headerName': 'Email', 'editable': True},
    ]

    rows = [
        {'id': u.id, 'firstname': u.firstname, 'lastname': u.lastname, 'email': u.email}
        for u in users
    ]

    def add_row():
        new_id = max((r['id'] for r in rows), default=0) + 1
        rows.append({'id': new_id, 'firstname': 'Nouveau', 'lastname': 'Nom', 'email': 'nouveau@exemple.com'})
        ui.notify(f'Ajouté utilisateur ID {new_id}')
        aggrid.update()

    def handle_cell_value_change(e):
        updated = e.args['data']
        session = SessionLocal()
        user = session.query(User).get(updated['id'])
        if user:
            user.firstname = updated['firstname']
            user.lastname = updated['lastname']
            user.email = updated['email']
            session.commit()
        session.close()

        for i, r in enumerate(rows):
            if r['id'] == updated['id']:
                rows[i] = updated
                break

        ui.notify(f'Modifié: {updated}')

    async def delete_selected():
        selected = await aggrid.get_selected_rows()
        ids = [row['id'] for row in selected]

        session = SessionLocal()
        for id_ in ids:
            user = session.query(User).get(id_)
            if user:
                session.delete(user)
        session.commit()
        session.close()

        rows[:] = [r for r in rows if r['id'] not in ids]
        aggrid.update()
        ui.notify(f'Supprimé(s): {ids}')

    aggrid = ui.aggrid({
        'columnDefs': columns,
        'rowData': rows,
        'rowSelection': 'multiple',
        'stopEditingWhenCellsLoseFocus': True,
    }).on('cellValueChanged', handle_cell_value_change).classes('ag-theme-balham-dark')

    ui.button('Supprimer sélection', on_click=delete_selected)
    ui.button('Nouvel utilisateur', on_click=add_row)
