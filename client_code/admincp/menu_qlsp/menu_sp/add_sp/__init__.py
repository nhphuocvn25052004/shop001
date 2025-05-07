from ._anvil_designer import add_spTemplate
from anvil import *


class add_sp(add_spTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
