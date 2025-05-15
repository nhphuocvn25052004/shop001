from ._anvil_designer import item_spTemplate
from anvil import *

class item_sp(item_spTemplate):
  def __init__(self, item=None, **properties):  # ✅ nhận item
    self.init_components(**properties)

    self.item = item or {}  # anvil.Row object hoặc dict

    self.label_tensp.text = self.item['tensanpham'] if 'tensanpham' in self.item else 'Không tên'
    self.label_gia.text = f"{self.item['giasanpham']:,} VND" if 'giasanpham' in self.item else "0 VND"
    self.image_1.source = self.item['hinhanh'] if 'hinhanh' in self.item and self.item['hinhanh'] else 'blank_image.png'

    self.image_1.width = "80px"
    self.image_1.height = "80px"
    self.width = "120px"
