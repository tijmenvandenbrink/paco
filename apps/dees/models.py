from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
	REASONS = (
				('Nieuwe klant', 'Nieuwe klant'), 
				('Bestaande klant', 'Bestaande klant'),
				('Interne opdracht', 'Interne opdracht'), 
				('Backfill', 'Backfill'),
			)

	title = models.CharField(max_length=255, 
							help_text="Please specify the title of the project")
	reason = models.CharField(max_length=16, choices=REASONS,
								help_text="Please specify the reason")
	location = models.CharField(max_length=128,
								help_text="Please specify the location")
	project_manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
										related_name="project_mgr_of_project",
										help_text="Please specify the project manager")
	account_manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL,
										related_name="account_mgr_of_project",
										help_text="Please specify the account manager")
	project_id = models.CharField(max_length=32,
							help_text="Please specify the SO or PID number")

	def __unicode__(self):
		return self.title


class Skill(models.Model):
	title = models.CharField(max_length=255,
							help_text="Please sepcify the name of the skill")
	description = models.TextField(help_text="Please specify a description of the skill")

	def __unicode__(self):
		return self.title


class Task(models.Model):
	WINDOWS = (
				('Office Hours', 'Office Hours'),
				('Extended Office Hours', 'Extended Office Hours'), 
				('Out of Office Hours', 'Out of Office Hours'),
			)

	title = models.CharField(max_length=255,
							help_text="Please specify the title of the task")
	project = models.ForeignKey(Project)
	description = models.TextField(help_text="Please specify a description of the task that needs to be performed")
	prework = models.TextField(help_text="Please specify the prework that needs to be done")
	scope = models.TextField(help_text="Please specify the scope of work")
	skills = models.ManyToManyField(Skill)
	duration = models.FloatField(help_text="Please specify the number of hours this task will take")
	window = models.CharField(max_length=255, choices=WINDOWS,
								help_text="Please specify when this task needs to be performed")

	def __unicode__(self):
		return self.title

class ResourceRequest(models.Model):
	requester = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
	project = models.ForeignKey(Project)
	task = models.ForeignKey(Task)
	request_date = models.DateTimeField(datetime.now())
	start_date = models.DateTimeField('start date',
								help_text="Please specify the start date")
	end_date = models.DateTimeField('end date',
								help_text="Please specify the end date")

	def __unicode__(self):
		return self.id