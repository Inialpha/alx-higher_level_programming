$.getJSON("https://swapi-api.alx-tools.com/api/films/?format=json", function (data) {
	for (let film of data.results) {
		$('UL#list_movies').append(`<li>${film.title}</li>`)
	}
});

