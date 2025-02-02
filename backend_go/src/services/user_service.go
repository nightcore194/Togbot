package services

import (
	"backend_go/src/db/dto"
	"backend_go/src/db/models"
	"backend_go/src/repositories"
	"errors"
)

type UserService struct {
	UserRepo repositories.UserRepository
}

func NewUserService(repo repositories.UserRepository) UserService {
	return UserService{UserRepo: repo}
}

// Its exmaple, TODO
func (service *UserService) CreateUser(request dto.UserDTO) (models.User, error) {
	user := models.User{FirstName: request.FirstName, Email: request.Email}
	createdUser, err := service.UserRepo.CreateUser(user)
	if err != nil {
		return models.User{}, err
	}
	return createdUser, nil
}

// Its exmaple, TODO
func (service *UserService) GetUserByID(id string) (models.User, error) {
	user, err := service.UserRepo.FindUserByID(id)
	if err != nil {
		return models.User{}, errors.New("user not found")
	}
	return user, nil
}
