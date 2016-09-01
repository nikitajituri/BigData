from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    count = models.IntegerField()
    excerpt_post_id = models.IntegerField(blank=True, null=True)
    wiki_post_id = models.IntegerField(blank=True, null=True)
    
    
# Create your models here.
class UserStats(models.Model):
    tag = models.ForeignKey(Tag)
    year = models.IntegerField()
    count = models.IntegerField()
     
# Create your models here.
class PostStats(models.Model):
    tag = models.ForeignKey(Tag)
    year = models.IntegerField()
    total_questions = models.IntegerField()
    total_answers = models.IntegerField()
    accepted_answers = models.IntegerField()
    deleted_questions = models.IntegerField()
    closed_questions = models.IntegerField()
    score = models.IntegerField()
    
    
# Create your models here.
class TopQ(models.Model):
    tag = models.ForeignKey(Tag)
    viewcount = models.IntegerField()
    question_id = models.IntegerField()
    title = models.CharField(max_length=500)
    tag1 = models.CharField(max_length=100, blank=True, null=True)
    tag2 = models.CharField(max_length=100, blank=True, null=True)
    tag3 = models.CharField(max_length=100, blank=True, null=True)
    tag4 = models.CharField(max_length=100, blank=True, null=True)
    tag5 = models.CharField(max_length=100, blank=True, null=True)

# Create your models here.
class TopUsers(models.Model):
    tag = models.ForeignKey(Tag)
    user_id = models.IntegerField()
    questioncount = models.IntegerField()
    displayname = models.CharField(max_length=500)
    urlpicture = models.CharField(max_length=100, blank=True, null=True)

# Create your models here.
class topusersnew(models.Model):
    tag = models.ForeignKey(Tag)
    user_id = models.IntegerField()
    questioncount = models.IntegerField()
    displayname = models.CharField(max_length=500)
    urlpicture = models.CharField(max_length=100, blank=True, null=True)

# Create your models here.
class TopU(models.Model):
    tag = models.ForeignKey(Tag)
    user_id = models.IntegerField()
    questioncount = models.IntegerField()
    displayname = models.CharField(max_length=500)
    urlpicture = models.CharField(max_length=100, blank=True, null=True)



