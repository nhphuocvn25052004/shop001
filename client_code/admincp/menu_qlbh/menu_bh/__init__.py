from ._anvil_designer import menu_bhTemplate
from anvil import *
import anvil.server

class menu_bh(menu_bhTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_sp()

  def load_sp(self):
    ds_sp = anvil.server.call('lay_sanpham_nguoidung')
    self.repeating_panel_1.items = ds_sp
