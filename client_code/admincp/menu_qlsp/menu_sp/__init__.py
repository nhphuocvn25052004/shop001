from ._anvil_designer import menu_spTemplate
from anvil import *

class menu_sp(menu_spTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def add_sp_click(self, **event_args):
    # Mở popup thêm sản phẩm
    from . import add_sp  # Import module add_sp từ cùng thư mục
    popup = add_sp.add_sp()  # Tạo instance từ class add_sp
    alert(popup, title="Thêm sản phẩm", large=True, buttons=[])
    pass

  def quanlydanhmuc_sp_click(self, **event_args):
    from . import add_danhmuc
    popup = add_danhmuc.add_danhmuc()
    alert(popup,title="thêm danh mục", large=True, buttons=[])
    pass

  def home_click(self, **event_args):
    open_form('index')
    pass
