from calculator import perform_operation

from behave import *


_operations = {
    "addition": "+",
    "substraction": "-"
}


@when("first number is {number}")
def step_impl(context, number):
    context.first_number = number


@when("second number is {number}")
def step_impl(context, number):
    context.second_number = number


@when("operation is {operation}")
def step_impl(context, operation):
    context.operation = _operations[operation]


@then("result is {expected_result}")
def step_impl(context, expected_result):
    operation_string = f"{context.first_number} {context.operation} {context.second_number}"
    actual_result = perform_operation(operation_string)
    assert int(expected_result) == actual_result, f"Expected operation '{operation_string}' to result in value '{expected_result}', but the result was actually '{actual_result}'"