from django.db import models

# Create your models here.

class CurrentView(models.Model):
	# represents our current calendar CurrentView
	calendar_id = modesls.CharField(max_length=200)

	def get_current_courses(self):
		# returns a list of registered courses
		return Course.objects.filter(is_registered='True')

	def register_course(self, Course):
		# registers the selected course

	def search_courses(self, keyword, field):
		# searches through the list of courses
		# given a field and a keyword
	


class Course(models.Model): 
	course_title = models.CharField(max_length=200)
	course_num = models.CharField(max_length=200)
	prof_name = models.CharField(max_length=200)
	room_num = models.CharFied(max_field=200)
	start_time = models.TimeField() # not sure about parameters
	end_time = models.TimeField()
	days = models.CharField(max_length=5) # MWF, MW, TT, S
	is_registered = models.BooleanField(default=False)

	def __unicode__(self): 
		return self.course_title

