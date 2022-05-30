
import os
import dataframe_image as dfi
from PIL import Image

from Constants import BASE_IMAGE

def getStyle(frame_color, text_color):
    styles = [
        dict(selector="th", props=[("color", "#fff"),
                                   ("border", "1px solid #eee"),
                                   ("padding", "18px 35px"),
                                   ("background", frame_color),
                                   ("text-transform", "uppercase"),
                                   ("font-size", "15px"),

                                   ]),
        dict(selector="td", props=[("color", text_color),
                                   ("border", "1px solid #eee"),
                                   ("padding", "12px 35px"),
                                   ("font-size", "20px"),
                                   ("text-align", "left")

                                   ]),
        dict(selector="", props=[
            ("font-family", 'Arial'),
            ("margin", "25px auto"),
            ("border", "5px solid "+frame_color),
            ("width", "1024px"),

        ]),
    ]

    return styles


def setStyle(df, frame_color, text_color):
    style = getStyle(frame_color, text_color)
    df = df.style.set_table_styles(style).hide(axis='index')
    return df

 

def prepareGainerAndLoserImage(gainerDf, loserDf,filename):
    gainerImg = "gainer.png"
    loserImg = "loser.png"
    base = Image.open(BASE_IMAGE)
    
    gainerDf = setStyle(gainerDf, "#189AB4", "#05445E")
    loserDf = setStyle(loserDf, "#F652A0", "#F51720")    
    dfi.export(gainerDf, gainerImg)
    dfi.export(loserDf, loserImg)
    
    gainer = Image.open(gainerImg)
    loser = Image.open(loserImg)
    
    baseWidth, baseHeight = base.size
    gainerWidth, gainerHeight = gainer.size
    loserWidth, loserHeight = loser.size

    base.paste(gainer, (int((baseWidth - gainerWidth) / 2), 100))
    base.paste(loser, (int((baseWidth - loserWidth) / 2), gainerHeight+200))
    base.save(filename)
    
    clean(loserImg)
    clean(gainerImg)

     
    return filename

def clean(path):
    os.remove(path)