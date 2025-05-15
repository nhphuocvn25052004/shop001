from ._anvil_designer import menu_bhTemplate
from anvil import *
import anvil.server
from .item_sp import item_sp

class menu_bh(menu_bhTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.flow_panel_sp.clear()
    self.flow_panel_danhmuc.clear()
    self.label_danhmuc.foreground = "white"
    
    self.load_danhmuc()
    self.load_sp()  # Mặc định load tất cả sản phẩm

  def load_danhmuc(self):
    ds_danhmuc = anvil.server.call('lay_danhmuc_nguoidung')
    for dm in ds_danhmuc:
      btn = Button(text=dm['tendanhmuc'], tag=dm, align='left')
      btn.set_event_handler('click', self.danhmuc_duoc_chon)
      self.flow_panel_danhmuc.add_component(btn)

  def load_sp(self, id_danhmuc=None):
    self.flow_panel_sp.clear()
    ds_sp = anvil.server.call('lay_sanpham_nguoidung', id_danhmuc)

    for sp in ds_sp:
      self.flow_panel_sp.add_component(item_sp(item=sp))

  def danhmuc_duoc_chon(self, sender, **event_args):
    danh_muc = sender.tag
    self.label_danhmuc.text = danh_muc['tendanhmuc']
    self.load_sp(danh_muc)
