from PIL import Image, ImageDraw, ImageFont

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def mainroute():
    """henlo"""
    html = """
<html>
<head>
<meta name="og:image" itemprop="image" content="path/to/image.png">
</head>
</html>
"""
    return html

@app.route("/math.png")
def mathroute():
    """Jeg ska åbenbart skrive en docstring, ellers klager pylint"""
    image_dimensions = (600, 200)
    title = "Kan du løse det her matematik problem?"
    img = Image.new("RGB", image_dimensions, color=(125, 125, 125))
    draw = ImageDraw.Draw(img)
    fontsize = 25
    font = ImageFont.truetype("arial.ttf", fontsize)
    textsize = draw.textlength(text=title, font=font)
    draw.text((image_dimensions[0] / 2 - textsize / 2, 10), title, (255, 255, 255), font=font)


    mathfontsize = 75
    mathfont = ImageFont.truetype("arial.ttf", mathfontsize)
    mathstring = "2 + 2 / 2"
    mathsize = draw.textlength(text=mathstring, font=mathfont)
    draw.text((image_dimensions[0] / 2 - mathsize / 2, image_dimensions[1] - mathfontsize - 30), mathstring, (255, 255, 255), font=mathfont)


    img.save("temporary.png")
    return send_file("temporary.png", mimetype="image/png")


if __name__ == "__main__":
    app.run("0.0.0.0", 8000, debug=True)