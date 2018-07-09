from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=150)
	pub_date = models.DateTimeField()
	image = models.ImageField(upload_to = 'media/')
	body = models.TextField()

	def __str__(self):
		return self.title

    #I like the way pub_date looks, I am not using this
	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %d %Y')

	def summary(self):
		if(len(self.body)>100):
			self.body = self.body[:100]+" ..."
		return self.body
