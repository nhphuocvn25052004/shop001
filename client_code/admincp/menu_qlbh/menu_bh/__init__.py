from ._anvil_designer import menu_bhTemplate
from anvil import *
import anvil.server
from .item_sp import item_sp
from .item_thanhtoan import item_thanhtoan

class menu_bh(menu_bhTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
    sp_component = item_thanhtoan(parent_form=self)
    sp_component.item = sp
    sp_component.hien_item()
    self.column_thanhtoan.add_component(sp_component) 
    
    self.flow_panel_sp.clear()
    self.flow_panel_danhmuc.clear()
    self.label_danhmuc.foreground = "white"
    self.load_danhmuc()
    self.load_sp()  # Mặc định load tất cả sản phẩm
    self.ds_thanhtoan = []
    self.label_tongtien.text = "0 VND"
  
  def load_danhmuc(self):
    self.flow_panel_danhmuc.clear()

    # Nút "Tất cả"
    btn_all = Button(text="Tất cả", tag=None, align='left')
    btn_all.set_event_handler('click', self.danhmuc_duoc_chon)
    self.flow_panel_danhmuc.add_component(btn_all)

    # Các danh mục thật sự của người dùng
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
    if not ds_sp:
      self.flow_panel_sp.add_component(Label(text="Hết sản phẩm", align="center", bold=True, foreground="red"))
    return

  def danhmuc_duoc_chon(self, sender, **event_args):
    danh_muc = sender.tag
    if danh_muc is None:
      self.label_danhmuc.text = "Tất cả"
      self.load_sp()
    else:
      self.label_danhmuc.text = danh_muc['tendanhmuc']
      self.load_sp(danh_muc)
  
  def home_click(self, **event_args):
    open_form('index', logged_in=True)
    pass

  def dangxuat_click(self, **event_args):
    open_form('index', logged_in=False)
    pass


  def them_vao_thanhtoan(self, sp):
    self.ds_thanhtoan.append(sp)
    self.hien_thi_lai_thanhtoan()

def hien_thi_lai_thanhtoan(self):
  self.column_thanhtoan.clear()
  for item in self.ds_thanhtoan:
    self.column_thanhtoan.add_component(
      item_thanhtoan(item=item, parent_form=self)
    )

def xoa_khoi_thanhtoan(self, sp):
  self.ds_thanhtoan = [i for i in self.ds_thanhtoan if i != sp]
  self.hien_thi_lai_thanhtoan()

def cap_nhat_tong_tien(self):
  tong = 0
  for comp in self.column_thanhtoan.get_components():
    try:
      tong += int(comp.item['giasanpham']) * comp.so_luong
    except:
      continue
  self.label_tongtien.text = f"{tong:,} VND"

def them_vao_thanhtoan(self, sp):
  self.ds_thanhtoan.append(sp)
  self.hien_thi_lai_thanhtoan()

  def hien_thi_lai_thanhtoan(self):
    self.column_thanhtoan.clear()
    for item in self.ds_thanhtoan:
      self.column_thanhtoan.add_component(
        item_thanhtoan(item=item, parent_form=self)
      )

def xoa_khoi_thanhtoan(self, sp):
  self.ds_thanhtoan = [i for i in self.ds_thanhtoan if i != sp]
  self.hien_thi_lai_thanhtoan()

  def cap_nhat_tong_tien(self):
    tong = 0
    for comp in self.column_thanhtoan.get_components():
      try:
        tong += int(comp.item['giasanpham']) * comp.so_luong
      except:
        continue
    self.label_tongtien.text = f"{tong:,} VND"