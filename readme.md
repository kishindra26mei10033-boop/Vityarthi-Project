# Vehicle Service Cost Calculator

## Overview

This is a command-line application built in Python that calculates the total service cost for different types of vehicles, including Premium Bikes, Normal Bikes, SUVs, and MUVs. The program features an interactive menu that allows users to perform multiple calculations in a single session, select various services, handle invalid inputs gracefully, apply taxes (CGST and SGST), and generate a final itemized invoice.

## Prerequisites (Environment Setup)

To run this project, you must have Python installed on your system.

* **Python Version:** Python 3.6 or higher is recommended.

* You can verify your Python installation by opening your terminal or command prompt and running:

  ```
  python --version
  
  ```

## Dependency Installation

This project relies on the external `tabulate` library to display the pricing table neatly in the terminal. Before running the script, you must install this dependency.

Open your terminal and run the following command:

```
pip install tabulate

```

## Setup and Execution

Follow these steps to run the project locally:

1. **Clone the repository**:

   ```
   git clone https://github.com/kishindra26mei10033-boop/Vityarthi-Project
   
   ```

2. **Navigate to the project directory**:

   ```
   cd Vityarthi-Project
   
   ```

3. **Run the script**:
   Execute the updated Python file from your terminal:

   ```
   python "Vehicle service cost calculator.py"
   
   ```

   *(Note: If you are on a Mac or Linux environment, you may need to use `python3` instead of `python`)*

## Usage Instructions

1. Upon running the script, you will be presented with a main menu to either **Enter the program** (1) or **Exit** (2).

2. If you enter the program, a pricing table will be displayed.

3. The terminal will prompt you to select a vehicle type (Bike or Car) using numeric inputs.

4. Follow the on-screen prompts to choose the specific vehicle category (e.g., SUV, Premium bike).

5. Select the desired services from the list. If you choose "Full Service" (Option 4), it will automatically override and replace any individual services previously selected.

6. Choose whether to add more services (`yes` or `no`).

7. Once finished, the program will print a final invoice including the subtotal and applicable taxes.

8. After the bill is printed, you will be returned to the main menu where you can start a new calculation or exit the application safely.