# Semantic Critique — Testdataset

Generated: 2026-05-25T13:08:05.447335Z

## Client Management

**Verdict:** yes  
**Forced ship:** no  

The AST captures the interactive elements and conditional logic from the description; only minor inferred items are present and no critical elements are missing.

**Missing:**

- Create_Client_Wizard.steps[3].fields.Family_Members

**Phantoms (hallucinations):**

- Client_Detail_Page.tabs[3].fields.Family_Members (repeating_group inferred though description only names the tab)
- Clients_Page.row_actions[0] (View link inferred instead of marking the Name column itself as a clickable link)

---
