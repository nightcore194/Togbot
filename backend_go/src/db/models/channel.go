package models

import (
	"gorm.io/gorm"
	"time"
)

type Channel struct {
	gorm.Model
	ID           uint64      `gorm:"primaryKey;autoIncrement:true"`
	Name         string      `gorm:"type:varchar(256);not null"`
	Description  string      `gorm:"type:text; null"`
	ServerID     uint64      `gorm:"null"`
	TypeID       uint64      `gorm:"not null"`
	CategoryID   uint64      `gorm:"null"`
	CreationDate time.Time   `gorm:"type:timestamp;default:CURRENT_TIMESTAMP;not null"`
	ChannelType  ChannelType `gorm:"not null"`
	Server       Server      `gorm:"foreignKey:ServerID;OnUpdate:CASCADE,OnDelete:CASCADE;"`
	Messages     []Message   `gorm:"foreignKey:ChannelID;OnUpdate:CASCADE,OnDelete:CASCADE;"`
}
