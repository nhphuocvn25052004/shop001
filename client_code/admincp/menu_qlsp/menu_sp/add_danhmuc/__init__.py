from ._anvil_designer import add_danhmucTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class add_danhmuc(add_danhmucTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  def chapnhan_click(self, **event_args):
    # Lấy nội dung từ TextBox
    ten_danh_muc = self.text_box_1.text

    # Kiểm tra dữ liệu có rỗng không
    if not ten_danh_muc:
      alert("Vui lòng nhập tên danh mục.", title="Thiếu thông tin")
      return

    try:
      # Gọi hàm từ server để thêm danh mục
      ket_qua = anvil.server.call('them_danh_muc', ten_danh_muc)
      alert(ket_qua, title="Thành công")

      # Xoá ô nhập sau khi thêm xong
      self.text_box_1.text = ""

    except Exception as e:
      alert(f"Lỗi: {e}", title="Lỗi")
