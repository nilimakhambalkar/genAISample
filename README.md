UI Estimation Framework with Assumptions

To standardize estimation and make the process easier to scale, we are defining three levels of complexity for UI development and support:

⸻

• Small Complexity
Use case: Minor UI enhancements, label/text changes, or styling updates without backend dependency
Estimate: 1 person-day per screen
Assumptions:
	•	No backend/API changes required
	•	Design assets or text changes are readily available
	•	No cross-browser or device-level testing needed
	•	No external team dependency

⸻

• Medium Complexity
Use case: New UI components with moderate logic (e.g., forms, validation, grid views) and API integration
Estimate: 3 person-days per screen
Assumptions:
	•	API contracts are finalized and accessible
	•	UI logic is moderately complex (e.g., conditional visibility, validations)
	•	Designs (Figma/Zeplin/etc.) are approved
	•	Functional and edge test cases will be handled within this timeframe
	•	No change in scope mid-sprint

⸻

• Large Complexity
Use case: End-to-end new screens with multiple interactions, state management, third-party libraries, or complex workflows
Estimate: 5 person-days per screen
Assumptions:
	•	All designs and backend integrations are signed off before development starts
	•	Complex UI behavior is clearly defined (modals, dynamic states, etc.)
	•	Involves responsive UI handling, accessibility checks, and third-party tools
	•	Includes collaboration with backend, QA, and possibly DevOps teams
	•	No blocker from external systems or unresolved infra issues
