from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# CASCADE means if we delete the User then delete their profile too 
	
	image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	# profile_pics is the directory in which the images of the users present when we upload the profile

	def __str__(self):
		send=self.user.username
		return '%s  Profile'%send

