import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def them_danh_muc(tendanhmuc):
  # Lấy danh sách hiện có và tìm id lớn nhất
  danh_sach = app_tables.tbl_danhmuc.search()
  if danh_sach:
    max_id = max(row['id_danhmuc'] for row in danh_sach if row['id_danhmuc'] is not None)
  else:
    max_id = 0

  new_id = max_id + 1

  # Thêm dòng mới
  app_tables.tbl_danhmuc.add_row(id_danhmuc=new_id, tendanhmuc=tendanhmuc)
  return f"Đã thêm danh mục: {tendanhmuc} (ID: {new_id})"
