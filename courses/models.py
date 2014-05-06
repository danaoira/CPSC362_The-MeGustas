# TitanPlanner
# 4/15/2014
# Kinjal Chatterjee
# models.py
# This file is the database object relational model implementation using
# the django object/model library. This file implements the control and 
# entity classes from the design docuementation.
import time
from django.db import models

class Course(models.Model):
	title = models.CharField(max_length=200)
	number = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	prof = models.CharField(max_length=200)
	room = models.CharField(max_length=200)
	start_time = models.CharField(max_length=200)
	end_time = models.CharField(max_length=200)
	days = models.CharField(max_length=5) # MWF, MW, TT, S
	is_registered = models.BooleanField(default=False)
	
	@classmethod
	def init(cls):
		c = Course(title="Intro to Programming", number="120", subject="Computer Science", prof="Moore", room="202", start_time="0830AM", end_time="0945AM", days="Tu")
		c.save()
		c = Course(title="Intro to Programming", number="120", subject="Computer Science", prof="Ghadami", room="300", start_time="0830AM", end_time="0945AM", days="Th")
		c.save()
		c = Course(title="Programming Concepts", number="121", subject="Computer Science", prof="Ahmadnia", room="202", start_time="0100PM", end_time="0150PM", days="TT")
		c.save()
		c = Course(title="Programming Concepts", number="121", subject="Computer Science", prof="Niyomtham", room="104", start_time="0700PM", end_time="0750PM", days="TT")
		c.save()
		c = Course(title="Data Structures Concepts", number="131", subject="Computer Science", prof="Torres", room="110B", start_time="0100PM", end_time="0215PM", days="TT")
		c.save()
		c = Course(title="Data Structures Concepts", number="131", subject="Computer Science", prof="Molodowitch", room="300", start_time="0400PM", end_time="0515PM", days="MW")
		c.save()
		c = Course(title="Visual C# Programming", number="223N", subject="Computer Science", prof="Holliday", room="104", start_time="1230PM", end_time="0220PM", days="M")
		c.save()
		c = Course(title="Visual C# Programming", number="223N", subject="Computer Science", prof="Holliday", room="104", start_time="1230PM", end_time="0220PM", days="W")
		c.save()
		c = Course(title="Python Programming", number="223P", subject="Computer Science", prof="Shafae", room="101", start_time="0400PM", end_time="0550PM", days="M")
		c.save()
		c = Course(title="Comp Org & Assembly Lang", number="240", subject="Computer Science", prof="Holliday", room="110B", start_time="1000AM", end_time="1150AM", days="Tu")
		c.save()
		c = Course(title="Comp Org & Assembly Lang", number="240", subject="Computer Science", prof="Shulman", room="300", start_time="0800PM", end_time="0950PM", days="M")
		c.save()
		c = Course(title="Software Dev w/ Open Source", number="254", subject="Computer Science", prof="Murphy", room="300", start_time="1000AM", end_time="1150AM", days="M")
		c.save()
		c = Course(title="Software Dev w/ Open Source", number="254", subject="Computer Science", prof="Turner", room="408", start_time="0730PM", end_time="0920PM", days="Th")
		c.save()
		c = Course(title="Tech Writing for Comp Sci", number="311", subject="Computer Science", prof="Falconer", room="300", start_time="0230PM", end_time="0345PM", days="MW")
		c.save()
		c = Course(title="Tech Writing for Comp Sci", number="311", subject="Computer Science", prof="Elizondo", room="109", start_time="1000AM", end_time="1115AM", days="MW")
		c.save()
		c = Course(title="The Computer Impact", number="313", subject="Computer Science", prof="Zhang", room="102B", start_time="0230PM", end_time="0345PM", days="TT")
		c.save()
		c = Course(title="The Computer Impact", number="313", subject="Computer Science", prof="Mohammad", room="300", start_time="1130AM", end_time="1245PM", days="TT")
		c.save()
		c = Course(title="Algorithm Engineering", number="335", subject="Computer Science", prof="Wortman", room="202", start_time="0100PM", end_time="0215PM", days="MW")
		c.save()
		c = Course(title="Algorithm Engineering", number="335", subject="Computer Science", prof="Wortman", room="202", start_time="0700PM", end_time="0815PM", days="TT")
		c.save()
		c = Course(title="Operating System Concepts", number="351", subject="Computer Science", prof="Tian", room="204", start_time="0500PM", end_time="0615PM", days="MW")
		c.save()
		c = Course(title="Operating System Concepts", number="351", subject="Computer Science", prof="Tian", room="204", start_time="0200PM", end_time="0215PM", days="TT")
		c.save()
		c = Course(title="Software Engineering", number="362", subject="Computer Science", prof="Bagheri", room="408", start_time="0500PM", end_time="0650PM", days="TT")
		c.save()
		c = Course(title="Software Engineering", number="362", subject="Computer Science", prof="Choi", room="408", start_time="1000AM", end_time="1150AM", days="MW")
		c.save()
		print("courses added.")

	@classmethod
	def get_all(cls):
		# returns a list of registered courses
		return Course.objects.all()
	
	@classmethod
	def get_registered(cls):
		# returns a list of registered courses
		return Course.objects.filter(is_registered='True')

	@classmethod
	def check_conflict(cls, c):
		# Checks for scheduling conflicts
		old = c
		print('old = '+str(old))
		registered_list = get_registered()

		for course in list:
			new = course
			print('new ='+str(new))
			if (old.days == new.days):
				print('same days')
				if( old.is_during(new) ): 
					return 'True'
		return 'False'

	def is_during(self, course2):
		# checks for timing conflict
		a_start = time.strptime(self.start_time, "%I%M%p")
		a_end = time.strptime(self.end_time, "%I%M%p")
		b_start = time.strptime(course2.start_time, "%I%M%p")
		b_end = time.strptime(course2.end_time, "%I%M%p")
		if ( a_start >= b_start ):
			if ( a_start <= b_end ):
				return 'True'
		if ( b_start >= a_start ):
			if ( b_start <= a_end ):
				return 'True'		
		else:
			return 'False'
	
	def __unicode__(self):  # Python 3: def __str__(self):
		return self.title
	