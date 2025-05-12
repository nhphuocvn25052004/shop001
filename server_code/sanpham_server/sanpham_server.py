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
  san_pham_list = app_tables.tbl_sanpham.search()
  max_id = 0

  for sp in san_pham_list:
    try:
      max_id = max(max_id, int(sp['id_sanpham']))
    except:
      continue  # Bỏ qua nếu id_sanpham không hợp lệ

  new_id = max_id + 1  # ✅ new_id là số, phù hợp với cột kiểu Number

  new_row = app_tables.tbl_sanpham.add_row(
    id_sanpham=new_id,
    tensanpham=ten_sp,
    giasanpham=gia_sp,
    id_danhmuc=danh_muc,
    hinhanh=hinh_anh
  )

  return f"Đã thêm sản phẩm: {ten_sp} (ID: {new_id})"


@anvil.server.callable
def cap_nhat_san_pham(id_sanpham, ten_sp, gia_sp, hinh_anh=None):
  rows = app_tables.tbl_sanpham.search(id_sanpham=id_sanpham)
  row = rows[0] if len(rows) > 0 else None

  if row:
    row['tensanpham'] = ten_sp
    row['giasanpham'] = gia_sp
    if hinh_anh:
      row['hinhanh'] = hinh_anh
    return True
  return False
@anvil.server.callable
def xoa_san_pham(id_sp):
  row = app_tables.tbl_sanpham.get(id_sanpham=id_sp)
  if row:
    row.delete()
    return True
  return False