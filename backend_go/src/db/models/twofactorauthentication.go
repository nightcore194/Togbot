package models

import "gorm.io/gorm"

type TwoFactorAuthentication struct {
	gorm.Model
	ID        uint64 `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	SecretKey string `gorm:"type:varchar(512);unique;not null"`
	UserID    uint64 `gorm:"type:bigint;not null"`
}
