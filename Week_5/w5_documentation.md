# Week 5 Tutorial – Café Bill Calculator

## 1. Problem Analysis

### 1.1 Problem Statement

The café currently calculates customer bills manually.  
The purpose of this program is to calculate the customer's total bill automatically based on the quantities of coffee, tea, and sandwiches ordered.

### 1.2 Inputs

The program requires the following inputs:

- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity

### 1.3 Outputs

The program displays a receipt containing:

- Customer name
- Coffee quantity
- Tea quantity
- Sandwich quantity
- Total bill in RM

### 1.4 Typical Process Flow

1. Start the program.
2. Ask the user to enter the customer's name.
3. Ask the user to enter the coffee quantity.
4. Ask the user to enter the tea quantity.
5. Ask the user to enter the sandwich quantity.
6. Calculate the total bill using the item prices.
7. Print the receipt.
8. End the program.

### 1.5 Constraints

- Coffee price is fixed at RM 8.50.
- Tea price is fixed at RM 6.00.
- Sandwich price is fixed at RM 12.00.
- Quantities must be whole numbers.
- Quantities cannot be negative.
- The customer name cannot be empty.
- The total must be displayed with two decimal places.

## 2. Problem Decomposition

The problem can be divided into the following smaller tasks:

1. Store the prices of coffee, tea, and sandwiches.
2. Get the customer name.
3. Get the quantity of each item.
4. Validate that the quantities are not negative.
5. Calculate the cost of each item.
6. Add all item costs to calculate the total bill.
7. Print the receipt with the customer information and total.

## 3. Pseudocode

START

SET coffee price = 8.50  
SET tea price = 6.00  
SET sandwich price = 12.00  

INPUT customer name  
INPUT coffee quantity  
INPUT tea quantity  
INPUT sandwich quantity  

IF any quantity is less than zero
    DISPLAY error message
ELSE
    coffee cost = coffee quantity × coffee price
    tea cost = tea quantity × tea price
    sandwich cost = sandwich quantity × sandwich price

    total = coffee cost + tea cost + sandwich cost

    DISPLAY receipt
    DISPLAY customer name
    DISPLAY coffee quantity
    DISPLAY tea quantity
    DISPLAY sandwich quantity
    DISPLAY total
END IF

END