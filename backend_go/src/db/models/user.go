package models

import (
	"backend_go/src/db/dto"
	"gorm.io/gorm"
	"time"
)

type User struct {
	gorm.Model
	ID                  uint64                  `gorm:"type:bigint;primaryKey;autoIncrement:true;not null"`
	Email               string                  `gorm:"type:varchar(256);unique;not null"`
	Username            string                  `gorm:"type:varchar(64);unique;not null"`
	FirstName           string                  `gorm:"type:varchar(64);unique;null"`
	SecondName          string                  `gorm:"type:varchar(64);unique;null"`
	DisplayName         string                  `gorm:"type:varchar(64);unique;null"`
	Password            string                  `gorm:"type:char(128);not null"`
	SecretKey           string                  `gorm:"type:char(128);unique;null"`
	ProfilePhoto        string                  `gorm:"type:varchar(256);null"`
	ProfilePhotoPreview string                  `gorm:"type:varchar(256);null"`
	BackgroundPhoto     string                  `gorm:"type:varchar(256);null"`
	About               string                  `gorm:"type:text;null"`
	Phone               string                  `gorm:"type:varchar(16);null"`
	Country             string                  `gorm:"type:varchar(16);null"`
	Birthday            time.Time               `gorm:"type:date;null"`
	CreationDate        time.Time               `gorm:"type:timestamp;null;default:CURRENT_TIMESTAMP"`
	IsConfirmed         bool                    `gorm:"type:boolean;not null"`
	Is2faEnabled        bool                    `gorm:"type:boolean;not null"`
	OTP                 TwoFactorAuthentication `gorm:"foreignKey:UserID;OnUpdate:CASCADE,OnDelete:SET NULL;"`
}

// ConvertToDTO converts a User entity to a UserDTO
func (user *User) ConvertToDTO() dto.UserDTO {
	return dto.UserDTO{
		ID:                  user.ID,
		Email:               user.Email,
		Username:            user.Username,
		FirstName:           user.FirstName,
		SecondName:          user.SecondName,
		DisplayName:         user.DisplayName,
		ProfilePhoto:        user.ProfilePhoto,
		ProfilePhotoPreview: user.ProfilePhotoPreview,
		BackgroundPhoto:     user.BackgroundPhoto,
		About:               user.About,
		Phone:               user.Phone,
		Country:             user.Country,
		Birthday:            user.Birthday,
		CreationDate:        user.CreationDate,
		IsConfirmed:         user.IsConfirmed,
		Is2faEnabled:        user.Is2faEnabled,
	}
}
