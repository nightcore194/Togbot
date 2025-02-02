package controllers

import (
	"backend_go/src/services"
)

type AuthController struct {
	AuthService services.UserService
}
