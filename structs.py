class lists:
    user_name_post = None
    post_url = None
    likers_collected = []
    likers_collected_clean = []

    user_name_followers = None
    user_url_followers = None
    followers_collected = []
    followers_collected_clean = []

    user_name_following = None
    user_url_following = None
    following_collected = []
    following_collected_clean = []

    user_name_commenters = None
    user_url_commenters = None
    commenters_collected = []
    commenters_collected_clean = []

    non_follow_back = []
    unavailable = []

class sorting_options:
    is_private = None
    is_empty = None
    min_age = None
    max_age = None
    gender = None
    max_followers = None
    max_following = None
    country = []
    leave_comment = None
    leave_like = None
    number_of_like = None

class user:
    name = None
    url = None
    followers = None
    following = None
