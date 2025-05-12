from ._anvil_designer import hienthiTemplate
from anvil import *
import anvil.server  # ✅ thêm dòng này

class hienthi(hienthiTemplate):
  def __init__(self, parent_form=None, **properties):
    self.init_components(**properties)
    self.parent_form = parent_form

    sp = self.item

    self.label_ten.text = sp['tensanpham']
    self.label_gia.text = f"{sp['giasanpham']} VND"
    self.image_1.source = sp['hinhanh'] if sp['hinhanh'] else None


  def delete_click(self, **event_args):
    if confirm("Bạn có chắc muốn xóa sản phẩm này?"):
      success = anvil.server.call('xoa_san_pham', self.item['id_sanpham'])
      if success:
        Notification("Đã xóa sản phẩm!", timeout=2).show()
        if self.parent_form:
          self.parent_form.load_lai_sanpham()
      else:
        alert("Xóa thất bại.")

  def sua_click(self, **event_args):
    from ..sua_sp import sua_sp
    popup = sua_sp(sanpham=self.item, parent_form=self.parent_form)  # 👈 Truyền form menu_sp
    alert(popup, title="Sửa sản phẩm", large=True, buttons=[])
