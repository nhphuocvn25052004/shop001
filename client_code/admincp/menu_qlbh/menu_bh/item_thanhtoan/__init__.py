from ._anvil_designer import item_thanhtoanTemplate
from anvil import *
from anvil import Timer

class item_thanhtoan(item_thanhtoanTemplate):
  def __init__(self, item=None, parent_form=None, **properties):
    self.item = item
    self.parent_form = parent_form
    self.so_luong = item.get('so_luong', 1)
    self.init_components(**properties)
    self.cap_nhat_hien_thi()

    self.btn_tang.role = "soluong-btn"
    self.btn_giam.role = "soluong-btn"
    self.btn_xoa.role = "btn-xoa"
    self.label_tong.role = "tong-dong"

    if self.item:
      self.hien_item()

  def hien_item(self):
    self.label_ten.text = self.item['tensanpham']
    self.label_gia.text = f"{int(self.item['giasanpham']):,} VND"
    self.cap_nhat_hien_thi()

  def cap_nhat_hien_thi(self):
    self.label_ten.text = self.item['tensanpham']
    self.label_soluong.text = str(self.so_luong)
    self.label_gia.text = f"{int(self.item['giasanpham']) * self.so_luong:,} VND"

  def tang_sl(self, **event_args):
    self.so_luong += 1
    self.cap_nhat_hien_thi()

  def btn_tang_click(self, **event_args):
    self.tang_sl()

  def btn_giam_click(self, **event_args):
    if self.so_luong > 1:
      self.so_luong -= 1
      self.cap_nhat_hien_thi()

  def btn_xoa_click(self, **event_args):
    if self.parent_form:
      self.parent_form.xoa_khoi_thanhtoan(self.item)
      self.remove_from_parent()  # Loại bỏ mục khỏi giao diện
      self.parent_form.cap_nhat_tong_tien()  # Cập nhật tổng tiền sau khi xóa
