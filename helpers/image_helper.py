import io
from PIL import Image, ImageDraw, ImageFont


def generate(rank, rating, background_color, width, height):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    try:
        font_rank = ImageFont.truetype('fonts/Iosevka-Bold.ttc', 36)
        font_rating = ImageFont.truetype('fonts/Iosevka-Bold.ttc', 36)
    except:
        font_rank = ImageFont.load_default()
        font_rating = ImageFont.load_default()

    # Draw a rectangel with the background color
    rect_height = height // 4
    rect_y = (height - rect_height) // 2
    draw.rectangle([0, rect_y, width, rect_y + rect_height], fill=background_color)

    # Prepare text content
    rank_text = rank.strip().upper()
    rating_text = f'{rating}'

    # Calculate text positions (centered)
    rank_bbox = draw.textbbox((0, 0), rank_text, font=font_rank)
    rating_bbox = draw.textbbox((0, 0), rating_text, font=font_rating)

    rank_width = rank_bbox[2] - rank_bbox[0]
    rank_ascent, rank_descent = font_rank.getmetrics()
    rank_height = rank_ascent + rank_descent

    rating_width = rating_bbox[2] - rating_bbox[0]
    rating_ascent, rating_descent = font_rating.getmetrics()
    rating_height = rating_ascent + rating_descent

    # Position text in the center
    rank_x = (width - rank_width) // 2
    rank_y = (height // 2) - rank_height
    rating_x = (width - rating_width) // 2
    rating_y = (height // 2)

    # Draw text on image
    draw.text((rank_x, rank_y), rank_text, fill=(255, 255, 255), font=font_rank)
    draw.text((rating_x, rating_y), rating_text, fill=(255, 255, 255), font=font_rating)

    # Save image to bytes
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)

    return img_byte_arr.getvalue()
