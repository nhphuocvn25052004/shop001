from ._anvil_designer import indexTemplate
from anvil import *

class index(indexTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    # Ẩn nút SẢN PHẨM và BÁN HÀNG khi mở trang
    self.sanpham.visible = False
    self.banhang.visible = False
  def sanpham_click(self, **event_args):
    open_form('admincp.menu_qlsp.menu_sp')

  def dangnhap_click(self, **event_args):
    # Sau khi nhấn đăng nhập, hiển thị 2 nút chức năng
    self.sanpham.visible = True
    self.banhang.visible = True
    pass
