# Homework Notebook: The Meeting Cost Calculator

**Course**: Vibe Coding Workshop &bull; Day 2 Session 1  
**Assignment**: HW1 — The Missing Penny  
**Student**: Mani Subramanian  
**Date**: October 2026  
**Tools Used**: Google Antigravity 2.0, Python 3.9+, macOS Chrome/Safari  

---

## 🧭 Executive Summary & Core Principle

> *"Every vague word in your prompt is a decision you've handed to the AI."*

This notebook documents the disciplined, step-by-step process of building **The Meeting Cost Calculator** for Linda and the Sierra Trails Hiking Club planning committee. Instead of letting the AI guess the financial rules, we established the exact arithmetic in integer cents by hand first, directed the AI with a structured six-part contractor brief, diagnosed the gap in one phrase, improved the brief with exactly one change, and verified every single cent using an automated Python test suite.

---

## 🧮 Part 1: Hand-Calculated Arithmetic (Before Prompting)

Before giving any instructions to the AI, we work out the baseline mathematical truth on paper to ensure we never "check the AI against itself."

### 1. Core Financial Rules
1. **Never use floating-point dollar numbers**: Floating-point math (`0.1 + 0.2 = 0.30000000000000004`) introduces rounding errors and phantom pennies.
2. **All rates converted to integer cents**: $\$85.00 \to 8,500¢$, $\$47.50 \to 4,750¢$, $\$62.75 \to 6,275¢$.
3. **Accumulate total hourly rate first**:
   $$\text{Total Hourly Rate (cents)} = \sum (\text{attendees}_i \times \text{rate\_cents}_i)$$
4. **Meeting cost formula**:
   $$\text{Total Cost (cents)} = \text{round}\left(\frac{\text{Total Hourly Rate} \times \text{minutes}}{60}\right)$$
   $$\text{Cost Per Minute (cents)} = \text{round}\left(\frac{\text{Total Hourly Rate}}{60}\right) \quad (\text{if minutes} > 0 \text{ else } 0)$$
5. **Rounding Convention**: Standard Financial Rounding (**Round Half Up**). A half-cent ($0.5¢$) rounds up to the next nearest whole cent.

---

### 2. Hand-Worked Test Cases

#### Case 1: Standard Committee Meeting (Success Criteria 1)
- **Input**: 6 people @ $\$85.00$/hr for 45 minutes
- **Hourly rate**: $6 \times 8,500¢ = 51,000¢/\text{hr}$
- **Total Cost**: $\frac{51,000 \times 45}{60} = \frac{2,295,000}{60} = 38,250¢ \implies \mathbf{\$382.50}$
- **Cost Per Minute**: $\frac{51,000}{60} = 850¢ \implies \mathbf{\$8.50/\text{min}}$

#### Case 2: All-Day Offsite Meeting (Success Criteria 2)
- **Input**: 120 people @ $\$150.00$/hr for 8 hours (480 minutes)
- **Hourly rate**: $120 \times 15,000¢ = 1,800,000¢/\text{hr}$
- **Total Cost**: $\frac{1,800,000 \times 480}{60} = 1,800,000 \times 8 = 14,400,000¢ \implies \mathbf{\$144,000.00}$ (with comma)
- **Cost Per Minute**: $\frac{1,800,000}{60} = 30,000¢ \implies \mathbf{\$300.00/\text{min}}$

#### Case 3: Fractional Half-Cent Rounding (Success Criteria 3)
- **Input**: 3 people @ $\$47.50$/hr for 7 minutes
- **Hourly rate**: $3 \times 4,750¢ = 14,250¢/\text{hr}$
- **Total Cost before rounding**: $\frac{14,250 \times 7}{60} = \frac{99,750}{60} = 1,662.5¢$
- **Round Half Up**: $1,662.5¢ \to 1,663¢ \implies \mathbf{\$16.63}$
- **Cost Per Minute before rounding**: $\frac{14,250}{60} = 237.5¢$
- **Round Half Up**: $237.5¢ \to 238¢ \implies \mathbf{\$2.38/\text{min}}$

