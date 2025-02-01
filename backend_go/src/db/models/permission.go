package models

import "gorm.io/gorm"

type Permission struct {
	gorm.Model
	ID     uint64 `gorm:"type:bigint;primaryKey;autoIncrement:true"`
	RoleID uint64 `gorm:"type:bigint"`
	// Admin permission
	IsAdmin     bool `gorm:"type:boolean;default:false"`
	IsModerator bool `gorm:"type:boolean;default:false"`
	// Channel permission
	CanCreateChannel bool `gorm:"type:boolean;default:false"`
	CanReadChannel   bool `gorm:"type:boolean;default:false"`
	CanUpdateChannel bool `gorm:"type:boolean;default:false"`
	CanDeleteChannel bool `gorm:"type:boolean;default:false"`
	// Voice permission
	CanConnectChannel      bool `gorm:"type:boolean;default:false"`
	CanSpeakChannel        bool `gorm:"type:boolean;default:false"`
	CanUseWebcam           bool `gorm:"type:boolean;default:false"`
	CanMuteUser            bool `gorm:"type:boolean;default:false"`
	CanDisableSpeakersUser bool `gorm:"type:boolean;default:false"`
	CanThrowUser           bool `gorm:"type:boolean;default:false"`
	// Role permission
	CanCreateRole bool `gorm:"type:boolean;default:false"`
	CanReadRole   bool `gorm:"type:boolean;default:false"`
	CanUpdateRole bool `gorm:"type:boolean;default:false"`
	CanDeleteRole bool `gorm:"type:boolean;default:false"`
	// Category permission
	CanCreateCategory bool `gorm:"type:boolean;default:false"`
	CanReadCategory   bool `gorm:"type:boolean;default:false"`
	CanUpdateCategory bool `gorm:"type:boolean;default:false"`
	CanDeleteCategory bool `gorm:"type:boolean;default:false"`
	// User permission
	CanEditUser    bool `gorm:"type:boolean;default:false"`
	CanKickUser    bool `gorm:"type:boolean;default:false"`
	CanTimeoutUser bool `gorm:"type:boolean;default:false"`
	CanBanUser     bool `gorm:"type:boolean;default:false"`
	// Message permission
	CanSendMessage   bool `gorm:"type:boolean;default:false"`
	CanDeleteMessage bool `gorm:"type:boolean;default:false"`
	CanReadMessage   bool `gorm:"type:boolean;default:false"`
	// Log activity permission
	CanViewActivity bool `gorm:"type:boolean;default:false"`
}
