import requests


# Define a constant dictionary mapping ranks to colors
RANK_COLORS = {
    'newbie': (128, 128, 128),                  # Gray
    'pupil': (0, 128, 0),                       # Green
    'specialist': (0, 191, 191),                # Cyan
    'expert': (0, 0, 255),                      # Blue
    'candidate master': (170, 0, 170),          # Purple
    'master': (255, 165, 0),                    # Orange
    'international master': (255, 165, 0),      # Orange
    'grandmaster': (255, 0, 0),                 # Red
    'international grandmaster': (255, 0, 0),   # Red
    'legendary grandmaster': (108, 0, 81)       # Dark Red
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


def get_color_by_rank(rank):
    normalized_rank = rank.lower()
    return RANK_COLORS.get(normalized_rank, (128, 128, 128))
