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
    print(">>> Không có user")
    return []

  sp_user = list(app_tables.tbl_sanpham.search(id_khachhang=user))
  print(">>> Tổng sản phẩm theo user:", len(sp_user))
  for sp in sp_user:
    print("→ Sản phẩm:", sp['tensanpham'], "| Danh mục:", sp['id_danhmuc'], "| Khách hàng:", sp['id_khachhang'])

  return sp_user  # KHÔNG LỌC THEO DANH MỤC LÚC NÀY
@anvil.server.callable
def lay_sanpham_cuong_che():
  all_sp = list(app_tables.tbl_sanpham.search())
  print(">>> TỔNG SẢN PHẨM TOÀN BẢNG:", len(all_sp))
  for sp in all_sp:
    print("Tên:", sp['tensanpham'], "| DM:", sp['id_danhmuc'], "| User:", sp['id_khachhang'])
  return all_sp








