from ._anvil_designer import item_spTemplate
from anvil import *

class item_sp(item_spTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.item = properties

    self.label_tensp.text = self.item.get('tensanpham', 'Không tên')
    self.label_gia.text = f"{self.item.get('giasanpham', 0):,} VND"

    # Hiển thị ảnh: nếu không có thì dùng ảnh mặc định
    self.image_1.source = self.item.get('hinhanh') or 'blank_image.png'

    # Tùy chỉnh hiển thị nhỏ gọn
    self.image_1.width = "60px"
    self.image_1.height = "60px"
    self.image_1.vertical_align = "middle"
