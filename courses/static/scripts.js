// Name: Dana Toribio
// Date: 4/15/14
// Filename: scripts.js
// Description: This is the scripts.js file which holds all the
// 		JavaScript/jQuery code to help with assisting in formatting
// 		TitanPlanner in areas that CSS cannot sufficiently format.

$(document).ready(function() {
	// formats the height of index.html's iframes to fill the window
	var calendarHeight = $(window).height() - $('#header').outerHeight();
	var contentHeight = $(window).height() - $('#logo').outerHeight();
	var timeslotWidth = ($('.time-slot').outerWidth() - 2);
	var hourslotWidth = ($('.hour-slot').outerWidth() - 2);
	$('#calendar').css('height', calendarHeight);

	// formats the height of the right iframe content
	var contentHeight = $(window).height() - $('#logo').outerHeight();
	$('#content').css('height', contentHeight);
	$('#left-page').css('height', $(window).height());
	$('#right-page').css('height', $(window).height());

	// formats the width of the time slots in the calendar
	var timeslotWidth = ($('.time-slot').outerWidth() - 2);
	$('.blank').css('width', hourslotWidth);

	// formats the width of the hour slots in the calendar
	var hourslotWidth = ($('.hour-slot').outerWidth() - 2);
	$('.week-day').css('width', timeslotWidth);

	// formats the height of the right iframe
	$('#right-page').css('height', $(window).height());
});


// Title: createCourseOverlay -----------------------------------------------------------------------------
// Description: This function creates & removes the Course overlay div 
// Pre-condition: course_days, start_time, end_time, course_subject, course_number, course_title, course_id
// Post-condition: 
//		- Does calculations and parsing on time values
//		- Appends HTML/CSS needed to do addition, positioning and removal of the course
function createCourseOverlay(course_days, start_time, end_time, course_subject, course_number, course_title, course_id) {
	// setting parameters into local variables
	var course_days = course_days;
	var course_id = course_id;
	var start_time = start_time;
	// parsing hour, min and AM/PM into strings with length of 2
	var start_hour = parseInt(start_time.substring(0, 2));
	var start_min = parseInt(start_time.substring(2, 4));
	var start_AMPM = start_time.substring(4, 6);

	// end time parameter setting and parsing of hour/min/AM/PM
	var end_time = end_time;
	var end_hour = end_time.substring(0, 2);
	var end_min = end_time.substring(2, 4);
	var end_AMPM = start_time.substring(4, 6);

	// calculations for time elapsed
	var time_elapsed = parseInt(end_time.substring(0, 4)) - parseInt(start_time.substring(0, 4));
	// ternary check for time elapsed
	var time_diff = time_elapsed > 60 ? time_elapsed - 40 : 55;

	// jQuery append data to create overlay div
	var append_data = '<a href="/remove/' + course_id + '/"><div class="course-listing" style="top: ' + start_min + 'px; height: ' + time_diff + 'px">' + start_time + '-' + end_time + '<hr />CPSC ' + course_number + '<br/>' + course_title + '</a></div>';

	// Scenarios: M, T, W, R, F, S, MW, TT, MWF, MTWTF
	// adds the append data to create the overlay div depending on the course day
	if (course_days == "Tu") {
		$('.T .' + start_hour + '.' + start_AMPM).append(append_data);
	} else if (course_days == "Th") {
		$('.R .' + start_hour + '.' + start_AMPM).append(append_data);
	} else if (course_days == "MW") {
		$('.M .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.W .' + start_hour + '.' + start_AMPM).append(append_data);
	} else if (course_days == "TT") {
		$('.T .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.R .' + start_hour + '.' + start_AMPM).append(append_data);
	} else if (course_days == "MWF") {
		$('.M .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.W .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.F .' + start_hour + '.' + start_AMPM).append(append_data);
	} else if (course_days == "MTWTF") {
		$('.M .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.T .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.W .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.R .' + start_hour + '.' + start_AMPM).append(append_data);
		$('.F .' + start_hour + '.' + start_AMPM).append(append_data);
	} else {
		$('.' + course_days + ' .' + start_hour + '.' + start_AMPM).append(append_data);
	}
};
// end createCourseOverlay -------------------------------------------------------------------------------