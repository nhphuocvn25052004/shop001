import anvil.server
from anvil.tables import app_tables
import anvil.tables.query as q
import anvil.users

@anvil.server.callable
def them_danh_muc(tendanhmuc):
  tendanhmuc = tendanhmuc.strip().lower()

  # Kiểm tra trùng tên
  ton_tai = app_tables.tbl_danhmuc.search(tendanhmuc=q.ilike(tendanhmuc))
  if any(ton_tai):
    return f"Tên danh mục '{tendanhmuc}' đã tồn tại."

  # Tạo id_danhmuc mới
  danh_sach = app_tables.tbl_danhmuc.search()
  id_list = [row['id_danhmuc'] for row in danh_sach if row['id_danhmuc'] is not None]
  new_id = max(id_list) + 1 if id_list else 1

  # Lấy người dùng hiện tại
  user = anvil.users.get_user()
  if not user:
    raise Exception("Chưa đăng nhập")

  # Thêm danh mục và gán liên kết đến user
  app_tables.tbl_danhmuc.add_row(
    id_danhmuc=new_id,
    tendanhmuc=tendanhmuc,
    id_khachhang=user
  )

  return f"Đã thêm danh mục: {tendanhmuc} (ID: {new_id})"

@anvil.server.callable
def lay_tat_ca_danh_muc():
  user = anvil.users.get_user()
  if not user:
    return []
  return app_tables.tbl_danhmuc.search(id_khachhang=user)

@anvil.server.callable
def xoa_danh_muc(id_danhmuc):
  row = app_tables.tbl_danhmuc.get(id_danhmuc=id_danhmuc)
  if row:
    row.delete()
    return True
  return False

@anvil.server.callable
def sua_danh_muc(id_danhmuc, ten_moi):
  row = app_tables.tbl_danhmuc.get(id_danhmuc=id_danhmuc)
  if row:
    row['tendanhmuc'] = ten_moi.strip().lower()
    return True
  return False