#### Case 4: Zero Minutes Edge Case
- **Input**: 5 people @ $\$100.00$/hr for 0 minutes
- **Total Cost**: $\mathbf{\$0.00}$
- **Cost Per Minute**: Must return $\mathbf{\$0.00}$ (Division by zero must be guarded against so it never shows `"NaN"`, `"Infinity"`, or an unhandled crash).

#### Case 5: Zero Attendees Edge Case
- **Input**: 0 attendees for 60 minutes
- **Total Cost**: $\mathbf{\$0.00}$, **Cost Per Minute**: $\mathbf{\$0.00}$

---

## 📝 Part 2: Brief v1 (The Initial Contractor Brief)

Here is the exact six-part brief created from the required skeleton:

```markdown
ROLE: You are an internal tools web developer building lightweight financial calculators for non-profit committee planning.
TASK: Build a single-page web meeting cost calculator.
CONTEXT: 
Who uses it: Linda and planning committee members of the Sierra Trails Hiking Club.
Where it runs: A web browser by double-clicking index.html offline on any computer.
Limits: Plain HTML, CSS, and JavaScript only. No external libraries, no frameworks, no backend, no build steps.

FORMAT:
Create exactly these files:
- index.html (single self-contained file containing HTML, styling, and JavaScript)
When finished, tell me:
- How to open index.html and confirm the calculation with an example.

CONSTRAINTS:
Money: Store and compute money as integer cents. Never calculate money using floating-point dollars.
Rounding: Round half up to the nearest whole cent at the final accumulation step.
If there are 0 attendees: Total cost and cost per minute should show $0.00.
If the length is 0 minutes: Total cost should show $0.00.
If unsure: Default to simple, clean vanilla JS with clear readable labels and reactive live updating.

EXAMPLES:
<example>
Input: 6 people at $85.00/hour for 45 minutes -> Total: $382.50 Per minute: $8.50
</example>
```

---

## 🔍 Part 3: What Brief v1 Produced & The Diagnosis

### Observation of v1 Output
When testing `index.html` produced from Brief v1:
- The standard calculations ($6 \times \$85.00$ for 45 min) evaluated cleanly to `$382.50`.
- However, when entering `0` in the minutes input field:
  - Total Cost correctly showed `$0.00`.
  - But **Cost Per Minute** produced `Infinity` (and in some browsers `NaN`).
  - Cause: Brief v1 stated `If the length is 0 minutes: Total cost should show $0.00`, but omitted an explicit constraint for the cost-per-minute metric when minutes is zero. The AI computed `costPerMinute = totalHourlyCents / 60` or divided by zero duration.

### One-Phrase Diagnosis:
> `missing constraint: cost per minute when meeting duration is 0 minutes must explicitly display $0.00 instead of evaluating division by zero.`

### Supporting Evidence:
The AI adhered strictly to what was written in v1, but because the 0-minute constraint only mentioned total cost, the per-minute display logic evaluated division by zero when minutes was set to 0. This allowed `Infinity` to be rendered to the user, violating the core assignment constraint.

---

## 🔄 Part 4: Brief v2 (One Targeted Change)

In Brief v2, we made **exactly one targeted change** from v1, fixing the specific gap named in the diagnosis:

```markdown
ROLE: You are an internal tools web developer building lightweight financial calculators for non-profit committee planning.
TASK: Build a single-page web meeting cost calculator.
CONTEXT: 
Who uses it: Linda and planning committee members of the Sierra Trails Hiking Club.
Where it runs: A web browser by double-clicking index.html offline on any computer.
Limits: Plain HTML, CSS, and JavaScript only. No external libraries, no frameworks, no backend, no build steps.

FORMAT:
Create exactly these files:
- index.html (single self-contained file containing HTML, styling, and JavaScript)
When finished, tell me:
- How to open index.html and confirm the calculation with an example.

CONSTRAINTS:
Money: Store and compute money as integer cents. Never calculate money using floating-point dollars.
Rounding: Round half up to the nearest whole cent at the final accumulation step.
If there are 0 attendees: Total cost and cost per minute should show $0.00.
*** CHANGE FROM V1 START ***
If the length is 0 minutes: Both Total cost and Cost per minute must display $0.00, and never evaluate division by zero, NaN, or Infinity.
*** CHANGE FROM V1 END ***
If unsure: Default to simple, clean vanilla JS with clear readable labels and reactive live updating.

EXAMPLES:
<example>
Input: 6 people at $85.00/hour for 45 minutes -> Total: $382.50 Per minute: $8.50
</example>
```

