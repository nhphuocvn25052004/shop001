import anvil.server
from anvil.tables import app_tables

@anvil.server.callable
def lay_danh_sach_danh_muc():
  return list(app_tables.tbl_danhmuc.search())

@anvil.server.callable
def them_san_pham(ten_san_pham, gia_san_pham, danh_muc_row, hinh_anh=None):
  danh_sach = app_tables.tbl_sanpham.search()
  id_list = [row['id_sanpham'] for row in danh_sach if row['id_sanpham'] is not None]
  max_id = max(id_list) if id_list else 0
  new_id = max_id + 1

  app_tables.tbl_sanpham.add_row(
    id_sanpham=new_id,
    tensanpham=ten_san_pham,
    giasanpham=gia_san_pham,
    id_danhmuc=danh_muc_row['id_danhmuc'],
    tendanhmuc=danh_muc_row['tendanhmuc'],
    hinhanh=hinh_anh
  )

  return f"Đã thêm sản phẩm: {ten_san_pham} (ID: {new_id})"
