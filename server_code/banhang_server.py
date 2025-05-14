import anvil.server
import anvil.users
from anvil.tables import app_tables

@anvil.server.callable
def lay_sanpham_nguoidung():
  user = anvil.users.get_user()
  if not user:
    return []
  return list(app_tables.tbl_sanpham.search(id_khachhang=user))
