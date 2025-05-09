import anvil.server
from anvil.tables import app_tables
import anvil.tables.query as q  # ✅ Thêm dòng này để dùng q.ilike()

@anvil.server.callable
def them_danh_muc(tendanhmuc):
  # Chuẩn hóa chuỗi
  tendanhmuc = tendanhmuc.strip().lower()

  # Kiểm tra trùng tên
  ton_tai = app_tables.tbl_danhmuc.search(tendanhmuc=q.ilike(tendanhmuc))
  if any(ton_tai):
    return f"Tên danh mục '{tendanhmuc}' đã tồn tại."

  # Tự tăng ID
  danh_sach = app_tables.tbl_danhmuc.search()
  if danh_sach:
    max_id = max(row['id_danhmuc'] for row in danh_sach if row['id_danhmuc'] is not None)
  else:
    max_id = 0

  new_id = max_id + 1

  # Thêm mới
  app_tables.tbl_danhmuc.add_row(id_danhmuc=new_id, tendanhmuc=tendanhmuc)
  return f"Đã thêm danh mục: {tendanhmuc} (ID: {new_id})"
