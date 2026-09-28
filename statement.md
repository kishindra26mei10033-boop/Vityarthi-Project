# Project Statement: Vehicle Service Cost Calculator

## 1. Problem Statement
Automotive service workshops and independent repair garages frequently experience operational friction and billing discrepancies when calculating maintenance costs manually. Because pricing varies significantly across different vehicle classifications (e.g., standard commuter two-wheelers vs. premium bikes, or multi-utility vehicles vs. sports utility vehicles), relying on verbal estimates or manual entry creates several recurring problems:

- **Pricing Inconsistency & Human Calculation Errors:** Service advisors may miscalculate individual charges or fail to properly compute statutory tax rates.
- **Double Billing:** Customers who choose "Full Service" after selecting individual repairs like "Oil Change", "Brake Service", risk being charged redundant fees without automated package override policies.
- **Lack of Defensive Input Validation:** Simple calculation tools often crash when users provide invalid numerical ranges or non-numeric textual inputs.

The **Vehicle Service Cost Calculator** provides an automated, terminal-based computational engine that enforces consistent rate cards, prevents duplicate item selections, handles bundled service overrides, and computes transparent, tax-compliant invoices.

---

## 2. Scope of the Project

### In-Scope
- **Vehicle Classification Support:** Dedicated multi-tier pricing structures for four specific categories: Premium Bikes, Normal Bikes, SUVs, and MUVs.
- **Service Line Selections:** Standardized options for Brake Service, Engine Check, Oil Change, and Full Service.
- **Interactive Multi-Service Selection:** Allowing users to add multiple distinct service items within a single billing cycle.
- **Duplicate Service Suppression:** Active tracking to prevent the identical service from being added more than once.
- **Package Override Rule:** Automatic clearing of prior individual selections when "Full Service" is chosen, applying consolidated bundle pricing.
- **Statutory Tax Calculations:** Automated computation of Central GST (CGST @ 9%) and State GST (SGST @ 9%) over the subtotal to generate a final payable invoice.
- **Defensive Error Handling:** Input validation routines employing `try...except` exception trapping to handle arbitrary string inputs and out-of-range options without program crashes.
- **Pure Terminal Execution:** Zero GUI dependencies, ensuring 100% command-line compatibility across Linux, macOS, and Windows.

### Out-of-Scope
- Persistent external database storage (e.g., SQLite/PostgreSQL) for archival storage of past invoices.
- Graphical User Interface (GUI) or browser-based web frontend.
- Payment gateway integration or digital card/UPI processing.
- Dynamic spare parts inventory tracking or labor hour scheduling.

---

## 3. Target Users
1. **Automotive Workshop Service Advisors:** Primary operators who interact with customers at service reception desks to quickly determine diagnostic and repair estimates.
2. **Independent Mechanics & Small Garage Owners:** Small business owners requiring a lightweight, zero-overhead billing tool that runs locally without complex point-of-sale software.
3. **Vehicle Owners / Customers:** End users seeking transparent, upfront pricing breakdowns and tax visibility before authorizing vehicle maintenance work.
4. **Academic Evaluators:** Instructors and automated test runners assessing Python programming concepts, structured flow control, function modularity, and input validation.

---

## 4. High-Level Features
- **Tabular Rate Grid Presentation:** Utilizes the `tabulate` library to output a clear, aligned pricing matrix for all supported vehicle classes upon program entry.
- **Structured Multi-Tier Navigation:** Sequential selection hierarchy (Main Menu → Vehicle Choice → Category Choice → Service Requirements).
- **Session Continuity & Exit Control:** Main application loop allowing continuous billing transactions or clean termination without abrupt interruptions.
- **Exception-Resilient Prompting:** Centralized validation loop (`loop_service`) that defends against non-integer inputs and boundary violations.
- **Full Service Package Override Engine:** Intelligent state reset that clears temporary arrays when bundled servicing is selected, ensuring fair and accurate customer billing.
- **Detailed Itemized Invoice:** Generates a structured bill display detailing individual item charges, subtotal, itemized CGST (9%), SGST (9%), and total charges.
