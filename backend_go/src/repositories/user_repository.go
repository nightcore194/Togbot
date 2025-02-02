package repositories

import (
	"backend_go/src/db/models"
	"gorm.io/gorm"
)

type UserRepository struct {
	DB *gorm.DB
}

// NewUserRepository initializes the repository
func NewUserRepository(db *gorm.DB) UserRepository {
	return UserRepository{DB: db}
}

// CreateUser creates a new user in the database
func (repo *UserRepository) CreateUser(user models.User) (models.User, error) {
	if err := repo.DB.Create(&user).Error; err != nil {
		return models.User{}, err
	}
	return user, nil
}

// FindUserByID finds a user by their ID
func (repo *UserRepository) FindUserByID(id string) (models.User, error) {
	var user models.User
	if err := repo.DB.First(&user, id).Error; err != nil {
		return models.User{}, err
	}
	return user, nil
}
