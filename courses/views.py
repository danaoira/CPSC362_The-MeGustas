from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from courses.models import Course


def index(request):
	return render_to_response('index.html')

def display_all(request):
	course_list = Course.objects.all()
	context = { 'course_list': course_list}
	return render(request, 'display_all.html', context)

def calendar(request):
	list = Course.objects.filter(is_registered='True')
	context = { 'list': list}
	return render(request, 'calendar.html', context)

def add(request, pk):
	new = Course.objects.get(pk=pk)
	reg_list = Course.objects.filter(is_registered='True')
	for course in reg_list:
		old = course
		if (old == new):
			return HttpResponse('You have already selected this course.')
		if (old.days in new.days) or (new.days in old.days) or (old.days == new.days):
			if ( old.is_during(new) ):
				return HttpResponse('Error: \"'+str(new)+'\" not added due to time conflict with \"'+str(old)+'\" at '+old.start_time)
	new.is_registered = True
	new.save()
	msg = "Message text."
	#return reverse('add', args)
	return HttpResponseRedirect('/search-form/')

def remove(request, pk):
	course = Course.objects.get(pk=pk)
	course.is_registered = False
	course.save()
	msg = "Message text."
	#return reverse('add', args)
	return HttpResponseRedirect('/calendar/')


def search(request):
	if 'key' in request.GET and request.GET['key']:
		key = request.GET['key']
		list = Course.objects.filter(title__contains=key)
		# remember to pass back the radio button/column choice and change the line above
		context = {'list': list, 'key': key}
		return render(request, 'results.html', context)
	else:
		return HttpResponse('Please submit a search term.')

def search_form(request):
	return render(request, "search.html")

#def important_dates(request):
#	return render_to_response('important-dates.html')
