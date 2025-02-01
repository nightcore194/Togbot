package models

import (
	"gorm.io/gorm"
	"time"
)

type User struct {
	gorm.Model
	ID                  uint64                  `gorm:"type:bigint;primaryKey;autoIncrement:true;not null"`
	Email               string                  `gorm:"type:varchar(128);unique;not null"`
	Username            string                  `gorm:"type:varchar(64);unique;not null"`
	FirstName           string                  `gorm:"type:varchar(64);unique;null"`
	SecondName          string                  `gorm:"type:varchar(64);unique;null"`
	DisplayName         string                  `gorm:"type:varchar(128);unique;null"`
	Password            string                  `gorm:"type:varchar(512);not null"`
	ProfilePhoto        string                  `gorm:"type:varchar(256);null"`
	ProfilePhotoPreview string                  `gorm:"type:varchar(256);null"`
	BackgroundPhoto     string                  `gorm:"type:varchar(256);null"`
	About               string                  `gorm:"type:text;null"`
	Phone               string                  `gorm:"type:varchar(16);null"`
	Address             string                  `gorm:"type:varchar(128);null"`
	Birthday            time.Time               `gorm:"type:date;null"`
	CreationDate        time.Time               `gorm:"type:timestamp;null;default:CURRENT_TIMESTAMP"`
	IsConfirmed         bool                    `gorm:"type:boolean;not null"`
	Is2faEnabled        bool                    `gorm:"type:boolean;not null"`
	OTP                 TwoFactorAuthentication `gorm:"foreignKey:UserID;OnUpdate:CASCADE,OnDelete:SET NULL;"`
	Servers             []Server                `gorm:"many2many:servers_users;order_by:CreationDate DESC;OnUpdate:CASCADE,OnDelete:CASCADE"`
}
