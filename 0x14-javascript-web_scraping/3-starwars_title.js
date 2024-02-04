#!/usr/bin/node
const request = require("request");

const movieId = process.argv[2];

if (!movieId) {
  console.error("Usage: node 3-starwars_title.js <movie_id>");
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      const movieData = JSON.parse(body);
      console.log(`${movieData.title}`);
    } catch (parseError) {
      console.error("Error parsing response:", parseError);
    }
  }
});
