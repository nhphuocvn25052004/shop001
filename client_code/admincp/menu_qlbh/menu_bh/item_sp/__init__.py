from ._anvil_designer import item_spTemplate
from anvil import *

class item_sp(item_spTemplate):
  def __init__(self, item=None, **properties):
    self.init_components(**properties)
    self.column_panel_1.role = "sanpham_card"
    self.item = item
    
    self.label_tensp.text = getattr(self.item, 'tensanpham', 'Không tên')
    self.label_gia.text = f"{getattr(self.item, 'giasanpham', 0):,} VND"

    # Nếu hinhanh rỗng/null thì gán ảnh mặc định
    self.image_1.source = getattr(self.item, 'hinhanh', '') or 'assets/blank_image.png'

    self.image_1.width = "60px"
    self.image_1.height = "60px"
    self.image_1.align = 'center'
    self.label_tensp.align = 'center'
    self.label_gia.align = 'center'
