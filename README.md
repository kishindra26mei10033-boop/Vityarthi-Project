# Vehicle Service Cost Calculator

## Overview

This is a command-line interface application built with Python IDLE that calculates the total service cost for different types of vehicles like: Premium Bikes, Normal Bikes, SUVs, and MUVs. The program shows the menu that allows users to perform multiple calculations in a single session, select various services, handle invalid inputs gracefully, apply taxes (CGST and SGST), and generate a final service invoice.

## Prerequisites & Installation

To run this project from scratch, you will need **Python**, **pip** (Python's package installer), and **Git** installed on your system.

### 1. Installing Git

Git is required to clone the repository into your local machine

* **Windows:** Download and install from [git-scm.com](https://git-scm.com/download/).

* **macOS:** Open your terminal and run `xcode-select --install`, or install via Homebrew using `brew install git`.

* **Linux (Debian/Ubuntu):** Open your terminal and run `sudo apt-get update` followed by `sudo apt-get install git`.

Verify Git is installed by running:

```
git --version

```

### 2. Installing Python & pip

You must have Python 3.6 or higher installed. `pip` is usually included automatically when you install Python.

* **Windows & macOS:** Download the official installer from [python.org](https://www.python.org/downloads/).
* **Important:** During Windows installation, ensure you check the box that says **"Add Python to PATH"**.

* **Linux (Debian/Ubuntu):** Run `sudo apt install python3 python3-pip`.

Verify Python and pip are installed by running:

```
python --version
pip --version

```

*(Note: If you are on Mac or Linux, you may need to use `python3` and `pip3`)*

## Dependency Installation

This project relies on the external `tabulate` library to display the pricing table neatly in the terminal. Once `pip` is installed, open your terminal and run:

```
pip install tabulate

```

## Setup and Execution

Follow these steps to run the project locally in Command Prompt:

Open Command Prompt and
1. **Clone the repository**:

   ```
   git clone https://github.com/kishindra26mei10033-boop/Vityarthi-Project.git
   
   ```

2. **Navigate to the project directory**:

   ```
   cd Vityarthi-Project
   
   ```

3. **Run the script**:
   Execute the Python file from your terminal:

   ```
   python "main.py"
   
   ```

   *(Note: Use `python3` instead of `python` if required by your operating system)*

## Usage Instructions

1. Upon running the script, you will be presented with a main menu to either **Enter the program** (1) or **Exit** (2).

2. If you enter the program, a pricing table will be displayed.

3. The terminal will prompt you to select a vehicle type (Bike or Car) using inputs.

4. Follow the on-screen prompts to choose the specific vehicle category (e.g., SUV, Premium bike).

5. Select the desired services from the list. If you choose "Full Service" (Option 4), it will automatically override and replace any individual services previously selected.

6. Choose whether to add more services (`yes` or `no`).

7. Once finished, the program will print a final invoice including the subtotal and applicable taxes.

8. After the bill is printed, you will be returned to the main menu where you can start a new calculation or exit the application safely.

## To Safely Clear the Program in Command Prompt 

Open Fresh Command Prompt and 

**clear the program**:

   ```
   rmdir /s /q Vityarthi-Project 
   
   ```
