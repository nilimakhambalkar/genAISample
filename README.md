Cost Insights UI – Key Requirements

⸻

🟢 1. View-Based Navigation (Core UX)

* Provide predefined views:
    * Portfolio View (TC → Service → Process)
    * Accounts View (Chart of Accounts)
    * Driver View (JML / FT / other drivers)
* Each view should:
    * Auto-load predefined filters + dimensions
    * Allow optional user customization

⸻

🟢 2. View Type Routing (Data Source Logic)

* Introduce viewType / category to control data source:
    * Portfolio / Accounts → Cost dataset
    * Driver → Driver datasets (JML, FT, Vendor, etc.)
* Backend should route queries based on viewType

⸻

🟢 3. Common Filters & Context

* Maintain consistent filters across all views:
    * TC / Service / Function hierarchy (L5–L8)
    * Period (Month / YTD)
    * Plan type (Actual vs Plan)
* Same filter selection should apply to:
    * Cost data
    * Driver data

⸻

🟢 4. Predefined Configurations (Presets)

* Replace manual config with predefined presets
* Examples:
    * Portfolio → L6/L7 hierarchy
    * Accounts → Chart of Accounts
    * Driver → Driver-specific breakdown
* Allow users to:
    * Modify config after loading
    * Save custom views (future)

⸻

🟢 5. Drill-Down Capability

* Support hierarchical drill-down:
    * TC → Service → Process
* Drill-down should:
    * Stay within same view (Portfolio/Accounts)
    * Not mix with Driver view logic

⸻

🟢 6. Separate Data Rendering (Important)

* Do NOT merge datasets into one table
* Instead:
    * Cost view → show cost table
    * Driver view → show driver-specific table(s)
* Each driver dataset:
    * Rendered separately (JML, Vendor, Tech, etc.)
    * Based on same filters

⸻

🟢 7. Driver Data Handling

* Driver data is:
    * Multiple datasets (not one unified table)
    * Different structures (JML, Vendor, Tech, etc.)
* UI should:
    * Dynamically fetch based on viewType
    * Display relevant driver table / chart

⸻

🟢 8. AI Commentary Integration

* Generate aggregated commentary based on selected view
* Commentary should:
    * Align with current view (Portfolio / Accounts / Driver)
    * Update when filters change

⸻

🟢 9. Commentary Workflow (HITL)

* Support:
    * Edit commentary
    * Regenerate commentary
    * Save / approve commentary
* Persistence handled via backend

⸻

🟢 10. POC Constraints

* Use single file input (CSV/Excel) for POC
* Limited ability to:
    * Join multiple datasets
    * Handle complex driver integration
* Simplify:
    * Use mock or limited driver data
    * Focus on UI + flow validation

⸻

🟢 11. Target State (Post-POC)

* Backend supports:
    * Multiple datasets
    * Dynamic queries
    * Separate driver tables
* UI supports:
    * Real-time switching between views
    * Scalable driver integrations