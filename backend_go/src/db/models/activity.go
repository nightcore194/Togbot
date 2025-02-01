package models

import (
	"gorm.io/gorm"
	"time"
)

type Activity struct {
	gorm.Model
	ID          uint64    `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	Description string    `gorm:"type:varchar(512);not null"`
	ServerID    uint64    `gorm:"type:bigint;not null"`
	CreatedAt   time.Time `gorm:"type:datetime;default:CURRENT_TIMESTAMP;not null"`
}
