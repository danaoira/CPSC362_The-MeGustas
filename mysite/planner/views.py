from django.shortcuts import render

# Create your views here.

def index(request):
	# main page
	template = loader.get_template('index.html')
	context = RequestContext( request, {

		})
	return HttpResponse(template.render(context))

def current_calendar_view(request):
	current_courses_list = get_current_courses()
	template = loader.get_template('current.html')
	context = RequestContext(request, {
			'current_courses_list' : current_courses_list,
		})
	return HttpResponse(template.render(context))

def register_course(request):
	# add course to current calendar view

def search(request):
	# view that represents the search page
	# has at least one field for inputting keywords

def search_results(request):
	# view that represents the search results page
	# has options to filter by attributes

def export(request):
	# view to represent the page containing export options

def dates(request):
	# this view displays holidasy and important events

def save(request):
	# this view allows the current calendar to be saved by the calendar

def feedback(request):
	# this view provides the feedback form functionality