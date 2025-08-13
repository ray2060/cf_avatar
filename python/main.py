import logging
import sys, datetime

from helpers import codeforces_helper, image_helper
from settings import *


logging.basicConfig(
            format='%(asctime)s [%(levelname)s]: %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO
        )

if __name__ == '__main__':
    logging.info('This program generates avatar image for Codeforces user')
    logging.info('Copyleft (C) 2025  Ray Hu<r@pythoner.work>\n')

    if len(sys.argv) < 2:
        sys.exit('Usage: python main.py <user_name>')

    user_name = sys.argv[1]
    logging.info(f'Generating avatar image for user: {user_name}')

    rank, rating = '', 0

    try:
        rank, rating = codeforces_helper.get_rank_and_rating(user_name)
    except Exception as e:
        sys.exit('Exception in fetching Codeforces user profile: %s' % (e,))

    background_color = codeforces_helper.get_color_by_rank(rank)
    image_data = image_helper.generate(rank, rating, background_color,
                                       AVATAR_WIDTH, AVATAR_HEIGHT)
    time_now = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    filename = f'{time_now}_{user_name}.png'

    with open(filename, 'wb') as f:
        f.write(image_data)

    logging.info(f"Avatar image saved as {filename}")
