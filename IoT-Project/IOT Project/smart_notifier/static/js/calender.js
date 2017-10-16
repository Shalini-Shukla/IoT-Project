$(document).ready(function(){
	$('button').click(function(){
		var date = $(this).text()
		alert(date)
		window.location.href = window.location.protocol + '/time_wise/'+ date.trim()
	})
})