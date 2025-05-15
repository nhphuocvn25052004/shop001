from ._anvil_designer import menu_bhTemplate
from anvil import *
import anvil.server
from .item_sp import item_sp

class menu_bh(menu_bhTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.load_sp()
    self.label_danhmuc.text = getattr(self.item, 'tendanhmuc', 'Không tên')
    
  def load_sp(self):
    ds_sp = anvil.server.call('lay_sanpham_nguoidung')
    self.flow_panel_sp.clear()

    for sp in ds_sp:
      sp_form = item_sp(item=sp)  # ✅ truyền sp qua key 'item'
      self.flow_panel_sp.add_component(sp_form)
