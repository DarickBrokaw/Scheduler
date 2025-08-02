# Scheduler

# 📎 Software Application Planning Document

**MVP: Speech Therapy Scheduling Application**
**Version:** 1.0
**Date:** \[Insert Date]

---

## 1. Executive Summary

This MVP demonstrates an automated scheduling system for pediatric speech therapy. It supports two therapists and thirty patients, solving for real-world constraints like therapist availability, patient age and schooling, parent availability, therapist specialties, and sibling grouping. The system outputs a **calendar-style schedule per therapist** and includes a simple UI for viewing results.

---

## 2. Scope of the MVP

### ✅ Inclusions

* Therapist-patient scheduling (hard constraints only)
* Static JSON test dataset (therapists and patients)
* Sibling grouping (same-time or sequential)
* Calendar-style schedule output
* Simulated cancellations
* Basic HTML UI (no frameworks)

### ❌ Exclusions

* Authentication or user roles
* Database storage (e.g., Firebase)
* Notifications or messaging
* Mobile/responsive UI
* Soft constraints (e.g., load balancing)

---

## 3. Architecture Goals & AI Agent Preferences

### 🐽 High-Level Goals

* Modular architecture
* Clear I/O separation
* Human- and AI-readable structure

### 💡 Design Preferences

* JSON as input/output (no hardcoded data)
* Scheduler = single entry point script
* Output grouped by therapist → day → time
* UI reads pre-formatted JSON (no transformation)

### 🧠 AI Agent Guidance

* One module per responsibility (`scheduler`, `utils`, `data`)
* Avoid global variables
* Output: JSON in calendar layout, no UI transformation needed
* Keep functions small and named clearly

---

## 4. System Overview

### Architecture Diagram

```
[therapists.json] + [patients.json]
         ↓
  [run_scheduler.py] → schedule_output.json
         ↓
   [index.html] ↔ [styles.css, script.js]
```

---

## 5. Directory & File Structure

```
/speech_scheduler_mvp/
│
├── data/
│   ├── therapists.json
│   ├── patients.json
│   └── schedule_output.json   ← calendar-style output
│
├── scheduler/
│   ├── run_scheduler.py       ← main script
│   ├── constraint_solver.py   ← OR-Tools logic
│   └── utils.py               ← time parsing, sibling utils
│
├── ui/
│   ├── index.html             ← visual schedule
│   ├── styles.css
│   └── script.js              ← renders calendar view
│
├── simulate_cancellation.py   ← test script
├── README.md
└── requirements.txt           ← ortools
```

---

## 6. Data Model

### 6.1 Therapists

```json
{
  "id": "therapist_1",
  "name": "Emily Chen",
  "available_days": ["Mon", "Wed", "Fri"],
  "available_hours": ["08:00-12:00", "13:00-17:00"],
  "specialties": ["speech delay", "apraxia"]
}
```

### 6.2 Patients

```json
{
  "id": "patient_01",
  "name": "Lucas Smith",
  "age": 5,
  "school_status": "preschool",
  "available_days": ["Mon", "Wed"],
  "available_hours": ["14:00-17:00"],
  "parent_available_hours": ["13:30-17:30"],
  "sibling_ids": ["patient_02"],
  "grouping_type": "same_time",
  "preferred_specialties": ["speech delay"]
}
```

---

## 7. Scheduling Logic

### Algorithm

* **Google OR-Tools CP-SAT**
* Binary decision variables for therapist x time x patient
* Output format built as: therapist → day → list of time slots

### Hard Constraints

* Therapist and patient availability
* Parent availability
* Therapist specialty match
* Sibling grouping (same-time or sequential)
* No double booking

---

## 8. Output Format: Calendar-Based Schedule

### Example: `data/schedule_output.json`

```json
{
  "therapist_1": {
    "name": "Emily Chen",
    "schedule": {
      "Monday": [
        {
          "time": "08:00",
          "patient_id": "patient_01",
          "patient_name": "Lucas Smith",
          "duration": 30,
          "grouping_type": "same_time"
        },
        {
          "time": "08:30",
          "patient_id": "patient_02",
          "patient_name": "Sophia Smith",
          "duration": 30,
          "grouping_type": "same_time"
        }
      ]
    }
  }
}
```

---

## 9. Cancellation Simulation

* Triggered by script or test button
* Cancels 3–5 random sessions
* Reallocates open time slots to eligible patients
* Grouping logic is preserved

---

## 10. UI: Minimal Calendar Display

### Requirements

* Weekly calendar grid (Mon–Fri, 08:00–17:00)
* 30-minute time blocks
* Dropdown to toggle between therapists
* Each time block shows patient name

### Technologies

* `index.html` + `script.js` + `styles.css`
* Reads directly from `schedule_output.json`
* No user interaction beyond display

---

## 11. Development Stack

| Layer    | Technology         |
| -------- | ------------------ |
| Backend  | Python 3, OR-Tools |
| Data     | JSON (flat files)  |
| Frontend | HTML, JS, CSS      |
| Platform | Replit / Local run |

---

## 12. Testing Plan

* ✅ Verify each therapist has no overlapping sessions
* ✅ Ensure each patient is assigned once
* ✅ Validate sibling grouping (same-time or sequential)
* ✅ Simulate cancellations and reallocation
* ✅ Confirm UI shows correct data in correct time slots

---

## 13. Post-MVP (Future Scope)

* Firebase for persistence and auth
* Gemini-powered natural-language scheduling
* Admin dashboard with filters and overrides
* HIPAA compliance review
* SMS/email reminder system

---

**Next Step:**
Would you like to generate the JSON test dataset or the scheduling engine first?

```
```
