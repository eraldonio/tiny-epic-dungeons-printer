"""
Thermal card layout generator for Tiny Epic Dungeons items.
Refined with:
- Centered 240px artwork flanked by fantasy flourishes on left and right
- Generous internal padding on set bonus box (no line merging)
- Removed footer reference text from the printed card (kept in CLI app)
- High-readability large typography
"""

import io
import os
import urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

from funprint.protocol import PRINTER_WIDTH

CACHE_DIR = Path.home() / ".cache" / "funprint" / "dungeons"


def get_fonts():
    """Finds and loads the best available TrueType fonts on the system."""
    bold_candidates = [
        "/usr/share/fonts/julietaula-montserrat-fonts/Montserrat-Bold.otf",
        "/usr/share/fonts/google-droid-sans-fonts/DroidSans-Bold.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/liberation-sans-fonts/LiberationSans-Bold.ttf",
    ]
    regular_candidates = [
        "/usr/share/fonts/julietaula-montserrat-fonts/Montserrat-Regular.otf",
        "/usr/share/fonts/google-droid-sans-fonts/DroidSans.ttf",
        "/usr/share/fonts/dejavu-sans-fonts/DejaVuSans.ttf",
        "/usr/share/fonts/liberation-sans-fonts/LiberationSans-Regular.ttf",
    ]

    bold_path = next((p for p in bold_candidates if os.path.exists(p)), None)
    regular_path = next((p for p in regular_candidates if os.path.exists(p)), None)

    if bold_path and regular_path:
        return {
            "title": ImageFont.truetype(bold_path, 25),
            "banner": ImageFont.truetype(bold_path, 18),
            "tag": ImageFont.truetype(bold_path, 18),
            "body": ImageFont.truetype(regular_path, 21),
            "body_bold": ImageFont.truetype(bold_path, 21),
        }
    else:
        d = ImageFont.load_default()
        return {k: d for k in ["title", "banner", "tag", "body", "body_bold"]}


def get_cached_image(url: str, filename: str) -> Image.Image:
    """Loads local image if present, otherwise checks cache or downloads."""
    local_repo_path = Path(__file__).resolve().parent / "web" / "images" / filename
    if local_repo_path.exists():
        try:
            return Image.open(local_repo_path)
        except Exception:
            pass

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    local_cache_path = CACHE_DIR / filename

    if local_cache_path.exists():
        try:
            return Image.open(local_cache_path)
        except Exception:
            pass

    if url:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8.0) as resp:
            img_bytes = resp.read()

        with open(local_cache_path, "wb") as f:
            f.write(img_bytes)

        return Image.open(io.BytesIO(img_bytes))

    # Blank fallback if no image
    return Image.new("L", (240, 240), color=255)

