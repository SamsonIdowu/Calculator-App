# Use a lightweight base image
FROM alpine:3.12

# Set the working directory in the container
WORKDIR /app

# Copy the calculator source code to the container
COPY calculator.cpp .

# Install the required packages
RUN apk add --no-cache g++ make

# Build the calculator application
RUN g++ -o calculator calculator.cpp

# Set the entrypoint to run the calculator
ENTRYPOINT ["./calculator"]
