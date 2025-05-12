from ._anvil_designer import delete_danhmucTemplate
from anvil import *
import anvil.server
from ..sua_danhmuc import sua_danhmuc

class delete_danhmuc(delete_danhmucTemplate):
  def __init__(self, parent_form=None, **properties):
    self.init_components(**properties)
    self.parent_form = parent_form  # Lưu lại form cha để gọi lại load_data
    self.label_id.text = str(self.item['id_danhmuc']) if self.item['id_danhmuc'] is not None else "N/A"
    self.label_ten.text = self.item['tendanhmuc'] or "Không có"

  def delete_click(self, **event_args):
    if confirm("Bạn có chắc chắn muốn xóa danh mục này?"):
      success = anvil.server.call('xoa_danh_muc', self.item['id_danhmuc'])
      if success:
        Notification("Đã xóa danh mục!", timeout=2).show()

        # Ép buộc gọi lại load_data() từ form cha
        if self.parent_form:
          self.parent_form.load_data()

        self.raise_event("x-close-alert")  # Đóng popup
      else:
        Notification("Xóa thất bại!", style="danger").show()

  def sua_click(self, **event_args):
    if self.item:  # ✅ Kiểm tra trước khi truyền
      alert(
      content=sua_danhmuc(item=self.item, parent_form=self.parent_form),
      large=True,
      title="Sửa danh mục"
    )
    else:
      alert("Không tìm thấy dữ liệu danh mục để sửa.")
    pass
