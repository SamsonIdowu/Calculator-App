# Use an official GCC runtime as the base image
FROM gcc:9.2

# Set the working directory in the container
WORKDIR /app

# Copy the calculator script to the container
COPY calculator.cpp .

# Compile the calculator script
RUN g++ calculator.cpp -o calculator

# Set the entrypoint to run the calculator binary
ENTRYPOINT ["./calculator"]
