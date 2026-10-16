import os
from PIL import Image, ImageDraw

RAW_DIR = r"C:\Users\PC\.gemini\antigravity-ide\brain\b0383147-8848-4553-ad92-b46a9f6b3a99"
TARGET_DIR = r"d:\MSA\Levelup-microsoft-certification-voucher-guide\screenshots"
os.makedirs(TARGET_DIR, exist_ok=True)

RED = (255, 26, 26)

def draw_outline(img, bbox, width=3):
    draw = ImageDraw.Draw(img)
    x0, y0, x1, y1 = bbox
    for i in range(width):
        draw.rectangle([x0 - i, y0 - i, x1 + i, y1 + i], outline=RED)
    return img

def redact_light_header(im):
    draw = ImageDraw.Draw(im)
    draw.rectangle([1650, 0, 1920, 60], fill=(235, 242, 250))
    return im

def redact_dark_header(im):
    draw = ImageDraw.Draw(im)
    draw.rectangle([1750, 0, 1850, 60], fill=(12, 38, 49))
    return im

# 1. 07-enrolled-course-dashboard.png - Full Screen Courses View
im7 = Image.open(os.path.join(RAW_DIR, "full_my_courses_tab_1792120585142.png")).convert("RGB")
redact_dark_header(im7)
im7_sc = im7.resize((1366, 768), Image.Resampling.LANCZOS)
# Outline the AB-100 course card in full view:
draw_outline(im7_sc, (668, 340, 972, 755), width=4)
im7_sc.save(os.path.join(TARGET_DIR, "07-enrolled-course-dashboard.png"))

# 2. 08-learning-module.png - Full Screen Module List
im8 = Image.open(os.path.join(RAW_DIR, "raw_08_module_list_1792117511382.png")).convert("RGB")
redact_light_header(im8)
im8_sc = im8.resize((1366, 768), Image.Resampling.LANCZOS)
# Outline Module 1:
draw_outline(im8_sc, (228, 172, 1145, 300), width=4)
im8_sc.save(os.path.join(TARGET_DIR, "08-learning-module.png"))

# 3. 08-learning-activity.png - Full Screen Opened Activity
im_act = Image.open(os.path.join(RAW_DIR, "raw_08_activity_1792117538536.png")).convert("RGB")
redact_light_header(im_act)
im_act_sc = im_act.resize((1366, 768), Image.Resampling.LANCZOS)
# Outline Activity Header Banner:
draw_outline(im_act_sc, (226, 165, 1342, 365), width=4)
im_act_sc.save(os.path.join(TARGET_DIR, "08-learning-activity.png"))

# 4. 09-module-completion.png - Full Screen Module Completion Badge
im9 = Image.open(os.path.join(RAW_DIR, "raw_08_module_list_1792117511382.png")).convert("RGB")
redact_light_header(im9)
im9_sc = im9.resize((1366, 768), Image.Resampling.LANCZOS)
# Outline the Completed badge on Module 1:
draw_outline(im9_sc, (395, 260, 498, 290), width=3)
im9_sc.save(os.path.join(TARGET_DIR, "09-module-completion.png"))

# 5. 11-assessment-result.png - Dedicated Assessments Tab View
im11 = Image.open(os.path.join(RAW_DIR, "full_assessment_view_1792120221159.png")).convert("RGB")
redact_light_header(im11)
im11_sc = im11.resize((1366, 768), Image.Resampling.LANCZOS)
# Outline the Graded Assessment Row:
draw_outline(im11_sc, (220, 245, 1345, 310), width=4)
im11_sc.save(os.path.join(TARGET_DIR, "11-assessment-result.png"))

# 6. 12-course-completion.png - Full Screen Progress Widget
im12 = Image.open(os.path.join(RAW_DIR, "raw_08_module_list_1792117511382.png")).convert("RGB")
redact_light_header(im12)
im12_sc = im12.resize((1366, 768), Image.Resampling.LANCZOS)
# Outline the Progress 100% checkmark card in the right sidebar:
draw_outline(im12_sc, (1165, 68, 1348, 198), width=4)
im12_sc.save(os.path.join(TARGET_DIR, "12-course-completion.png"))

# 7. 15-levelup-helpdesk.png - Full Screen Support Page
im15 = Image.open(os.path.join(RAW_DIR, "raw_15_helpdesk_1792117674711.png")).convert("RGB")
redact_dark_header(im15)
im15_sc = im15.resize((1366, 768), Image.Resampling.LANCZOS)
# Outline the Need Assistance section:
draw_outline(im15_sc, (340, 375, 1300, 568), width=4)
im15_sc.save(os.path.join(TARGET_DIR, "15-levelup-helpdesk.png"))

print("All full-screen screenshots processed and saved!")
