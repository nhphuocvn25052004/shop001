from ._anvil_designer import add_danhmucTemplate
from anvil import *
import anvil.server
from .delete_danhmuc import delete_danhmuc

class add_danhmuc(add_danhmucTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    self.repeating_panel_1.item_template = delete_danhmuc  # Gán template
    # ⏬ Lắng nghe sự kiện x-refresh từ mỗi item con để cập nhật danh sách khi xóa
    self.repeating_panel_1.set_event_handler("x-refresh", self.load_data)
    self.load_data()
    
  def load_data(self, **event_args):
    # 📥 Gọi server để lấy danh sách danh mục
    ds = anvil.server.call('lay_tat_ca_danh_muc')
    self.repeating_panel_1.items = ds
  
  def chapnhan_click(self, **event_args):
    ten_danh_muc = self.text_box_1.text

    if not ten_danh_muc:
      alert("Vui lòng nhập tên danh mục.", title="Thiếu thông tin")
      return

    try:
      ket_qua = anvil.server.call('them_danh_muc', ten_danh_muc)
      alert(ket_qua, title="Thành công")
      self.text_box_1.text = ""
      self.load_data()  # ✅ Sau khi thêm thì cập nhật danh sách
    except Exception as e:
      alert(f"Lỗi: {e}", title="Lỗi")
