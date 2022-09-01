import sys,os
from PIL import (
        Image,
        ImageFont,
        ImageDraw
        )

def validator(nama,desk):
    font_name_size,font_desc_size = None,None
    font_name_size = 40 if len(nama) <= 7 else 35
    font_desc_size = 25 if len(desk) <= 12 else 20
    draw_position = 735 if font_desc_size == 25 else 745

    return {
                "fontNameSize":font_name_size,
                "fontDescSize":font_desc_size,
                "drawPositionName":(60,750),
                "drawPositionDesc":(60,draw_position),
                "color":(225,225,225),
                }

def generate(path,nama,desk):
    foto = Image.open(path)
    template = Image.open("img/twibbon.png")

    foto.paste(template,(0,0),template)
    foto.save("result.png")
    combined = Image.open("result.png")
    config = validator(nama,desk)

    if combined:
       font1 = ImageFont.truetype("fonts/font.ttf",config["fontNameSize"])
       font2 = ImageFont.truetype("fonts/font.ttf",config["fontDescSize"])

    drawing = ImageDraw.Draw(combined)
    drawing.text(
                    config["drawPositionName"],
                    str(nama),
                    config["color"],
                    font=font1,
                    )

    drawing.text(
                    config["drawPositionDesc"],
                    "\n\n" + desk,
                    config["color"],
                    font=font2,
                    )
    done = "{}.png".format(nama)
    combined.save(done)


    return "[*] twibbon created"

if __name__=="__main__":
   run = generate(sys.argv[1],sys.argv[2],sys.argv[3])

   print (run);os.remove('result.png')
   print ('[*] result.jpg removed')


