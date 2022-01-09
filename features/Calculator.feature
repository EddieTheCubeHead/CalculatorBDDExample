Feature: Performing two number operations

    Scenario: Adding two positive numbers
        When first number is 3
        And second number is 6
        And operation is addition
        Then result is 9

    Scenario: Adding a positive and negative number
        When first number is 10
        And second number is -11
        And operation is addition
        Then result is -1

    Scenario: Substracting a positive number from a bigger one
        When first number is 11
        And second number is 8
        And operation is substraction
        Then result is 3

    Scenario: Substracting a positive number from a smaller one
        When first number is 142
        And second number is 558
        And operation is substraction
        Then result is -416

    Scenario: Substracting a negative number from a positive one
        When first number is 38
        And second number is -13
        And operation is substraction
        Then result is 51

    Scenario: Substracting a positive number from a negative one
        When first number is -4
        And second number is 42
        And operation is substraction
        Then result is -46
