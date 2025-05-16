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
  if not user:
    return []

  # Không dùng user.get_id() vì cột id_khachhang là Link to row
  if id_danhmuc:
    return list(app_tables.tbl_sanpham.search(
      id_khachhang=user,         # Phải truyền object Row, không phải chuỗi
      id_danhmuc=id_danhmuc      # id_danhmuc cũng là Row nếu là Link
    ))
  else:
    return list(app_tables.tbl_sanpham.search(id_khachhang=user))




