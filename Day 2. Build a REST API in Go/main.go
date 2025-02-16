package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// game represents data about a record game
type game struct {
	ID string `json:"id"`
	Title string `json:"title"`
	Developer string `json:"developer"`
	Price float64 `json:"price"`
}

// Slice of games to fill in the data
var games = []game{
	{ID: "1", Title: "Mass Effect", Developer: "BioWare", Price: 50},
	{ID: "2", Title: "Fallout", Developer: "Obsidian Entertainment", Price: 30},
	{ID: "3", Title: "Outer Wilds", Developer: "Mobius Digital", Price: 20},
	{ID: "4", Title: "Civilization VI", Developer: "Firaxis Games", Price: 60},
}

// Get all games as JSON
func getGames(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, games)
}

// Get game by ID, return the 1st entry if games share same id
func getGameById(c *gin.Context) {
	id := c.Param("id")

	for _, val := range games {
		if val.ID == id {
			c.IndentedJSON(http.StatusOK, val)
			return
		}
	}
	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "game not found"})
}

// Add a game from the JSON in the request body
func postGames (c *gin.Context) {
	var newGame game

	// Bind the received JSON to newGame
	if err := c.BindJSON(&newGame); err != nil {
		return
	}

	// Add new game to the slice
	games = append(games, newGame)
	c.IndentedJSON(http.StatusCreated, newGame)
}

func main(){
	router := gin.Default()
	router.GET("/games", getGames)
	router.GET("/games/:id", getGameById)
	router.POST("/games", postGames)

	router.Run("localhost:8080")
}