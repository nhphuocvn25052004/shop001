from ._anvil_designer import add_danhmucTemplate
from anvil import *


class add_danhmuc(add_danhmucTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
