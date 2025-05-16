import anvil.server
import anvil.users
from anvil.tables import app_tables

# Lấy danh mục của người dùng
@anvil.server.callable
def lay_danhmuc_nguoidung():
  user = anvil.users.get_user()
  if not user:
    return []
  return list(app_tables.tbl_danhmuc.search(id_khachhang=user))

# Lấy sản phẩm theo người dùng và (nếu có) danh mục
@anvil.server.callable
def lay_sanpham_nguoidung(id_danhmuc=None):
  user = anvil.users.get_user()
  if not user:
    print(">>> Không có user")
    return []

  if id_danhmuc:
    print(">>> LỌC THEO DANH MỤC:", id_danhmuc)
    ds = list(app_tables.tbl_sanpham.search(
      id_khachhang=user,
      id_danhmuc=id_danhmuc
    ))
    print(">>> SỐ SP TÌM ĐƯỢC:", len(ds))
    return ds

  ds = list(app_tables.tbl_sanpham.search(id_khachhang=user))
  print(">>> LẤY TOÀN BỘ SP:", len(ds))
  return ds



# Thêm sản phẩm mới
@anvil.server.callable
def them_san_pham(ten_sp, gia_sp, danh_muc, hinh_anh):
  user = anvil.users.get_user()
  if not user:
    return "Không có người dùng!"

  app_tables.tbl_sanpham.add_row(
    tensanpham=ten_sp,
    giasanpham=gia_sp,
    id_danhmuc=danh_muc,
    hinhanh=hinh_anh,
    id_khachhang=user
  )
  return "Thêm sản phẩm thành công!"
