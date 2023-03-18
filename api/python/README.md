This file defines a FastAPI application with three routes: "/", "/hello/{name}", and "/json". The "/" and "/hello/{name}" routes handle GET requests and return a JSON response with a greeting message. The "/json" route handles POST requests and returns the JSON data sent in the request body. Additionally, this file defines a GraphQL schema using the graphene library, and a "/graphql" route that handles GET requests and serves the GraphQL API.

Run the API using the Uvicorn server by running the following command in your terminal:
uvicorn main:app --reload

This will start the API server on port 8000 and automatically reload it when changes are made to the code.

Test the API using a REST client like Postman or a GraphQL client like GraphQL Playground. For example, to test the "/" route, open a web browser and navigate to http://localhost:8000/, and you should see the "Hello, World!" message.
To test the GraphQL API, open a GraphQL client like GraphQL Playground and navigate to http://localhost:8000/graphql. You can then execute queries against the hello field, passing a name argument:


query {
  hello(name: "Alice")
}


This should return a JSON response with the greeting message "Hello, Alice!".

That's it! This is just a simple example, but you can extend and customize it to suit your needs.

docker build -t my-api .

docker run -p 8000:8000 my-api
