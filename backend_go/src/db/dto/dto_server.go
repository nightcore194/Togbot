package dto

import (
	"time"
)

// ServerDTO represents the Data Transfer Object for the Server model
type ServerDTO struct {
	ID           uint64    `json:"id"`
	CreationDate time.Time `json:"creation_date"`
	Name         string    `json:"name"`
	Description  string    `json:"description,omitempty"`
	PhotoUrl     string    `json:"photo_url,omitempty"`
}
