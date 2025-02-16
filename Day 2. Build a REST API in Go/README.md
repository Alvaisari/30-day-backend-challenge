# Games API

A simple REST API written in Go using the Gin framework. It provides endpoints for managing a collection of games.

## Features

- **GET /games:** Retrieves a list of all games in JSON format.
- **GET /games/:id:** Retrieves a specific game by its ID.
- **POST /games:** Adds a new game to the collection.  The game data is expected in JSON format in the request body.