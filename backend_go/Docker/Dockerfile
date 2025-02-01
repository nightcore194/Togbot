FROM golang:1.23
# Set the working directory
WORKDIR /app

# Copy go.mod and go.sum files first to leverage Docker cache
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the application code
COPY . .

# Build the Go application
RUN go build -o main .

# Expose the application on port 8080
EXPOSE 8080

# Command to run the application
CMD ["./main"]