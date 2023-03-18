simple "Hello, World!" Go API using gorilla/mux and graph-gophers/graphql-go packages, and handling REST/JSON and GraphQL requests:


Install the required packages by running the following command in your terminal:
go get github.com/gorilla/mux github.com/graph-gophers/graphql-go

Create a new directory called api/go in the root directory of your project, and navigate to it in your terminal.

Inside the api/go directory, create a new file called main.go with the following contents:

This file defines a Go API using the gorilla/mux package, with two routes: "/" and "/graphql". The "/" route handles GET requests and returns a JSON response with a greeting message. The "/graphql" route serves the GraphQL API using the graph-gophers/graphql-go package.

Run the API by running the following command in the api/go directory:
go run main.go
This will start the API server on port 8080.

Test the API using a REST client like Postman or a GraphQL client like GraphQL Playground. For example, to test the "/" route, open a web browser and navigate to http://localhost:8080/, and you should see the "Hello, World!" message.
To test the GraphQL API, open a GraphQL client like GraphQL Playground and navigate to http://localhost:8080/graphql. You can then execute queries against the hello field, passing a name argument:

query {
  hello(name: "Alice")
}


This should return a JSON response with the greeting message "Hello, Alice!".

