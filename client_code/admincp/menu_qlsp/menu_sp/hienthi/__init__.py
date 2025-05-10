from ._anvil_designer import hienthiTemplate
from anvil import *

class hienthi(hienthiTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    sp = self.item  # Mỗi item là 1 dòng từ bảng tbl_sanpham

    self.label_ten.text = sp['tensanpham']
    self.label_gia.text = f"{sp['giasanpham']} VND"
    self.image_1.source = sp['hinhanh'] if sp['hinhanh'] else None
