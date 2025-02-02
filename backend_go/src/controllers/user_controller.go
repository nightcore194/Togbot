package controllers

import (
	"backend_go/src/db/dto"
	"backend_go/src/services"
	"github.com/gin-gonic/gin"
	"net/http"
)

type UserController struct {
	UserService services.UserService
}

// NewUserController initializes the controller
func NewUserController(service services.UserService) *UserController {
	return &UserController{UserService: service}
}

func (ctrl *UserController) CreateUser(c *gin.Context) {
	var user dto.UserDTO
	if err := c.ShouldBindJSON(&user); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	createdUser, err := ctrl.UserService.CreateUser(user)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, createdUser)
}

// GetUser returns a user by ID
func (ctrl *UserController) GetUser(c *gin.Context) {
	id := c.Param("id")
	user, err := ctrl.UserService.GetUserByID(id)
	if err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": err.Error()})
		return
	}

	c.JSON(http.StatusOK, user)
}
