import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def lay_sanpham_nguoidung():
  user = anvil.users.get_user()
  if not user:
    return []

  # Lọc theo id_khachhang
  return list(app_tables.tbl_sanpham.search(id_khachhang=user))

