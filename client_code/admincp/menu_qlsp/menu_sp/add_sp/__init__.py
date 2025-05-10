from ._anvil_designer import add_spTemplate
from anvil import *
import anvil.server

class add_sp(add_spTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.tai_danh_sach_danh_muc()

  def tai_danh_sach_danh_muc(self):
    ds = anvil.server.call('lay_danh_sach_danh_muc')
    self.danhsach_danhmuc.items = [(row['tendanhmuc'], row) for row in ds]

  def chapnhan_click(self, **event_args):
    ten_sp = self.ten_sanpham.text
    gia_sp = self.gia_sanpham.text
    danh_muc = self.danhsach_danhmuc.selected_value
    hinh_anh = self.file_loader_1.file  # Nếu có ảnh

    if not ten_sp or not gia_sp or not danh_muc:
      alert("Vui lòng nhập đầy đủ thông tin!", title="Thiếu thông tin")
      return

    try:
      kq = anvil.server.call('them_san_pham', ten_sp, gia_sp, danh_muc, hinh_anh)
      alert(kq, title="Thành công")
      self.ten_sanpham.text = ""
      self.gia_sanpham.text = ""
      self.danhsach_danhmuc.selected_value = None
      self.file_loader_1.clear()
    except Exception as e:
      alert(f"Lỗi: {e}", title="Lỗi")

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass
