# 1.install (pip install pyqrcode) using terminal
import pyqrcode


url = pyqrcode.create('https://instagram.com/y_a_d_h_u_krishnan_?igshid=ZDdkNTZiNTM=')
url.svg("myqr.svg", scale=6)
