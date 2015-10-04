from __future__ import unicode_literals

from django.db import models

class page(models.Model):
	page_url=	models.CharField(max_length=500)
	page_title=	models.CharField(max_length=200)
	page_domain=	models.CharField(max_length=50)

class logo(models.Model):
	page_domain= models.ForeignKey(page,on_delete=models.CASCADE)
	logo_url=	models.CharField(max_length=500)

class pull(models.Model):
	#logo_url=	models.ForeignKey(logo,on_delete=models.CASCADE)
	page_url=	models.ForeignKey(page,on_delete=models.CASCADE)
	date_pulled=	models.DateTimeField('date pulled')


# Create your models here.
