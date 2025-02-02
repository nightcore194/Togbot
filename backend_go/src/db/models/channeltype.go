package models

import "gorm.io/gorm"

type ChannelType struct {
	gorm.Model
	ID          uint64 `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	Name        string `gorm:"type:varchar(256);not null"`
	Description string `gorm:"type:varchar(256);null"`
}
