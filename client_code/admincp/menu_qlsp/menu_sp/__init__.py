from ._anvil_designer import menu_spTemplate
from anvil import *
import anvil.server
from .hienthi import hienthi  # ✅ import đúng class

class menu_sp(menu_spTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.sanpham.item_template = lambda **props: hienthi(parent_form=self, **props)
    self.load_lai_sanpham()

  def load_lai_sanpham(self):
    ds_sanpham = anvil.server.call('lay_danh_sach_san_pham')
    self.sanpham.items = ds_sanpham

  def add_sp_click(self, **event_args):
    from . import add_sp
    popup = add_sp.add_sp()
    alert(popup, title="Thêm sản phẩm", large=True, buttons=[])

  def quanlydanhmuc_sp_click(self, **event_args):
    from . import add_danhmuc
    popup = add_danhmuc.add_danhmuc()
    alert(popup, title="Thêm danh mục", large=True, buttons=[])

  def home_click(self, **event_args):
    # Quay về form index với trạng thái đã đăng nhập
    open_form('index', logged_in=True)

  def dangxuat_click(self, **event_args):
    # Quay về form index với trạng thái đã đăng xuất
    open_form('index', logged_in=False)
