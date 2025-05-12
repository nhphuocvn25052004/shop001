import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def cap_nhat_id_khachhang():
  users = app_tables.users.search()
  id_list = [u['id_khachhang'] for u in users if u['id_khachhang'] is not None]
  new_id = max(id_list) + 1 if id_list else 1

  user = anvil.users.get_user()
  if user:
    user['id_khachhang'] = new_id
    return f"ID khách hàng mới: {new_id}"
  else:
    return "Chưa đăng nhập"

