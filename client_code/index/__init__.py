from ._anvil_designer import indexTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class index(indexTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.logged_in = False  # Mặc định chưa đăng nhập
    self.update_ui()

  def update_ui(self):
    if self.logged_in:
      self.dangxuat.text = "Đăng xuất"
      self.sanpham.visible = True
      self.banhang.visible = True
    else:
      self.dangxuat.text = "Đăng nhập"
      self.sanpham.visible = False
      self.banhang.visible = False

  def sanpham_click(self, **event_args):
    open_form('admincp.menu_qlsp.menu_sp')

  def dangxuat_click(self, **event_args):
    self.logged_in = not self.logged_in  # Đảo trạng thái
    self.update_ui()


  
