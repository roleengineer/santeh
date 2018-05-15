from django.db import models

# Create your models here.
class Price(models.Model):
	"""docstring for Price"""
	


	'''def __init__(self, arg):
		super(Price, self).__init__()
		self.arg = arg'''
	
	title = models.CharField(max_length = 120)
	post = models.TextField()
	date = models.DateTimeField()


	def __str__(self):
		return self.title
		