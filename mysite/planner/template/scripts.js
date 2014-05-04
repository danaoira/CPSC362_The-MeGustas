// Name: Dana Toribio
// Date: 4/15/14
// Filename: scripts.js
// Description: This is the scripts.js file which holds all the
// 		JavaScript/jQuery code to help with assisting in formatting
// 		TitanPlanner in areas that CSS cannot sufficiently format.

$(document).ready(function() {
	// formats the height of index.html's iframes to fill the window
	$("iframe").height($(window).height());
	//$(".time-slot").width($(window).width(timeslot-width);
});

// function iframeResize() {
// 	description: resizes iframe heights to span the entire height of
// 		the window
// 	triggers: document.ready/onPageLoad, onWindowResize
// }

// function weekdayResize() {
// 	description: resizes the width of the weekday slots
// 	calculation: (window.width() - 45px) / 7
// 	selectors affected: ".week-day"
// }

// function calendarSlotResize() {
// 	description: resizes the width of the calendar slots
// 	calculation: (window.width() - 45px) / 7
// 	selectors affected: ".hour-slot"
// }

// function calendarResize() {
// 	description: resizes the height of the calendar to span the
// 		entire height of the window
// 	calculation: (window).height() = 100%
// 	triggers: document.ready/onPageLoad, onWindowResize
// }