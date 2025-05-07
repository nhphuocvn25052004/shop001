from ._anvil_designer import indexTemplate
from anvil import *

class index(indexTemplate):
  def __init__(self, logged_in=False, **properties):
    self.init_components(**properties)

    # Hiện hoặc ẩn nút theo trạng thái đăng nhập
    self.sanpham.visible = logged_in
    self.banhang.visible = logged_in

  def sanpham_click(self, **event_args):
    open_form('admincp.menu_qlsp.menu_sp')

  def dangnhap_click(self, **event_args):
    # Mô phỏng đăng nhập thành công: mở lại index với logged_in=True
    open_form('index', logged_in=True)