---

## 📊 Part 5: The Test Table (Validation Across All Edge Cases)

| Test # | Test Case & Inputs | Expected (By Hand) | Actual (App Result) | Status |
| :---: | :--- | :--- | :--- | :---: |
| **1** | **SC1: Standard Meeting**<br>6 attendees @ $85.00/hr, 45 min | Total: **$382.50**<br>Per Min: **$8.50** | Total: $382.50<br>Per Min: $8.50 | **PASS** |
| **2** | **SC2: Large Offsite Meeting**<br>120 attendees @ $150.00/hr, 480 min (8 hrs) | Total: **$144,000.00**<br>Per Min: **$300.00** | Total: $144,000.00<br>Per Min: $300.00 | **PASS** |
| **3** | **SC3: Fractional Half-Cent**<br>3 attendees @ $47.50/hr, 7 min | Total: **$16.63** (1,663¢)<br>Per Min: **$2.38** (238¢) | Total: $16.63<br>Per Min: $2.38 | **PASS** |
| **4** | **Zero Duration Edge Case**<br>5 attendees @ $100.00/hr, 0 min | Total: **$0.00**<br>Per Min: **$0.00** (no NaN/Infinity) | Total: $0.00<br>Per Min: $0.00 | **PASS** |
| **5** | **Zero Attendees Edge Case**<br>0 attendees @ $120.00/hr, 60 min | Total: **$0.00**<br>Per Min: **$0.00** | Total: $0.00<br>Per Min: $0.00 | **PASS** |
| **6** | **Decimal Rates & Multi-Tier**<br>2 @ $100.00/hr + 4 @ $62.75/hr, 30 min | Total: **$225.50**<br>Per Min: **$7.52** | Total: $225.50<br>Per Min: $7.52 | **PASS** |
| **7** | **Upper Limit Threshold**<br>520 attendees @ $100.00/hr, 60 min | Total: **$52,000.00**<br>Friendly warning shown | Total: $52,000.00<br>Warning banner displayed | **PASS** |
| **8** | **Negative Input Safeguard**<br>Attendees: -3, Rate: $50.00, 30 min | Friendly error notification;<br>Total: $0.00 | Error displayed;<br>Total: $0.00 | **PASS** |
| **9** | **Non-Numeric Rate Safeguard**<br>Attendees: 4, Rate: "abc", 30 min | Friendly error notification;<br>Total: $0.00 | Error displayed;<br>Total: $0.00 | **PASS** |

---

## 🐍 Part 6: Python Verification Engine with Comments

