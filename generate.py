#!/usr/bin/env python

import qrcode

url = "https://github.com/stumpy-dev/stumpy-links"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=1,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save('qrcode.png')
