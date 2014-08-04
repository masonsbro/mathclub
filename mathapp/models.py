import hashlib
import uuid

from django.db import models

# Create your models here.

class User(models.Model):

	email = models.EmailField(unique = True)
	password_hash = models.CharField(max_length = 128, null = True, blank = True, default = "")
	password_salt = models.CharField(max_length = 32, null = True, blank = True, default = "")
	reset_code = models.CharField(max_length = 32, null = True, blank = True, default = "")
	admin = models.BooleanField(default = False)
	contributor = models.BooleanField(default = False)
	active = models.BooleanField(default = False)
	name = models.CharField(max_length = 64, null = True, blank = True, default = "")

	def set_password(self, password):
		# Generate random salt
		salt = uuid.uuid4().hex
		# Apply salt to password
		salted = password + salt
		# Hash the salted password
		hashed = hashlib.sha512(salted).hexdigest()
		# Store the results for later
		self.password_hash = hashed
		self.password_salt = salt

	def check_password(self, password):
		# Apply salt to password
		salted = password + self.password_salt
		# Hash the salted password
		hashed = hashlib.sha512(salted).hexdigest()
		# Check it against the stored one
		return self.password_hash == hashed

class BlogPost(models.Model):

	title = models.CharField(max_length = 256)
	body = models.TextField()
	author = models.ForeignKey('User', related_name = 'posts')
	date_created = models.DateTimeField(auto_now_add = True)
	date_modified = models.DateTimeField(auto_now = True)
	seen_by = models.ManyToManyField('User', related_name = 'posts_seen')

class Difficulty(models.Model):

	name = models.CharField(max_length = 256)

class Skill(models.Model):

	difficulty = models.ForeignKey('Difficulty')
	name = models.CharField(max_length = 256)

class ProblemGenerator(models.Model):

	skill = models.ForeignKey('Skill')
	name = models.CharField(max_length = 256)
	question = models.CharField(max_length = 256)
	answer = models.CharField(max_length = 256)

	def generate_problem(self):
		# Replace variables in question with random values
		# Replace variables in answer with same values and evaluate
		return self.question, float(self.answer)