The Python engine ([meeting_cost.py](file:///Users/manisubramanian/Documents/GitHub/CI-CD/Day2_HW1/meeting_cost.py)) serves as our mathematical ground truth:

```python
"""
meeting_cost.py - The Meeting Cost Calculator (Core Arithmetic Engine)
Day 2 Session 1 Homework: "The Missing Penny"
Author: Mani Subramanian
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import List, Dict, Union

def dollars_to_cents(amount_str: Union[str, float, int]) -> int:
    """
    Parses a dollar input into exact integer cents.
    Prevents floating-point precision drift by utilizing Python's Decimal.
    """
    if amount_str is None:
        raise ValueError("Hourly rate cannot be empty.")
    
    # Strip whitespace, dollar symbols, and thousand commas
    cleaned = str(amount_str).strip().replace("$", "").replace(",", "")
    if not cleaned:
        raise ValueError("Hourly rate cannot be empty.")
    
    try:
        val = Decimal(cleaned)
    except Exception:
        raise ValueError(f"Invalid hourly rate: '{amount_str}'.")
    
    if val < 0:
        raise ValueError(f"Hourly rate cannot be negative: '{amount_str}'.")
    
    # Quantize to whole cents using ROUND_HALF_UP (Standard Financial Rounding)
    return int((val * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))

def format_cents(cents: int) -> str:
    """
    Formats integer cents into standard US currency string with comma separators.
    e.g. 14400000 -> "$144,000.00", 38250 -> "$382.50"
    """
    dollars = cents // 100
    rem_cents = cents % 100
    return f"${dollars:,}.{rem_cents:02d}"

def calculate_meeting_cost(
    roles: List[Dict[str, Union[str, int, float]]],
    minutes: int,
    max_attendees: int = 500,
    max_minutes: int = 1440
) -> Dict[str, Union[int, str]]:
    """
    Calculates total meeting cost and cost per minute in integer cents.
    """
    if minutes is None or minutes < 0:
        raise ValueError("Meeting minutes must be a non-negative integer.")
        
    total_attendees = 0
    total_hourly_rate_cents = 0
    
    # Accumulate rates in integer cents across all roles
    for row in roles:
        raw_name = str(row.get("name", "")).strip()
        raw_attendees = row.get("attendees", 0)
        raw_rate = row.get("hourly_rate", 0)
        
        if not raw_name and not raw_attendees and not raw_rate:
            continue
            
        attendees = int(raw_attendees)
        if attendees < 0:
            raise ValueError("Attendees count cannot be negative.")
            
        rate_cents = dollars_to_cents(raw_rate) if raw_rate else 0
        total_attendees += attendees
        total_hourly_rate_cents += (attendees * rate_cents)
    
    # Zero minutes or zero attendees: division-by-zero safeguard
    if minutes == 0 or total_hourly_rate_cents == 0:
        return {
            "total_cost_cents": 0,
            "total_cost_formatted": "$0.00",
            "cost_per_minute_cents": 0,
            "cost_per_minute_formatted": "$0.00"
        }
    
    # Exact calculation in integer cents with Round Half Up
    unrounded_total = Decimal(total_hourly_rate_cents * minutes) / Decimal(60)
    total_cost_cents = int(unrounded_total.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    
    unrounded_per_min = Decimal(total_hourly_rate_cents) / Decimal(60)
    cost_per_minute_cents = int(unrounded_per_min.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    
    return {
        "total_cost_cents": total_cost_cents,
        "total_cost_formatted": format_cents(total_cost_cents),
        "cost_per_minute_cents": cost_per_minute_cents,
        "cost_per_minute_formatted": format_cents(cost_per_minute_cents)
    }
```

---

## 📦 Part 7: Final Submission Package Layout

The submission archive is built under `subramanian_s1_hw1.zip` matching the rubric:

```
subramanian_s1_hw1/
├── README.md         # Student name, how to open the app, browser notes, AI reflection
├── brief_v1.md       # Initial six-part brief exactly as written
├── output_v1.png     # Screenshot of v1 output showing the initial build
├── diagnosis.md      # One-phrase diagnosis and 2-3 sentences of evidence
├── brief_v2.md       # Brief v2 with the single targeted change highlighted
├── test_table.md     # 9 test rows (input, expected, actual, pass/fail)
└── app/
    ├── index.html    # Standalone offline app (double-click to open)
    └── tests.html    # Bonus automated in-browser test runner (all green)
```

### Self-Assessment Against Marking Guidance:
- **Brief v1 (15 pts)**: All six parts present and specific.
- **Diagnosis (15 pts)**: Precise one-phrase diagnosis naming the missing constraint with evidence.
- **Brief v2 (15 pts)**: Exactly one targeted change marked.
- **Working App (25 pts)**: Opens offline by double-click; all money in whole cents; matches all 3 success criteria figures.
- **Edge Cases & Test Table (20 pts)**: 9 rows covering all required edge cases with hand-worked expected values.
- **Packaging & Honesty (10 pts)**: Correct zip name, clear README, candid AI-use notes.
- **Bonus Work**: In-browser test suite (`tests.html`), live meeting ticker, and companion Python engine.
