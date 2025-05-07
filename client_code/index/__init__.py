from ._anvil_designer import indexTemplate
from anvil import *

class index(indexTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def sanpham_click(self, **event_args):
    open_form('admincp.menu_qlsp.menu_sp')