package models

import (
	"gorm.io/gorm"
	"time"
)

type Session struct {
	gorm.Model
	ID           uint64    `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	Hash         string    `gorm:"type:varchar(256);not null"`
	Expires      time.Time `gorm:"type:timestamp;not null"`
	CreationDate time.Time `gorm:"type:timestamp;not null"`
	UserID       uint64    `gorm:"type:bigint;not null"`
	User         User      `gorm:"foreignKey:UserID;onDelete:CASCADE"`
}
