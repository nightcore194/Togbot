package models

import (
	"gorm.io/gorm"
	"time"
)

type Server struct {
	gorm.Model
	ID           uint64     `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	CreationDate time.Time  `gorm:"type:timestamp;default:CURRENT_TIMESTAMP;not null"`
	Name         string     `gorm:"type:varchar(256);not null"`
	Description  string     `gorm:"type:text;null"`
	PhotoUrl     string     `gorm:"type:varchar;null"`
	Users        []User     `gorm:"many2many:server_users"`
	Role         []Role     `gorm:"foreignKey:ServerID;OnDelete:CASCADE,OnUpdate:CASCADE;"`
	Category     []Category `gorm:"foreignKey:ServerID;OnDelete:CASCADE,OnUpdate:CASCADE;"`
	Channel      []Channel  `gorm:"foreignKey:ServerID;OnDelete:CASCADE,OnUpdate:CASCADE;"`
	Activity     []Activity `gorm:"foreignKey:ServerID;OnDelete:CASCADE;"`
}
