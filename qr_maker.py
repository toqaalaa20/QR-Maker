
import qrcode

def qr_maker(data, size_box, border_size, color_fill, color_back):

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=size_box ,border=border_size,)
    qr.make(fit=True)
    qr.add_data(data)
    qr.make()
    img = qr.make_image(fill_color=color_fill, back_color=color_back)
    img.save("qr.png","PNG")

qr_maker('abcded',8,4,'black','white')
