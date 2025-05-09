from ._anvil_designer import delete_danhmucTemplate
from anvil import *

class delete_danhmuc(delete_danhmucTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

    # ✅ Truy cập đúng thuộc tính của row (LiveObjectProxy)
    self.label_id.text = str(self.item['id_danhmuc']) if self.item['id_danhmuc'] is not None else "N/A"
    self.label_ten.text = self.item['tendanhmuc'] or "Không có"
