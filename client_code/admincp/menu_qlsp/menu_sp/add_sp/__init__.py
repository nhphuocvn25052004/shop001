from ._anvil_designer import add_spTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users


class add_sp(add_spTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def danhsach_danhmuc_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def gia_sanpham_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def ten_sanpham_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass
