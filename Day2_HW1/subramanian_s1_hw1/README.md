# The Meeting Cost Calculator

**Student Name**: Mani Subramanian  
**Assignment**: Day 2 Session 1 Homework — "The Missing Penny"  
**Course**: Vibe Coding Workshop (Core Prompting Concepts & Tools)  

---

## 🚀 How to Open the App

1. Navigate to the `app/` folder.
2. Double-click `index.html` to open it in your default web browser.
   - **Alternative via Terminal (macOS)**:
     ```bash
     open app/index.html
     ```
3. No installations, npm packages, web servers, or internet connection are required. The calculator runs completely offline.

---

## 🌐 Browser Tested In

- **Google Chrome**: Version 131+ (macOS Sonoma / Sequoia)
- **Apple Safari**: Version 18+ (macOS)
- **Mozilla Firefox**: Version 133+ (macOS)

---

## 📝 Honest AI-Use Notes

1. **Brief Formulation**:
   - I started by manually calculating all edge cases on paper before prompting the AI, establishing our baseline truth (especially the 1,662.5¢ fractional cent case and 0-minute division safeguard).
   - I filled out the six-part brief skeleton for v1.
2. **Diagnosis & Iteration**:
   - In v1, the model handled 0 minutes on total cost, but neglected cost-per-minute division by zero, resulting in `Infinity`.
   - Instead of rewriting everything, I formulated a single precise diagnosis: `"missing constraint: cost per minute when meeting duration is 0 minutes must explicitly display $0.00 instead of evaluating division by zero"`.
   - In v2, I changed exactly that one constraint, resolving the bug without introducing regressions.
3. **Integer-Cent Arithmetic Verification**:
   - I authored a companion Python verification script (`meeting_cost.py`) and pytest suite (`test_meeting_cost.py`) to mathematically guarantee zero floating-point penny drift.
4. **Bonus Challenges Included**:
   - Integrated an in-browser automated test suite in `app/tests.html` (inspired by FairShare).
   - Added a live "Meeting So Far" ticker tracking accrued cost in real time.
