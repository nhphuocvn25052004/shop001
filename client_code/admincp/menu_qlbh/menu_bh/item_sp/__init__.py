from ._anvil_designer import item_spTemplate
from anvil import *

class item_sp(item_spTemplate):
  def __init__(self, item=None, parent_form=None, **properties):
    self.init_components(**properties)
    self.item = item
    self.parent_form = parent_form

    self.link_item_sp.role = "sanpham_card"
    self.link_item_sp.set_event_handler("click", self.sp_duoc_click)

    if self.item:
      tensanpham = self.item['tensanpham']
      giasanpham = self.item['giasanpham']
      hinhanh = self.item['hinhanh']
    else:
      tensanpham = "Không tên"
      giasanpham = 0
      hinhanh = None

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

  def sp_duoc_click(self, **event_args):
    if self.parent_form:
      self.parent_form.them_vao_thanhtoan(self.item)
