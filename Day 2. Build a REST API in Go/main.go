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
	Price string `json:"price"`
}

// Slice of games to fill in the data
var games = []game{
	{ID: "1", Title: "Mass Effect", Developer: "BioWare", Price: "50"},
	{ID: "2", Title: "Fallout", Developer: "Obsidian Entertainment", Price: "30"},
	{ID: "3", Title: "Outer Wilds", Developer: "Mobius Digital", Price: "20"},
	{ID: "4", Title: "Civilization VI", Developer: "Firaxis Games", Price: "60"},
}

// Get all games as JSON
func getGames(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, games)
}

func main(){
	router := gin.Default()
	router.GET("/games", getGames)

	router.Run("localhost:8080")
}