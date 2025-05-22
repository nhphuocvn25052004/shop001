from ._anvil_designer import item_thanhtoanTemplate
from anvil import *
from anvil import Timer

class item_thanhtoan(item_thanhtoanTemplate):
  def __init__(self, item=None, parent_form=None, **properties):
    self.init_components(**properties)
    self.item = item
    self.parent_form = parent_form
    self.so_luong = 1
    self.hold_timer = None

    # Gán role để đẹp như POS
    self.btn_tang.role = "soluong-btn"
    self.btn_giam.role = "soluong-btn"
    self.btn_xoa.role = "btn-xoa"
    self.label_tong.role = "tong-dong"

    # Nếu đã có item thì hiển thị
    if self.item:
      self.hien_item()
      
  # ✅ Hàm hiển thị thông tin sản phẩm
  def hien_item(self):
    self.label_ten.text = self.item['tensanpham']
    self.label_gia.text = f"{int(self.item['giasanpham']):,} VND"
    self.cap_nhat_hien_thi()

  # ✅ Cập nhật hiển thị số lượng và tổng tiền
  def cap_nhat_hien_thi(self):
    if not self.item:
      return

    gia = int(self.item['giasanpham'])
    self.label_sl.text = f"x{self.so_luong}"
    self.label_tong.text = f"{gia * self.so_luong:,} VND"

    if self.parent_form:
      self.parent_form.cap_nhat_tong_tien()

  # ✅ Tăng số lượng
  def tang_sl(self, **event_args):
    self.so_luong += 1
    self.cap_nhat_hien_thi()

  # ✅ Giảm số lượng
  def btn_giam_click(self, **event_args):
    if self.so_luong > 1:
      self.so_luong -= 1
      self.cap_nhat_hien_thi()

  # ✅ Xoá sản phẩm khỏi hóa đơn
  def btn_xoa_click(self, **event_args):
    if self.parent_form:
      self.parent_form.xoa_khoi_thanhtoan(self.item)

  # ✅ Giữ nút để tăng liên tục
  def bat_dau_giu(self, **event_args):
    self.tang_sl()
    self.hold_timer = Timer(interval=0.1, tick=self.tang_sl)
    self.hold_timer.start_running()
    self.add_component(self.hold_timer)

  def dung_giu(self, **event_args):
    if self.hold_timer:
      self.hold_timer.stop_running()
      self.hold_timer.remove_from_parent()
      self.hold_timer = None

  def btn_tang_click(self, **event_args):
    self.tang_sl()
    pass
