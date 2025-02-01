package engine

// For migration use Atlas
import (
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
	"log"
	"sync"
	"time"
)

type DBManager struct {
	DB *gorm.DB
}

func NewDBManager(DB_URL string) (*DBManager, error) {
	// Initialize the GORM connection pool with the provided PostgreSQL URL
	db, err := gorm.Open(postgres.Open(DB_URL), &gorm.Config{})
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

// DBSessionManager represents the context for managing database sessions.
type DBSessionManager struct {
	db     *gorm.DB
	mu     sync.Mutex
	active bool
}

// NewDBSessionManager creates a new session manager
func NewDBSessionManager(db *gorm.DB) *DBSessionManager {
	return &DBSessionManager{
		db: db,
	}
}

// Begin starts a new database transaction
func (sm *DBSessionManager) Begin() *gorm.DB {
	sm.mu.Lock()
	defer sm.mu.Unlock()

	if sm.active {
		log.Fatal("Session already active")
		return nil
	}

	tx := sm.db.Begin()
	sm.active = true
	return tx
}

// Commit commits the current transaction
func (sm *DBSessionManager) Commit(tx *gorm.DB) error {
	if tx == nil {
		return nil
	}

	if err := tx.Commit().Error; err != nil {
		return err
	}

	sm.mu.Lock()
	defer sm.mu.Unlock()
	sm.active = false
	return nil
}

// Rollback rolls back the current transaction
func (sm *DBSessionManager) Rollback(tx *gorm.DB) error {
	if tx == nil {
		return nil
	}

	if err := tx.Rollback().Error; err != nil {
		return err
	}

	sm.mu.Lock()
	defer sm.mu.Unlock()
	sm.active = false
	return nil
}

// Example usage of DBManager and DBSessionManager
func main() {
	DB_URL := "postgres://user:password@localhost:5432/mydb"
	manager, err := NewDBManager(DB_URL)
	if err != nil {
		log.Fatalf("Error creating DBManager: %v", err)
	}
	defer manager.Close()

	// Get the underlying GORM DB instance
	db := manager.Engine()

	// Create a new session manager
	sessionManager := NewDBSessionManager(db)

	// Start a new transaction session
	tx := sessionManager.Begin()
	if tx == nil {
		log.Fatalf("Failed to start a transaction")
	}

	// Perform some database operations inside the transaction
	if err := tx.Create(&SomeModel{Field: "value"}).Error; err != nil {
		log.Printf("Error inserting record: %v", err)
		if rollbackErr := sessionManager.Rollback(tx); rollbackErr != nil {
			log.Fatalf("Error rolling back transaction: %v", rollbackErr)
		}
	} else {
		// Commit the transaction if everything is fine
		if commitErr := sessionManager.Commit(tx); commitErr != nil {
			log.Fatalf("Error committing transaction: %v", commitErr)
		}
	}
}
