import anvil.files
from anvil.files import data_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def cap_nhat_id_khachhang():
  user = anvil.users.get_user()
  if not user:
    return "Chưa đăng nhập"

  if user['id_khachhang'] is not None:
    return f"Đã có ID: {user['id_khachhang']}"  # Không thay đổi

  # Tạo ID mới duy nhất
  all_users = app_tables.users.search()
  id_list = [u['id_khachhang'] for u in all_users if u['id_khachhang'] is not None]
  new_id = max(id_list) + 1 if id_list else 1

  user['id_khachhang'] = new_id
  return f"ID khách hàng mới: {new_id}"

