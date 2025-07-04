from ._anvil_designer import sua_spTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q

from anvil.tables import app_tables
import anvil.server


class sua_sp(sua_spTemplate):
  def __init__(self, sanpham=None, parent_form=None, **properties):
    self.init_components(**properties)
    self.sanpham = sanpham
    self.parent_form = parent_form  # 👈 Lưu lại form cha để gọi load lại

    if self.sanpham:
      # Hiển thị dữ liệu lên các trường
      self.ten_sanpham.text = sanpham['tensanpham']
      self.gia_sanpham.text = sanpham['giasanpham']
      self.file_loader_1.url = sanpham['hinhanh'].url if sanpham['hinhanh'] else ""

  def chapnhan_click(self, **event_args):
    if not self.sanpham:
     Notification("Không tìm thấy sản phẩm để cập nhật!", style="danger").show()
     return

     try:
      gia_sp_number = float(self.gia_sanpham.text)
      kq = anvil.server.call(
        'cap_nhat_san_pham',
        id_sanpham=self.sanpham['id_sanpham'],
        ten_sp=self.ten_sanpham.text,
        gia_sp=gia_sp_number,
        hinh_anh=self.file_loader_1.file if self.file_loader_1.file else None
     )

      if kq:
       Notification("Cập nhật thành công!", style="success").show()
       if hasattr(self, 'parent_form') and self.parent_form:
          self.parent_form.load_lai_sanpham()
       self.raise_event("x-close-alert")

     except Exception as e:
      Notification(f"Lỗi: {e}", style="danger").show()

