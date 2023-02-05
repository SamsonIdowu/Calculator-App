#include <iostream>
#include <string>
#include <cmath>

#include <flask/flask.hpp>

int main() {
    Flask app;
    app.route("/", []() {
        return "Welcome to the calculator!";
    });
    app.route("/calculate", []() {
        return "Enter your calculation in the URL in the format '/calculate/<expression>', where <expression> is the calculation you want to perform.";
    });
    app.route("/calculate/<expression>", [](std::string expression) {
        // Evaluate the expression
        double result = eval(expression.c_str());
        return std::to_string(result);
    });
    app.run();
    return 0;
}
