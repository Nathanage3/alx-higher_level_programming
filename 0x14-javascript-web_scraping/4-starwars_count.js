#!/usr/bin/node
const request = require("request");

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error("Usage: node 4-starwars_count.js <api_url>");
  process.exit(1);
}

const characterId = 18;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const filmsData = JSON.parse(body).results;
      const moviesWithWedge = filmsData.filter((film) =>
        film.characters.includes(
          `https://swapi-api.alx-tools.com/api/people/${characterId}/`
        )
      );
      console.log(moviesWithWedge.length);
    } catch (parseError) {
      console.error("Error parsing response:", parseError);
    }
  }
});
