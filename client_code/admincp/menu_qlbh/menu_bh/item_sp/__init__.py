from ._anvil_designer import item_spTemplate
from anvil import *

class item_sp(item_spTemplate):
  def __init__(self, item=None, **properties):
    self.init_components(**properties)
    self.column_item_sp.role = "sanpham_card"
    self.item = item

    if self.item:
      # Sử dụng cú pháp [‘field_name’] thay vì .get() hay .tensanpham
      tensanpham = self.item['tensanpham'] 
      giasanpham = self.item['giasanpham'] 
      hinhanh = self.item['hinhanh']
    else:
      tensanpham = 'Không tên'
      giasanpham = 0
      hinhanh = 'assets/blank_image.png'

    self.label_tensp.text = tensanpham
    try:
      self.label_gia.text = f"{int(giasanpham):,} VND"
    except:
      self.label_gia.text = "0 VND"

    self.image_1.source = hinhanh

    self.image_1.width = "60px"
    self.image_1.height = "60px"
    self.image_1.align = 'center'
    self.label_tensp.align = 'center'
    self.label_gia.align = 'center'

    self.column_item_sp.set_event_handler("click",self.sp_duoc_click )

  def sp_duoc_click(self, **event_args):
    # Ví dụ: hiển thị tên sản phẩm
    alert(f"Bạn đã chọn: {self.item['tensanpham']}", title="Chi tiết")