from django.db import models
class Interests(models.Model):
	name = models.TextField(max_length=200)
	created_at = models.DateField()
	class Meta:
		db_table = 'interests'
class Users(models.Model):
	first_name = models.TextField(max_length=200)
	last_name = models.TextField(max_length=200)
	age = models.IntegerField()
	created_at = models.DateField()
	occupation = models.TextField(max_length=200)
	interest = models.ForeignKey(Interests)
	class Meta:
		db_table = 'users'