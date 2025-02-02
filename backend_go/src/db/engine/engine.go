package engine

// For migration use Atlas
import (
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"time"
)

type DBManager struct {
	DB *gorm.DB
}

func NewDBManager(DbUrl string) (*DBManager, error) {
	// Initialize the GORM connection pool with the provided PostgreSQL URL
	db, err := gorm.Open(postgres.Open(DbUrl), &gorm.Config{})
	if err != nil {
		return nil, err
	}

	// Setup connection pooling
	sqlDB, err := db.DB()
	if err != nil {
		return nil, err
	}

	// Connection pool settings
	sqlDB.SetMaxIdleConns(100)
	sqlDB.SetMaxOpenConns(100)
	sqlDB.SetConnMaxLifetime(1 * time.Hour)

	return &DBManager{DB: db}, nil
}

// Engine returns the underlying GORM DB object
func (dm *DBManager) Engine() *gorm.DB {
	return dm.DB
}

// Close closes the DB connection
func (dm *DBManager) Close() error {
	sqlDB, err := dm.DB.DB()
	if err != nil {
		return err
	}
	return sqlDB.Close()
}

func (dm *DBManager) GetSession() *gorm.DB { return dm.DB.Session(&gorm.Session{}) }
