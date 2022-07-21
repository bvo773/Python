class User:
	def __init__(self, user_id, username):
		print("New user being created...")
		self.id = user_id
		self.username = username
		self.followers = 0
		self.following = 0

	# self, when the object calls this method, it knows the object that called it
	# self is a way for us to refer to the object that is created from the class blueprint
	def follow(self, user):
		user.followers += 1 # their followers go up by one
		self.following += 1 # our following count goes up by one

user_1 = User("001", "bino")
user_2 = User("002", "david")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)