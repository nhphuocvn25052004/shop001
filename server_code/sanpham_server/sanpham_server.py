import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def lay_danh_sach_danh_muc():
  return list(app_tables.tbl_danhmuc.search())
@anvil.server.callable
def lay_danh_sach_san_pham():
  return list(app_tables.tbl_sanpham.search())
@anvil.server.callable
def them_san_pham(ten_sp, gia_sp, danh_muc, hinh_anh):
  # Thêm một dòng mới vào bảng sản phẩm
  new_row = app_tables.tbl_sanpham.add_row(
    tensanpham=ten_sp,
    giasanpham=gia_sp,
    id_danhmuc=danh_muc,  # Đây là một dòng từ tbl_danhmuc
    hinhanh=hinh_anh
  )

  return f"Đã thêm sản phẩm: {ten_sp} (ID: {new_row['id_sanpham']})"
