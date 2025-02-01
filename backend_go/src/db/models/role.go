package models

import (
	"gorm.io/gorm"
	"time"
)

type Role struct {
	gorm.Model
	ID            uint64     `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	CreationDate  time.Time  `gorm:"type:datetime;default:CURRENT_TIMESTAMP"`
	Name          string     `gorm:"type:varchar(255);not null"`
	Color         string     `gorm:"type:varchar(7);not null;default:'#FFFFFF'"`
	IsDisplayable bool       `gorm:"type:boolean;not null;default:True"`
	IsTaggable    bool       `gorm:"type:boolean;not null;default:False"`
	ServerID      uint64     `gorm:"type:bigint;not null"`
	Server        Server     `gorm:"foreignKey:ServerID;constraint:OnUpdate:CASCADE,OnDelete:CASCADE;"`
	Permission    Permission `gorm:"foreignKey:RoleID;OnUpdate:CASCADE,OnDelete:CASCADE;"`
	Users         []User     `gorm:"many2many:role_users;"`
}
