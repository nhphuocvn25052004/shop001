from ._anvil_designer import sua_spTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class sua_sp(sua_spTemplate):
  def __init__(self, sanpham=None, **properties):
    self.init_components(**properties)

    self.sanpham = sanpham  # Gán sản phẩm được truyền vào

    if self.sanpham:
      # Hiển thị dữ liệu lên các trường
      self.ten_sanpham.text = sanpham['tensanpham']
      self.gia_sanpham.text = sanpham['giasanpham']
      self.file_loader_1.url = sanpham['hinhanh'].url if sanpham['hinhanh'] else ""

  def chapnhan_click(self, **event_args):
    self.sanpham['tensanpham'] = self.ten_sanpham.text
    self.sanpham['giasanpham'] = self.gia_sanpham.text

    if self.file_loader_1.file:  # Nếu người dùng chọn file mới
      self.sanpham['hinhanh'] = self.file_loader_1.file

      Notification("Cập nhật thành công!", style="success").show()
    pass
