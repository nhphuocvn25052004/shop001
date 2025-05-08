from ._anvil_designer import indexTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class index(indexTemplate):
  def __init__(self, logged_in=False, **properties):
    self.init_components(**properties)

  def sanpham_click(self, **event_args):
    open_form('admincp.menu_qlsp.menu_sp')

  def dangxuat_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  
