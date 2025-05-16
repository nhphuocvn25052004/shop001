from ._anvil_designer import item_spTemplate
from anvil import *

class item_sp(item_spTemplate):
  def __init__(self, item=None, **properties):
    self.init_components(**properties)
    self.column_panel_1.role = "sanpham_card"
    self.item = item

    if self.item:
      # Truy cập theo kiểu object thay vì .get()
      tensanpham = self.item.tensanpham if self.item.tensanpham else "Không tên"
      giasanpham = self.item.giasanpham if self.item.giasanpham else 0 
      hinhanh = self.item.hinhanh if self.item.hinhanh else 'assets/blank_image.png'
    else:
      tensanpham = 'Không tên'
      giasanpham = 0
      hinhanh = 'assets/blank_image.png'

    self.label_tensp.text = tensanpham
    self.label_gia.text = f"{int(giasanpham):,} VND"
    self.image_1.source = hinhanh

    self.image_1.width = "60px"
    self.image_1.height = "60px"
    self.image_1.align = 'center'
    self.label_tensp.align = 'center'
    self.label_gia.align = 'center'
