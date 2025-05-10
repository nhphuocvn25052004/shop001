from ._anvil_designer import hienthiTemplate
from anvil import *

class hienthi(hienthiTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    sp = self.item  # Mỗi item là 1 dòng từ bảng tbl_sanpham

    # Gán dữ liệu
    self.Label_ten.text = sp['tensanpham']
    self.Label_gia.text = f"{sp['giasanpham']} VND"

    # Hình ảnh nếu có
    self.Image_1.source = sp['hinhanh'] if sp['hinhanh'] else None
    self.Image_1.visible = bool(sp['hinhanh'])
