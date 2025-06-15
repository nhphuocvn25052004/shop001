from ._anvil_designer import menu_bhTemplate
from anvil import *
import anvil.server
from .item_sp import item_sp
from .item_thanhtoan import item_thanhtoan

class menu_bh(menu_bhTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    self.flow_panel_sp.clear()
    self.flow_panel_danhmuc.clear()
    self.label_danhmuc.foreground = "white"
    self.ds_thanhtoan = []
    self.label_tongtien.text = "0 VND"
    self.so_don = 1  # Bắt đầu từ đơn 1

    self.them_hoadon_moi()  # Tạo đơn đầu tiên mặc định
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
    # Tìm xem sản phẩm đã có chưa
    for comp in self.column_thanhtoan.get_components():
      if comp.item == sp:
        comp.so_luong += 1
        comp.cap_nhat_hien_thi()
        return

    # Nếu chưa có → thêm mới
    self.ds_thanhtoan.append(sp)
    self.hien_thi_lai_thanhtoan()
    self.cap_nhat_tong_tien()


  def hien_thi_lai_thanhtoan(self):
    self.column_thanhtoan.clear()
    for item in self.ds_thanhtoan:
      self.column_thanhtoan.add_component(item_thanhtoan(item=item, parent_form=self))

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

  def btn_thanhtoan_click(self, **event_args):
    danh_sach = []
    tong_tien = 0

    for comp in self.column_thanhtoan.get_components():
      if hasattr(comp, "item") and comp.item:
        ten = comp.item['tensanpham']
        sl = comp.so_luong
        gia = int(comp.item['giasanpham'])
        tong = gia * sl
        tong_tien += tong
        danh_sach.append(f"{ten} x{sl} = {tong:,} VND")

    if not danh_sach:
      alert("Chưa có món nào được chọn.", title="Thông báo")
      return

    noi_dung = "\n".join(danh_sach)
    noi_dung += f"\n\nTỔNG: {tong_tien:,} VND"

    # ✅ Hiện hóa đơn
    alert(noi_dung, title="Hóa đơn")

    # ✅ Xóa danh sách + cập nhật tổng tiền
    self.column_thanhtoan.clear()
    self.ds_thanhtoan.clear()
    self.label_tongtien.text = "0 VND"

  def them_hoadon_moi(self):
    ten_don = f"Đơn {self.so_don}"
    lbl = Label(text=ten_don, bold=True)
    self.flow_panel_hoadon.add_component(lbl)
    self.so_don += 1

  def btn_them_don_click(self, **event_args):
    self.them_hoadon_moi()



