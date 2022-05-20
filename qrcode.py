import pyqrcode
import png
from pyqrcode import QRCode
name= "https://twitter.com/harshhes/photo"

url = pyqrcode.create(name)
url.png("harsh_photo.png", scale=8)

