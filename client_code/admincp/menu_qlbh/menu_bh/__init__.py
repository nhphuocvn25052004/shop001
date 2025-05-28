from ._anvil_designer import menu_bhTemplate
from anvil import *
import anvil.server
from .item_sp import item_sp
from .item_thanhtoan import item_thanhtoan
import copy
class menu_bh(menu_bhTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.flow_panel_sp.clear()
    self.flow_panel_danhmuc.clear()
    self.label_danhmuc.foreground = "white"
    self.tabs_thucdon.tab_titles = ["Đơn 1"]
    self.ds_thanhtoan = [[]for _ in self.tabs_thucdon.tab_titles]
    self.tabs_thucdon.set_event_handler('tab_click', self.tabs_thucdon_tab_click)
    self.label_tongtien.text = "0 VND"

    self.load_danhmuc()
    self.load_sp()  # Mặc định load tất cả sản phẩm

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
      self.flow_panel_sp.add_component(item_sp(item=sp, parent_form=self))
    if not ds_sp:
      self.flow_panel_sp.add_component(Label(text="Hết sản phẩm", align="center", bold=True, foreground="red"))

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

  def dangxuat_click(self, **event_args):
    open_form('index', logged_in=False)

  def them_vao_thanhtoan(self, sp):
    index = self.tabs_thucdon.active_tab_index
    if index >= len(self.ds_thanhtoan):
      # Nếu index vượt quá phạm vi, thêm các đơn hàng trống cho đến khi đủ
      for _ in range(len(self.ds_thanhtoan), index + 1):
        self.ds_thanhtoan.append([])
    ds_don = self.ds_thanhtoan[index]

    # Kiểm tra xem sản phẩm đã có trong đơn chưa
    for item in ds_don:
      if item['id'] == sp['id']:
        item['so_luong'] += 1
        break
    else:
      # Nếu chưa có, thêm sản phẩm mới với số lượng 1
      sp_moi = copy.deepcopy(sp)  # Sử dụng deepcopy để tạo bản sao
      sp_moi['so_luong'] = 1
      ds_don.append(sp_moi)

    self.hien_thi_lai_thanhtoan()
    self.cap_nhat_tong_tien()


  def hien_thi_lai_thanhtoan(self):
    index = self.tabs_thucdon.active_tab_index
    while index >= len(self.ds_thanhtoan):
      self.ds_thanhtoan.append([])
    self.column_thanhtoan.clear()
    for item in self.ds_thanhtoan[index]:
      self.column_thanhtoan.add_component(item_thanhtoan(item=item, parent_form=self))

  def xoa_khoi_thanhtoan(self, sp):
    index = self.tabs_thucdon.active_tab_index
    while index >= len(self.ds_thanhtoan):
      self.ds_thanhtoan.append([])
    self.ds_thanhtoan[index] = [i for i in self.ds_thanhtoan[index] if i['id'] != sp['id']]
    self.hien_thi_lai_thanhtoan()
    self.cap_nhat_tong_tien()

  def cap_nhat_tong_tien(self):
    index = self.tabs_thucdon.active_tab_index
    while index >= len(self.ds_thanhtoan):
      self.ds_thanhtoan.append([])
    tong = 0
    for item in self.ds_thanhtoan[index]:
      try:
        tong += int(item['giasanpham']) * item['so_luong']
      except:
        continue
    self.label_tongtien.text = f"{tong:,} VND"

  def btn_thanhtoan_click(self, **event_args):
    index = self.tabs_thucdon.active_tab_index
    while index >= len(self.ds_thanhtoan):
      self.ds_thanhtoan.append([])
    danh_sach = []
    tong_tien = 0
    index = self.tabs_thucdon.active_tab_index

    for item in self.ds_thanhtoan[index]:
      ten = item['tensanpham']
      sl = item['so_luong']
      gia = int(item['giasanpham'])
      tong = gia * sl
      tong_tien += tong
      danh_sach.append(f"{ten} x{sl} = {tong:,} VND")

    if not danh_sach:
      alert("Chưa có món nào được chọn.", title="Thông báo")
      return

    noi_dung = "\n".join(danh_sach)
    noi_dung += f"\n\nTỔNG: {tong_tien:,} VND"

    alert(noi_dung, title="Hóa đơn")

    # Xóa danh sách sản phẩm của đơn hàng hiện tại
    self.ds_thanhtoan[index] = []
    self.hien_thi_lai_thanhtoan()
    self.cap_nhat_tong_tien()

  def tabs_thucdon_tab_click(self, tab_index, tab_title, **event_args):
    while tab_index >= len(self.ds_thanhtoan):
      self.ds_thanhtoan.append([])

    self.hien_thi_lai_thanhtoan()
    self.cap_nhat_tong_tien()
    

  def btn_them_don_click(self, **event_args):
    so_don = len(self.tabs_thucdon.tab_titles) + 1
    self.tabs_thucdon.tab_titles.append(f"Đơn {so_don}")
    self.ds_thanhtoan.append([])
    self.tabs_thucdon.active_tab_index = so_don - 1
    self.hien_thi_lai_thanhtoan()
    self.cap_nhat_tong_tien()

  def ensure_ds_thanhtoan(self, index):
    while index >= len(self.ds_thanhtoan):
      self.ds_thanhtoan.append([])

  def chip_thucdon_close_click(self, **event_args):
    """This method is called when the close link is clicked"""
    pass
