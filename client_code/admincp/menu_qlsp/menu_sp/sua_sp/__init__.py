from ._anvil_designer import sua_spTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class sua_sp(sua_spTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def file_loader_1_change(self, file, **event_args):
    """This method is called when a new file is loaded into this FileLoader"""
    pass

  def ten_sanpham_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def gia_sanpham_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def danhsach_danhmuc_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
