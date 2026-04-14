🔴 UI ISSUES (What needs fixing)

1. ❌ AI Commentary Error Block (Critical)
	•	Big red error panel visible on right
	•	Shows raw API error → not user-friendly
	•	Mentions technical fields like srp_functional_l7 etc.

👉 Issue:
	•	Breaks trust
	•	Looks unfinished / dev-stage

👉 Fix:
	•	Replace with:
	•	“⚠️ Unable to generate commentary. Please retry.”
	•	Add:
	•	Retry button
	•	Hide technical details behind “View details”

⸻

2. ❌ Variance Sign Logic (Major)
	•	Already confirmed:
	•	Showing wrong sign (Plan - Actual instead of Actual - Plan)

👉 Impact:
	•	Misleading financial insight (VERY serious)

👉 Fix:
	•	Correct formula:
variance = actual - plan

Color logic:
	•	🔴 Red → over plan (bad)
	•	🟢 Green → under plan (good)

⸻

3. ❌ Inconsistent Color Meaning
	•	Orange bars used in Plan & Actual
	•	Red/Green used in variance

👉 Issue:
	•	No clear visual hierarchy

👉 Fix:
	•	Standardize:
	•	Plan → Neutral (gray/blue)
	•	Actual → Blue
	•	Variance → Red/Green only

⸻

4. ❌ Progress Bar Confusion
	•	“90% of Plan” shown but:
	•	No label explaining calculation
	•	Bars look same for Plan & Actual

👉 Fix:
	•	Add label:
	•	“Actual vs Plan Completion”
	•	Use different colors for clarity

⸻

5. ❌ Table Density / Readability
	•	Table is too compressed
	•	Hard to scan quickly

👉 Fix:
	•	Add:
	•	Row spacing
	•	Zebra striping
	•	Freeze first column

⸻

6. ❌ Expand/Collapse UX Weak
	•	Only one row expanded
	•	No visual indicator of hierarchy depth

👉 Fix:
	•	Add:
	•	Indentation lines
	•	Chevron animation
	•	“Expand All / Collapse All”

⸻

7. ❌ No Clear KPI Insight

Top cards show numbers but:
	•	No takeaway like:
	•	“Overspend driven by X”
	•	“Top cost driver”

👉 Fix:
	•	Add 1-line insight under variance:
	•	“Driven by Technology Cost Partnering +£90K”

⸻

8. ❌ Export Button Low Visibility
	•	Hidden near table
	•	Not prominent

👉 Fix:
	•	Move to top right
	•	Style as primary button

⸻

9. ❌ Filter / Config UX Weak
	•	“CONFIG: UC_1” not intuitive
	•	“Manage” unclear

👉 Fix:
	•	Rename:
	•	“Config” → “Scenario”
	•	“Manage” → “Edit Scenario”

⸻

10. ❌ No Loading / Empty State
	•	Error just appears
	•	No loading indicator

👉 Fix:
	•	Add:
	•	Skeleton loader
	•	“Generating AI commentary…”

⸻

✨ COST MAGIC CHANGES (High Impact, Low Effort)

These are your 🔥 wow features for demo/client

⸻

1. 💡 AI Insight Summary (Game Changer)

Add below cards:

👉 “Key Insight”

“Costs are 1.6% under plan, mainly due to lower spend in Central Planning and Consumption Management.”

⸻

2. 🔍 Top Drivers Section

Auto-generate:
	•	🔴 Top overspend:
	•	Technology Cost Partnering (+£90K)
	•	🟢 Top savings:
	•	Consumption Management (-£118K)

⸻

3. 🎯 Drill-down Highlight

When user clicks row:
👉 Show:
	•	Trend (last 3 months)
	•	Reason (AI generated)

⸻

4. 📊 Variance Visualization

Instead of just numbers:
👉 Add mini bar chart for variance

⸻

5. ⚡ Smart Tooltips

Hover on variance:
👉 Show:
	•	Plan
	•	Actual
	•	% difference

⸻

6. 🔄 Scenario Comparison

Allow:
👉 UC_1 vs UC_2 comparison

⸻

7. 🎯 “What Changed?” Button

One-click:
👉 Explains:
	•	“Why variance changed from last month”

⸻

8. 📈 Trend Indicator

Add arrows:
	•	↑ increasing cost
	•	↓ decreasing cost

⸻

9. 🧠 AI Commentary Fix (Important)

Instead of raw API:
👉 Show:
	•	Bullet insights
	•	Clean sentences

⸻

10. 🎨 Micro UI Polish
	•	Rounded cards
	•	Softer shadows
	•	Slight animations on hover

⸻

💥 Final Reality Check

👉 Right now:
	•	Backend logic = strong
	•	UI = 70% good
	•	Client readiness = ❌ not yet

👉 After fixes:
	•	🚀 This becomes enterprise-grade dashboard
