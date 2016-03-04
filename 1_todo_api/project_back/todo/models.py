from django.db import models
import uuid
from django.utils import timezone 
from django.contrib.auth.models import User 


# Create your models here.
class Profile(models.Model):
	name = models.OneToOneField(User)
	token = models.UUIDField(default=uuid.uuid4)


class Todos(models.Model):
	content = models.TextField()
	user_id = models.ForeignKey(Profile)
	created_date = models.DateTimeField(null = True)
	updated_date = models.DateTimeField(null = True)
	finished = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.updated_at = timezone.now()
		if not self.id:
			self.created_at = timezone.now()
		super(Todos,self).save(*args,**kwargs)

	def to_json(self):
		return {
			'content': self.content,
			'finished': self.finished,
		}