def wrap_text_pixels(text: str, font: ImageFont.ImageFont, max_width_px: int = 340) -> list[str]:
    """Wraps text so no line exceeds max_width_px."""
    dummy_img = Image.new("L", (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    lines = []

    for paragraph in text.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        words = paragraph.split(" ")
        current_line = []
        for word in words:
            test_line = " ".join(current_line + [word])
            bbox = draw.textbbox((0, 0), test_line, font=font)
            line_w = bbox[2] - bbox[0]
            if line_w <= max_width_px:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
        if current_line:
            lines.append(" ".join(current_line))

    return lines


def draw_side_flourish(draw: ImageDraw.ImageDraw, cx: int, top_y: int, bot_y: int):
    """Draws an ornate fantasy filigree column centered at cx between top_y and bot_y."""
    mid_y = (top_y + bot_y) // 2

    # Vertical spine
    draw.line([(cx, top_y + 25), (cx, bot_y - 25)], fill=0, width=1)

    # 3 Diamond ornaments
    for y in [top_y + 25, mid_y, bot_y - 25]:
        draw.polygon([(cx, y - 7), (cx + 7, y), (cx, y + 7), (cx - 7, y)], fill=0)
        draw.point((cx, y), fill=255)

    # Filigree curves / scrolls
    draw.arc([(cx - 15, mid_y - 42), (cx + 15, mid_y - 14)], start=180, end=360, fill=0, width=1)
    draw.arc([(cx - 15, mid_y + 14), (cx + 15, mid_y + 42)], start=0, end=180, fill=0, width=1)

    # Horizontal accent tics
    draw.line([(cx - 14, mid_y), (cx + 14, mid_y)], fill=0, width=2)
    draw.line([(cx - 10, top_y + 12), (cx + 10, top_y + 12)], fill=0, width=1)
    draw.line([(cx - 10, bot_y - 12), (cx + 10, bot_y - 12)], fill=0, width=1)


def render_dungeon_item_card(item: dict) -> Image.Image:
    """
    Renders a Tiny Epic Dungeons item card onto a 384px wide thermal receipt.
    """
    fonts = get_fonts()
    content_width = PRINTER_WIDTH - 36  # 348px usable width for text

    # 1. Download/Load card illustration
    if item.get("type") == "Hero" or item.get("category") == "Hero Mat":
        img_filename = f"hero_{item['id']}.png"
    elif item.get("card_type") == "Spell" or item.get("category") == "Spell Card" or item.get("type") == "Spell":
        img_filename = f"spell_{item['id']}.png"
    else:
        img_filename = f"item_{item['id']}.png"
    card_art = get_cached_image(item['image_url'], img_filename)

    # 2. Resized artwork: 240px wide centered (flanked by flourishes)
    art_w = 240
    ratio = art_w / card_art.width
    art_h = int(card_art.height * ratio)
    card_art_resized = card_art.convert('L').resize((art_w, art_h), Image.Resampling.LANCZOS)

    # 3. Format Title & Text with pixel-perfect wrapping
    title_lines = wrap_text_pixels(item['name'].upper(), fonts['title'], max_width_px=content_width)
    desc_lines = wrap_text_pixels(item['description'], fonts['body'], max_width_px=content_width)

    # Set bonus text wrapped inside a narrower box (320px)
    set_lines = []
    if item.get("set_bonus"):
        set_lines = wrap_text_pixels(item['set_bonus'], fonts['body'], max_width_px=content_width - 32)

    # Calculate line heights with comfortable spacing
    title_line_h = 32
    body_line_h = 30
    set_line_h = 30

    title_block_h = len(title_lines) * title_line_h
    desc_block_h = len(desc_lines) * body_line_h
    
    # Generous set box height: 42px header + lines * line_h + 20px bottom breathing room
    set_box_h = (42 + len(set_lines) * set_line_h + 20) if set_lines else 0

    # Total card height (no bottom reference text)
    # top_border(12) + banner(46) + margin(14) + title(title_block_h) + tag(36) + divider(14)
    # + art(art_h + 24) + effect_header(30) + desc(desc_block_h) + spacing(18)
    # + set_box(set_box_h + 20 if set_lines else 0) + bottom_margin(24) + bottom_border(12)
    total_h = (
        12 + 46 + 14
        + title_block_h + 36 + 14
        + art_h + 26
        + 32 + desc_block_h + 18
        + (set_box_h + 22 if set_lines else 0)
        + 24 + 12
    )

    img = Image.new('L', (PRINTER_WIDTH, total_h), color=255)
    draw = ImageDraw.Draw(img)

    # Outer decorative borders
    draw.rectangle([(6, 6), (PRINTER_WIDTH - 6, total_h - 6)], outline=0, width=3)
    draw.rectangle([(11, 11), (PRINTER_WIDTH - 11, total_h - 11)], outline=0, width=1)

    # Header banner (inverted black box)
    draw.rectangle([(18, 18), (PRINTER_WIDTH - 18, 62)], fill=0)
    banner_txt = "TINY EPIC DUNGEONS"
    bbox_b = draw.textbbox((0, 0), banner_txt, font=fonts['banner'])
    bw = bbox_b[2] - bbox_b[0]
    draw.text(((PRINTER_WIDTH - bw) // 2, 28), banner_txt, fill=255, font=fonts['banner'])

    # Title (Large, bold)
    cur_y = 76
    for t_line in title_lines:
        bbox_t = draw.textbbox((0, 0), t_line, font=fonts['title'])
        tw = bbox_t[2] - bbox_t[0]
        draw.text(((PRINTER_WIDTH - tw) // 2, cur_y), t_line, fill=0, font=fonts['title'])
        cur_y += title_line_h

    # Slot & Set Tag (Bold)
    if item.get("type") == "Hero" or item.get("category") == "Hero Mat":
        category_tag = f"[ HERO: {item.get('title', '').upper()} ]"
    elif item.get("card_type") == "Spell" or item.get("category") == "Spell Card" or item.get("type") == "Spell":
        category_tag = "[ SPELL CARD ]"
    else:
        category_tag = f"[ {item['type'].upper()} ]"
        if item.get('set'):
            category_tag += f"  •  [ {item['set'].upper()} ]"
        else:
            category_tag += "  •  [ LOOT CARD ]"
    bbox_tag = draw.textbbox((0, 0), category_tag, font=fonts['tag'])
    tag_w = bbox_tag[2] - bbox_tag[0]
    draw.text(((PRINTER_WIDTH - tag_w) // 2, cur_y + 2), category_tag, fill=0, font=fonts['tag'])
    cur_y += 34

    draw.line([(18, cur_y), (PRINTER_WIDTH - 18, cur_y)], fill=0, width=2)
    cur_y += 12

    # Centered artwork flanked by flourishes
    art_x = (PRINTER_WIDTH - art_w) // 2
    art_top = cur_y
    art_bot = cur_y + art_h

    # Double frame around artwork
    draw.rectangle([(art_x - 3, art_top - 3), (art_x + art_w + 2, art_bot + 2)], outline=0, width=2)
    draw.rectangle([(art_x - 6, art_top - 6), (art_x + art_w + 5, art_bot + 5)], outline=0, width=1)
    img.paste(card_art_resized, (art_x, art_top))

    # Draw flourishes on Left (cx ~34) and Right (cx ~350)
    flourish_left_cx = art_x // 2
    flourish_right_cx = PRINTER_WIDTH - (art_x // 2)
    draw_side_flourish(draw, flourish_left_cx, art_top, art_bot)
    draw_side_flourish(draw, flourish_right_cx, art_top, art_bot)

    cur_y = art_bot + 16
    draw.line([(18, cur_y), (PRINTER_WIDTH - 18, cur_y)], fill=0, width=2)
    cur_y += 16

    # Description / Rules text (Large & readable)
    draw.text((20, cur_y), "EFFECT:", fill=0, font=fonts['body_bold'])
    cur_y += 30

    for line in desc_lines:
        draw.text((20, cur_y), line, fill=0, font=fonts['body'])
        cur_y += body_line_h

    cur_y += 14

    # Set Bonus Box (with generous internal padding so text never touches border)
    if set_lines:
        box_top = cur_y
        draw.rectangle([(18, box_top), (PRINTER_WIDTH - 18, box_top + set_box_h)], outline=0, width=2)
        draw.text((28, box_top + 10), "★ SET BONUS:", fill=0, font=fonts['body_bold'])
        
        by = box_top + 40
        for sline in set_lines:
            draw.text((28, by), sline, fill=0, font=fonts['body'])
            by += set_line_h

        cur_y = box_top + set_box_h + 20

    # Clean ending (no bottom reference text)
    return img
