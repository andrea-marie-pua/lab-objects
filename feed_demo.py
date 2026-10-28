from lab_classes import User, Tweet


def build_feed():
    # Create two accounts
    andrea = User('andrea')
    dopplegangerandrea = User('dopplegangerandrea')

    users = [andrea, dopplegangerandrea]

    # Create three posts
    post1 = Tweet('andrea', 'Microdosing adenosine antagonist class-IV #midterm week :)')
    post2 = Tweet('dopplegangerandrea', 'Anyone want a study buddy? #looking4friends')
    post3 = Tweet('andrea', 'Finally finished my coding lab!! #CSCI40!')

    posts = [post1, post2, post3]

    # Follow and unfollow
    andrea.follow()
    dopplegangerandrea.follow()
    andrea.unfollow()

    # Like and unlike
    post1.like()
    post1.like()
    post1.unlike()
    post2.like()
    post3.like()

    return users, posts


def main():
    users, posts = build_feed()

    print('USERS')
    for user in users:
        print(user)

    print('POSTS')
    for post in posts:
        print(post)
        print(post.hashtags())


if __name__ == '__main__':
    main()