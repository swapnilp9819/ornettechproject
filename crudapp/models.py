from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import User

# Create your models here.

class News(models.Model):

    categorychoices = (
        ('',''),
        ('Politics','Politics'),
        ('Education','Education'),
        ('Health','Health'),
        ('Business','Business'),
        ('Sports','Sports'),
        ('Entertainment','Entertainment'),
        ('Technology','Technology'),
        ('Science','Science'),
        ('Travel','Travel'),
        ('Miscellaneous','Miscellaneous')
    )

    regionchoices = (
        ('',''),
        ('National','National'),
        ('International','International')
    )

    statuschoices = (
        ('',''),
        ('Draft','Draft'),
        ('Approved','Approved'),
        ('Published','Published')
    )

    news_id = models.AutoField(primary_key=True)
    news_title = models.CharField(max_length=100, null=False)
    news_description = models.TextField(max_length=500)
    news_banner_image = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=100, default='', choices=categorychoices)
    region = models.CharField(max_length=100, default='', choices=regionchoices)
    status = models.CharField(max_length=100, default='', choices=statuschoices)
    language = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    createdon = models.DateField(auto_now=True)
    createdby = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.news_title