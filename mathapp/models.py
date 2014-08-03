import hashlib
import uuid

from django.db import models

# Create your models here.

class User(models.Model):

	email = models.EmailField(unique = True)
	password_hash = models.CharField(max_length = 128)
	password_salt = models.CharField(max_length = 32)
	reset_code = models.CharField(max_length = 32, null = True, blank = True, default = "")
	admin = models.BooleanField(default = False)
	contributor = models.BooleanField(default = False)
	active = models.BooleanField(default = False)

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