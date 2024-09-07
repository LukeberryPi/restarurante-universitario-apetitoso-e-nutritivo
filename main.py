from instaloader import Instaloader, Profile

INSTAGRAM_USERNAME = "ru360ufsc"
L = Instaloader()

profile = Profile.from_username(L.context, INSTAGRAM_USERNAME)
posts = profile.get_posts()

for post in posts:
    print(post)
    L.download_post(post, INSTAGRAM_USERNAME)

def get_stories():
    return L.get_stories()

def is_menu_image(story):
    # return true if the story contains text with "almoço", "jantar" or "apetite"
    return True

print(get_stories())

# def main():
#     pass

# if __name__ == '__main__':
#     main()