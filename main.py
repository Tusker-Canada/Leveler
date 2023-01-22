xp = 0 # USER XP
member = "NAME" # USERNAME
member_avatar_url = "IMG_PATH" # USER IMAGE


#BUILT BY TUSKER-CANADA


#IMPORTS

import numerize
from numerize import numerize
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from io import BytesIO
from PIL import ImageChops


lvl = 0
rank = 5
while True:
    if xp < ((50*(lvl**2))+(50*lvl)):
        break
    lvl += 1
xp -= ((50*((lvl-1)**2)) + (50*(lvl-1)))
boxes = int((xp/(200*((1/2) * lvl)))*20)

WHITE = (0, 0, 0)
MAIN_BLUE = (118, 219, 168)
BACKGROUND_BLUE =(135, 188, 160)
BACKGROUNDCARD = (168, 184, 176)


BAR_BIG = 1492  # how big bar?(length)


xpneed = int(200*((1/2)*lvl)) - 0
xphave = xp - 0

total = (BAR_BIG-30)/xpneed

length_of_bar = (xphave * total) + 60

profile = member_avatar_url
card_size = (2500, 800)
img = Image.new("RGBA", card_size, BACKGROUNDCARD)
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("font.ttf", 100)
draw.text((50, 50), "{}".format(member), WHITE,
            font=font)
draw.text((50, 240), f"Rank: {rank}",
            WHITE, font=font)  

draw.text((500, 240), f"Level: {lvl}", WHITE, font=font)

xp = numerize.numerize(xp)
out_of = numerize.numerize(int(200*((1/2)*lvl)))
draw.text(
    (850, 525), f"Xp: {xp}/{out_of}", WHITE, font=font)

def circle(pfp, size=(700, 700)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp
if length_of_bar > BAR_BIG-30:
    length_of_bar = length_of_bar - 60
    draw.rounded_rectangle((50, 670, BAR_BIG, 750), 30, fill=BACKGROUND_BLUE, outline=WHITE, width=10)
    draw.rectangle((60, 680, 80, 740),fill=WHITE) #left side "rectangle" to make bar more rectangular
    draw.rectangle(((BAR_BIG-10), 680, (BAR_BIG-30), 740),fill=WHITE) #right side "rectangle" to make bar more rectangular
    draw.rectangle((80, 680, length_of_bar, 740),fill=MAIN_BLUE)
elif length_of_bar == 60.0 or length_of_bar < 61:
    draw.rounded_rectangle((50, 670, BAR_BIG, 750), 30, fill=BACKGROUND_BLUE, outline=WHITE, width=10)
    draw.rectangle((60, 680, 80, 740),fill=WHITE) #left side "rectangle" to make bar more rectangular
    draw.rectangle(((BAR_BIG-10), 680, (BAR_BIG-30), 740),fill=WHITE) #right side "rectangle" to make bar more rectangular
else:
    draw.rounded_rectangle((50, 670, BAR_BIG, 750), 30, fill=BACKGROUND_BLUE, outline=WHITE, width=10)
    draw.rectangle((60, 680, 80, 740),fill=WHITE) #left side "rectangle" to make bar more rectangular
    draw.rectangle(((BAR_BIG-10), 680, (BAR_BIG-30), 740),fill=WHITE) #right side "rectangle" to make bar more rectangular
    draw.rectangle((80, 680, length_of_bar, 740),fill=MAIN_BLUE)

print(length_of_bar)    


pfp = Image.open(profile).convert('RGBA')
pfp = circle(pfp)
img.paste(pfp, (1650, 50), pfp)
final_bytes = BytesIO()
img.save("real.png")
