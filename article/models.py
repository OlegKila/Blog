from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=255)
	content = models.TextField()
	slug = models.SlugField(max_length=150, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article_detail', kwargs={'slug':self.slug})

class Comment(models.Model):
	comment = models.TextField()
	comment_article = models.ForeignKey(Article)

	def get_absolute_url(self):
		return reverse('article_detail', kwargs={'slug':self.comment_article.slug})