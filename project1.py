import qrcode  #alias name
from PIL import Image

#using a variable qr
qr=qrcode.QRCode(version=1,
             error_correction=qrcode.constants.ERROR_CORRECT_H,
             box_size=6,
             border=4,)                  
# img= qr.make("https://www.youtube.com")
# img.save("Youtube.png")
qr.add_data("https://aws.amazon.com/free/?trk=16847e0c-46fb-467d-91ee-6e259e339665&sc_channel=ps&s_kwcid=AL!4422!10!72086958325164!72087482393523&ef_id=5e6ed55558d917beec91b270e9c85dfb:G:s&msclkid=5e6ed55558d917beec91b270e9c85dfb")
qr.make(fit=True)
img=qr.make_image(fill_color="red")
img.save("Amazon_Web_Services.png")


#qr for amazon.in
qr1=qrcode.QRCode(version=2,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=7,border=3,)
qr1.add_data("https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_pfleuceqh_e&adgrpid=1320515122347239&hvadid=82532458991604&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=156826&hvtargid=kwd-82533123856602:loc-90&hydadcr=14453_2334184&msclkid=8bba62f49f781e7024d505d12c67eac0")
qr1.make(fit=True)
img=qr1.make_image(fill_color="Blue")
img.save("Amazon.png")

#qrcode for myntra and facebook
qr2=qrcode.QRCode(version=3,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=5,border=6,)
qr2.add_data=("https://www.myntra.com/")
qr2.add_data=("https://www.facebook.com/")
qr2.make(fit=True)
img=qr.make_image(fill_color="purple")
img.save("Myntra.png")
img.save("Facebook.png")

qr3=qrcode.QRCode(version=4,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=7,border=3,)
qr3.add_data("image.png")
qr3.make(fit=True)
img=qr.make_image(fill_color="orange")
img.save("republic.png")

qr4=qrcode.QRCode(version=4,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=7,border=3,)
qr4.add_data("www.google.com")
qr3.make(fit=True)
img=qr.make_image(fill_color="Green")
img.save("google.png")