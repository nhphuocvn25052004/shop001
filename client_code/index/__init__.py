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
      try:
        # Bắt buộc đăng nhập lại dù đang đăng nhập
        anvil.users.logout()  # thoát phiên hiện tại

        user = anvil.users.login_with_form(allow_cancel=True)
        if user:
          # Nếu bạn cần gán lại ID KH sau khi login
          anvil.server.call('cap_nhat_id_khachhang')

          self.logged_in = True
          self.update_ui()

          # Đăng nhập lại OK -> mở trang Sản phẩm
          open_form('admincp.menu_qlsp.menu_sp')
        else:
          # Người dùng bấm Cancel
          Notification("Bạn đã hủy đăng nhập.", timeout=2).show()
          self.logged_in = False
          self.update_ui()

      except Exception as e:
        alert(f"Lỗi khi yêu cầu đăng nhập lại:\n{e}")
        self.logged_in = False
        self.update_ui()


  def dangxuat_click(self, **event_args):
    try:
      if self.logged_in:
        # Nếu đang đăng nhập → thực hiện đăng xuất
        anvil.users.logout()
        self.logged_in = False
        Notification("Đã đăng xuất", timeout=2).show()
      else:
      # Đang đăng xuất → mở form đăng nhập
        user = anvil.users.login_with_form()  # ✅ Gọi đúng 1 lần
        if user:
          anvil.server.call('cap_nhat_id_khachhang')  # ✅ Gán ID tại đây
          self.logged_in = True
          Notification("Đăng nhập thành công!", timeout=2).show()
        else:
          alert("Đăng nhập bị hủy!")

    except Exception as e:
      alert(f"Đăng nhập thất bại hoặc bị lỗi!\nChi tiết: {e}")

    self.update_ui()  # ✅ Luôn cập nhật lại giao diện

  def banhang_click(self, **event_args):
    
    open_form('admincp.menu_qlbh.menu_bh')
    pass

  

