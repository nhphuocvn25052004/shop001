import anvil.server
import anvil.users
from anvil.tables import app_tables

@anvil.server.callable
def lay_danhmuc_nguoidung():
  user = anvil.users.get_user()
  if not user:
    return []
  return list(app_tables.tbl_danhmuc.search(id_khachhang=user))


@anvil.server.callable
def lay_sanpham_nguoidung(id_danhmuc=None):
  user = anvil.users.get_user()
  print("User:", user)  # Thêm dòng này để debug
  if not user:
    return []

  if id_danhmuc:
    return list(app_tables.tbl_sanpham.search(id_khachhang=user, id_danhmuc=id_danhmuc))
  else:
    return list(app_tables.tbl_sanpham.search(id_khachhang=user))

