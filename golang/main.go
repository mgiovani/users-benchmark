package main

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"time"

	"github.com/gofrs/uuid"
	_ "github.com/lib/pq"
)

type User struct {
	Name  string `json:"name"`
	Email string `json:"email"`
}

const (
	host     = "localhost"
	port     = 5432
	user     = "postgres"
	password = "abc123"
	dbname   = "users_benchmark"
)

func openDBConnection() *sql.DB {
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s "+
		"password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		panic(err)
	}

	err = db.Ping()
	if err != nil {
		panic(err)
	}

	return db
}

func usersPostHandler(w http.ResponseWriter, r *http.Request) {
	log.Print("Running PostHandler...")
	db := openDBConnection()

	var user User
	err := json.NewDecoder(r.Body).Decode(&user)
	if err != nil {
		http.Error(w, err.Error(), http.StatusBadRequest)
		return
	}

	sqlStatement := `INSERT INTO user_golang (name, email, created, id) VALUES ($1, $2, $3, $4)`
	created := time.Now()
	id := uuid.Must(uuid.NewV4())
	_, err = db.Exec(sqlStatement, user.Name, user.Email, created, id)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		panic(err)
	}

	w.WriteHeader(http.StatusOK)
	defer db.Close()
}

func main() {
	log.Print("Running API...")
	http.HandleFunc("/", usersPostHandler)
	log.Fatal(http.ListenAndServe(":8000", nil))
}
