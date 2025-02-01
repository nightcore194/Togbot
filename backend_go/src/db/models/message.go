package models

import (
	"gorm.io/gorm"
	"time"
)

// TODO
type Message struct {
	gorm.Model
	ID           uint64    `gorm:";primaryKey;autoIncrement:true"`
	CreationDate time.Time `gorm:"type:timestamp;default:CURRENT_TIMESTAMP;not null"`
	EditDate     time.Time `gorm:"default:CURRENT_TIMESTAMP;autoUpdateTime:milli;not null"`
}
