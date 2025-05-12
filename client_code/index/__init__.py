from ._anvil_designer import indexTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.users

class index(indexTemplate):
  def __init__(self, logged_in=False, **properties):
    self.init_components(**properties)
    self.logged_in = logged_in  # Nhận trạng thái từ form khác
    self.update_ui()

  def update_ui(self):
    if self.logged_in:
      self.dangxuat.text = "Đăng xuất"
      self.sanpham.visible = True
      self.banhang.visible = True
    else:
      self.dangxuat.text = "Đăng nhập"
      self.sanpham.visible = False
      self.banhang.visible = False
      
  def sanpham_click(self, **event_args):
    open_form('admincp.menu_qlsp.menu_sp')  # Mở sang form sản phẩm

  def dangxuat_click(self, **event_args):
    try:
      if self.logged_in:
        # Nếu đang đăng nhập → thực hiện đăng xuất
        anvil.users.logout()
        self.logged_in = False
        Notification("Đã đăng xuất", timeout=2).show()
      else:
        # cái này dùng không được
        user = anvil.users.login_with_form() 
        if user:  
          # cái này dùng được
          user = anvil.users.login_with_form()
          anvil.server.call('cap_nhat_id_khachhang')
          self.logged_in = True
          Notification("Đăng nhập thành công!", timeout=2).show()
        else:
          alert("Đăng nhập bị hủy!")
    except Exception as e:
      alert(f"Đăng nhập thất bại hoặc bị lỗi!\nChi tiết: {e}")

    self.update_ui()  # Luôn cập nhật giao diện



