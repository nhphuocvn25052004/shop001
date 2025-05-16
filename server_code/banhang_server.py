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

  if id_danhmuc:
    print(">>> LỌC THEO DANH MỤC:", id_danhmuc)
    ds = list(app_tables.tbl_sanpham.search(
      id_khachhang=user,
      id_danhmuc=id_danhmuc
    ))
    print(">>> SỐ SP TÌM ĐƯỢC:", len(ds))
    return ds

  # Nếu không lọc danh mục
  ds = list(app_tables.tbl_sanpham.search(id_khachhang=user))
  print(">>> LẤY TOÀN BỘ SP:", len(ds))
  return ds









