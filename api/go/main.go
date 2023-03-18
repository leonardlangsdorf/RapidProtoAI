package main

import (
	"encoding/json"
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/graph-gophers/graphql-go"
	"github.com/graph-gophers/graphql-go/relay"
)

type message struct {
	Text string `json:"message"`
}

func main() {
	router := mux.NewRouter()

	router.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		message := message{Text: "Hello, World!"}
		json.NewEncoder(w).Encode(message)
	})

	schema := `
		type Query {
			hello(name: String!): String!
		}
	`
	resolver := &Resolver{}

	s, err := graphql.ParseSchema(schema, resolver)
	if err != nil {
		log.Fatal(err)
	}

	router.Handle("/graphql", &relay.Handler{Schema: s})

	log.Fatal(http.ListenAndServe(":8080", router))
}

type Resolver struct{}

func (r *Resolver) Hello(args struct{ Name string }) string {
	return "Hello, " + args.Name + "!"
}
