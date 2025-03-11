
# how to create a new class
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "kiko")
user_2 = User("002", "Love")
user_3 = User("003", "Abigail")
# print(user_1.id, user_1.username, user_1.followers)
user_1.follow(user_2)
user_1.follow(user_3)
print(f"user: {user_1.username} is following {user_1.following} and has {user_1.followers} number of followers")
print(f"user: {user_2.username} is following {user_2.following} and has {user_2.followers} number of followers")
print(f"user: {user_3.username} is following {user_3.following} and has {user_3.followers} number of followers")

# creating a new object from that class
# user_1 = User()

# creating an attribute for the object
# user_1.id = "001"
# user_1.username = "kiko"
