# Project Statement: Vehicle Service Cost Calculator

## 1. Problem Statement
Automotive service centers, garage owners, and vehicle mechanics frequently struggle to provide customers with instant, transparent, and itemized billing estimates for vehicle servicing. Customers often face ambiguity regarding individual service rates (such as engine checks, brake repairs, or oil changes) across different vehicle classes (Premium Bikes, Normal Bikes, SUVs, and MUVs). 

Manual calculations are prone to human errors, inconsistent tax evaluations (CGST & SGST application), and slow down the booking intake process. There is a clear need for a lightweight, automated interactive application that handles vehicle categorization, tracks multiple service selections dynamically, applies appropriate price tiers, calculates exact taxes, and generates structured, error-free invoices instantly.

## 2. Scope of the project
The scope of this project encompasses designing and implementing a modular, interactive terminal-based Vehicle Service Cost Calculator written in Python. 

### In-Scope Boundaries:
* **Vehicle Tier Management:** Providing structured options for two main vehicle groups (Bikes and Cars), further subdivided into specific pricing tiers (Premium Bike, Normal Bike, SUV, MUV).
* **Dynamic Menu & Multi-Selection Routing:** Presenting a flexible console interface that permits users to select individual services or chain multiple service requirements sequentially.
* **Smart "Full Service" Override:** Automatically clearing separate minor service costs and replacing them with a flat-rate tier if a customer chooses a full bundle package.
* **Duplicate Selection Prevention:** Dynamically keeping track of current selections within a user's session to ensure identical services cannot be accidentally added twice.
* **Taxation & Invoice Structuring:** Automating pricing math by breaking items down into explicit subtotal matrices, calculating precise CGST (9%) and SGST (9%) allocations, and presenting a formatted commercial text invoice.

### Out-of-Scope (Future Enhancements):
* Graphical User Interfaces (GUI) or web deployment.
* Persistent database engines (e.g., SQLite, PostgreSQL) for customer registration historical records.
* Digital payment processing or inventory stock parts tracking.

## 3. Target Users
* **Small to Medium Garage Owners & Staff:** Automates and standardizes billing rates for reception desks during vehicle intake.
* **Vehicle Mechanics:** Allows technicians to quickly evaluate service costs before beginning active maintenance.
* **Customers / End-Users:** Provides absolute price visibility and clear itemized billing options before approving repairs.

## 4. High-Level Features
* **Tiered Pricing Matrix Engine:** Houses predefined pricing profiles across multiple options (Brake Service, Engine Check, Oil Change, Full Service) customized per vehicle category.
* **Interactive Core Command Loop:** Sanitizes user inputs, validates integer bounds to handle unexpected keyboard faults gracefully, and coordinates application navigation.
* **Active Session Basket Tracker:** Stores current selected options in memory lists to build multi-item tasks dynamically while checking for repetitive inputs.
* **Automated Fiscal Calculation System:** Operates precise float conversions for subtotal fees, itemized double tax distributions (18% combined GST), and calculates final gross payable amounts.
* **Formatted Matrix Presentation Layout:** Leverages structured command-line tables to draw organized, scannable price indexes for a clear user experience.
