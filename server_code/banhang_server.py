import anvil.files
from anvil.files import data_files
import anvil.server
import anvil.users
from anvil.tables import app_tables
import requests

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
    return []

  if id_danhmuc:
    return list(app_tables.tbl_sanpham.search(
      id_khachhang=user,
      id_danhmuc=id_danhmuc
    ))

  return list(app_tables.tbl_sanpham.search(id_khachhang=user))

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

@anvil.server.callable
def tao_don_hang_moi(ten_donhang):
  return app_tables.tbl_donhang.add_row(
    ten_donhang=ten_donhang,
    ngaytao=datetime.now(),
    trangthai=False
  )

@anvil.server.callable
def cap_nhat_trang_thai_don(id_donhang):
  row = app_tables.tbl_donhang.get(id=id_donhang)
  if row:
    row['trangthai'] = True
    row.update()
    return "OK"
  return "Đơn không tồn tại"

@anvil.server.callable
def tai_file_google_sheets():
  url = "https://docs.google.com/spreadsheets/d/1GBbFYkL726AoNlju-kfIc5aRcVBNF8AF/export?format=csv"
  response = requests.get(url)

  if response.status_code == 200:
    # Tạo Media Object để trả về client
    return anvil.media.from_bytes(response.content, "sheet.csv")
  else:
    raise Exception("Tải file thất bại. Mã lỗi: " + str(response.status_code))