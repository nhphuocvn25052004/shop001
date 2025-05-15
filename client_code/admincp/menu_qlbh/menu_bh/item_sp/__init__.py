from ._anvil_designer import item_spTemplate
from anvil import *

class item_sp(item_spTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.item = properties

    self.label_tensp.text = self.item.get('tensanpham', 'Không tên')
    self.label_gia.text = f"{self.item.get('giasanpham', 0):,} VND"

    self.image_1.source = self.item.get('hinhanh') or 'blank_image.png'
    self.image_1.width = "80px"
    self.image_1.height = "80px"

    # Set width cố định để hiển thị như card
    self.width = "120px"
