from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=300)
	url = models.TextField()
	body = models.TextField(max_length=1000)
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to="image/blogimages/")
	icon = models.ImageField(upload_to="image/blogimages/")
	pub_date = models.DateTimeField(auto_now=False, auto_now_add=False) #models.DateTime
	hunter = models.ForeignKey(User, on_delete=models.CASCADE) #if an hunter(a user) is deleted, delete every product attached to it

	#returns specified text chunk from body
	#nb: when you define a functon in a class you must pass a self parameter into it
	def summary(self):
		return self.body[:100] #extract first 100 characters

	def __str__(self):
		return self.title #show titles in python admin page for blog model

	def pub_date_pretty(self):
		return pub_date.strftime('%b %e %Y')


	'''NB: anytime you make changes on a model such as renaming a field or so, you will need to makemigrations
       and then migrate'''
