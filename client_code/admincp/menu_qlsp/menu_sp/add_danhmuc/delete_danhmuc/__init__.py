from ._anvil_designer import delete_danhmucTemplate
from anvil import *

class delete_danhmuc(delete_danhmucTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def form_show(self, **event_args):
    # Anvil sẽ gọi hàm này khi item đã sẵn sàng → bạn dùng tại đây
    self.label_id.text = self.item.get('id_danhmuc', 'N/A')
    self.label_ten.text = self.item.get('tendanhmuc', 'Không có')

  def xoa_btn_click(self, **event_args):
    if confirm(f"Xoá danh mục '{self.item['tendanhmuc']}'?"):
      self.item.delete()
      Notification("Đã xoá thành công!", timeout=2).show()
      self.raise_event("x-refresh")
