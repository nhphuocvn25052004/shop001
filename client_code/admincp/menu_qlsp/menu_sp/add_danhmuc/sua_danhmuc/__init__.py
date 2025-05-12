from ._anvil_designer import sua_danhmucTemplate
from anvil import *
import anvil.server

class sua_danhmuc(sua_danhmucTemplate):
  def __init__(self, item=None, parent_form=None, **properties):
    self.init_components(**properties)
    self.item = item
    self.parent_form = parent_form

    # Hiển thị tên danh mục cũ
    self.text_box_1.text = item['tendanhmuc']

  def btl_luu_click(self, **event_args):
    ten_moi = self.text_box_1.text.strip()

    if not ten_moi:
      alert("Vui lòng nhập tên danh mục mới.")
      return

    success = anvil.server.call('sua_danh_muc', self.item['id_danhmuc'], ten_moi)
    if success:
      Notification("Đã cập nhật danh mục!", timeout=2).show()
      if self.parent_form:
        self.parent_form.load_data()
      self.raise_event("x-close-alert")
    else:
      alert("Cập nhật thất bại!")
    pass
