package dto

import (
	"time"
)

type UserDTO struct {
	ID                  uint64    `json:"id"`
	Email               string    `json:"email"`
	Username            string    `json:"username"`
	FirstName           string    `json:"first_name,omitempty"`
	SecondName          string    `json:"second_name,omitempty"`
	DisplayName         string    `json:"display_name,omitempty"`
	ProfilePhoto        string    `json:"profile_photo,omitempty"`
	ProfilePhotoPreview string    `json:"profile_photo_preview,omitempty"`
	BackgroundPhoto     string    `json:"background_photo,omitempty"`
	About               string    `json:"about,omitempty"`
	Phone               string    `json:"phone,omitempty"`
	Country             string    `json:"country,omitempty"`
	Birthday            time.Time `json:"birthday,omitempty"`
	CreationDate        time.Time `json:"creation_date"`
	IsConfirmed         bool      `json:"is_confirmed"`
	Is2faEnabled        bool      `json:"is_2fa_enabled"`
}
