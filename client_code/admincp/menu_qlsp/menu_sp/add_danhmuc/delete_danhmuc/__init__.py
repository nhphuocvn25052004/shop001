from ._anvil_designer import delete_danhmucTemplate
from anvil import *
import anvil.server

class delete_danhmuc(delete_danhmucTemplate):
  def __init__(self, row, **properties):
    self.init_components(**properties)

    self.row = row  # lưu bản ghi được truyền vào

    # Hiển thị thông tin
    self.label_id.text = self.row['id_danhmuc']
    self.label_ten.text = self.row['tendanhmuc']

  def xoa_btn_click(self, **event_args):
    if confirm(f"Xoá danh mục '{self.row['tendanhmuc']}'?"):
      self.row.delete()
      Notification("Đã xoá thành công!", timeout=2).show()
      self.raise_event("x-close-alert")  # Đóng popup sau khi xoá
      self.raise_event("x-refresh")     # Yêu cầu làm mới danh sách nếu có
