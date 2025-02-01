package models

import (
	"gorm.io/gorm"
	"time"
)

type Category struct {
	gorm.Model
	ID           uint64    `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	CreationDate time.Time `gorm:"type:timestamp;default:CURRENT_TIMESTAMP;"`
	Name         string    `gorm:"type:varchar(256);not null"`
	ServerID     uint64    `gorm:"type:bigint;"`
	Channels     []Channel `gorm:"foreignKey:CategoryID;OnUpdate:CASCADE,OnDelete:CASCADE;"`
}
