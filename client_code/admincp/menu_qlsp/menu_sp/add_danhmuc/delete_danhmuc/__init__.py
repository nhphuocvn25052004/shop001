from ._anvil_designer import delete_danhmucTemplate
from anvil import *
import anvil.server

class delete_danhmuc(delete_danhmucTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # Gọi server để lấy danh mục và nạp vào dropdown
    self.ds_danh_muc = anvil.server.call('lay_tat_ca_danh_muc')
    self.dropdown_1.items = [(row['tendanhmuc'], row) for row in self.ds_danh_muc]

  def dropdown_1_change(self, **event_args):
    # Khi chọn danh mục, hiển thị thông tin ra label
    row = self.dropdown_1.selected_value
    if row:
      self.label_1.text = row['id_danhmuc']
      self.label_2.text = row['tendanhmuc']

  def delete_btn_click(self, **event_args):
    row = self.dropdown_1.selected_value
    if row:
      if confirm(f"Bạn có chắc muốn xoá danh mục '{row['tendanhmuc']}' không?"):
        row.delete()
        Notification("Đã xoá thành công!", timeout=2).show()
        self.label_1.text = ""
        self.label_2.text = ""
        self.dropdown_1.items = [(r['tendanhmuc'], r) for r in anvil.server.call('lay_tat_ca_danh_muc')]
        self.dropdown_1.selected_value = None
