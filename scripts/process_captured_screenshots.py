#!/usr/bin/env python3
"""Process raw captures into compliant guide screenshots:
- Viewport size: exactly 1366 x 768
- Opaque redaction of personal names / avatars / identifiers
- 3-4px bright red highlight rectangle around verified action
"""

from PIL import Image, ImageDraw

RED = (255, 26, 26)
BG_HEADER = (240, 245, 250) # Light blue/white header background for redaction

def redact_and_resize(img_path, crop_box=None):
    im = Image.open(img_path).convert("RGB")
    # Redact user name and avatar at top right if present
    # In 1920x945, the top-right header name/avatar is roughly at x: 1650..1920, y: 0..55
    # In Technofocus header, top right has PLB avatar at x: 1750..1880, y: 15..55
    draw = ImageDraw.Draw(im)
    
    # Check top right corner color
    top_right_color = im.getpixel((1660, 25))
    draw.rectangle([1650, 0, 1920, 60], fill=top_right_color)
    
    # If crop_box specified: crop to crop_box then resize to (1366, 768)
    # 1680x945 is 16:9 ratio. Resized to 1366x768 maintains aspect ratio.
    if crop_box:
        cropped = im.crop(crop_box)
    else:
        # Default: keep left sidebar (x: 0..1680, y: 0..945)
        cropped = im.crop((0, 0, 1680, 945))
        
    scaled = cropped.resize((1366, 768), Image.Resampling.LANCZOS)
    return scaled

def draw_red_box(img, box, width=4):
    draw = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    for i in range(width):
        draw.rectangle([x0 - i, y0 - i, x1 + i, y1 + i], outline=RED)
    return img

print("Helper ready")
