$('DIV#toggle_header').addClass('red');

$('DIV#toggle_header').on('click', function () {
	if ($(this).hasClass('red')) {
		$(this).removeClass('red').addClass('green');
	} else if ($(this).hasClass('green')) {
		$(this).removeClass('green').addClass('red');
	}
});
