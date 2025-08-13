import requests


# Define a constant dictionary mapping ranks to colors
RANKS = {
    'newbie': {
        'color': (128, 128, 128),               # Gray
        'font_size': 36
    },
    'pupil': {
        'color': (0, 128, 0),                   # Green
        'font_size': 36
    },
    'specialist': {
        'color': (3, 168, 158),                 # Cyan
        'font_size': 36
    },
    'expert': {
        'color': (0, 0, 255),                   # Blue
        'font_size': 36
    },
    'candidate master': {
        'color': (170, 0, 170),                 # Purple
        'font_size': 36
    },
    'master': {
        'color': (255, 140, 0),                 # Orange
        'font_size': 36
    },
    'international master': {
        'color': (255, 140, 0),                 # Orange
        'font_size': 36
    },
    'grandmaster': {
        'color': (255, 0, 0),                   # Red
        'font_size': 36
    },
    'international grandmaster': {
        'color': (255, 0, 0),                   # Red
        'font_size': 30
    },
    'legendary grandmaster': {
        'color': (192, 64, 64),                 # Dark Red
        'font_size': 36
    }
}

def fetch(user_name):
    url = f'https://codeforces.com/api/user.info?handles={user_name}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data['status'] == 'OK':
            return data['result'][0]
        else:
            comment = data.get('comment', 'Unknown error')
            raise Exception(f'API Error: {comment}')
    except requests.RequestException as e:
        raise Exception(f'Failed to fetch data: {e}')


def get_rank_and_rating(user_name):
    try:
        user_data = fetch(user_name)
        rank = user_data.get('rank', 'unrated')
        rating = user_data.get('rating', 0)
        return rank, rating
    except Exception as e:
        raise Exception(f'Error getting rank and rating for {user_name}: {e}')


def get_font_size_by_rank(rank):
    normalized_rank = rank.lower()
    return RANKS.get(normalized_rank, {'font_size': 36}).get('font_size', 36)

def get_color_by_rank(rank):
    normalized_rank = rank.lower()
    return RANKS.get(normalized_rank, {'color': (0, 0, 0)}).get('color', (0, 0, 0))
