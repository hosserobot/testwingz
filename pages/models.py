from django.db import models

class Submit(models.Model):
	email	=models.EmailField()
	phone	=models.TextField()
	name	=models.CharField(max_length=100)
	date	=models.TextField()
	message	=models.TextField()

	def __str__(self):
		return self.name