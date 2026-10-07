# Test Table: The Meeting Cost Calculator

All **Expected** values were independently calculated by hand using integer-cent arithmetic before comparing with the actual application output.

Rounding convention: Standard Financial Rounding (Round Half Up). Half-cents ($0.005) round up to the nearest whole cent ($0.01).

| Test # | Test Description & Inputs | Expected (Calculated by Hand) | Actual (App Result) | Pass / Fail |
| :---: | :--- | :--- | :--- | :---: |
| **1** | **Standard Meeting (Success Criteria 1)**<br>6 attendees @ $85.00/hr, 45 minutes | **Total:** $382.50<br>**Per Min:** $8.50<br>*(6 × 8,500¢ = 51,000¢/hr; 51,000 × 45 / 60 = 38,250¢; 51,000 / 60 = 850¢)* | Total: $382.50<br>Per Min: $8.50 | **PASS** |
| **2** | **Large Offsite Meeting (Success Criteria 2)**<br>120 attendees @ $150.00/hr, 8 hours (480 mins) | **Total:** $144,000.00<br>**Per Min:** $300.00<br>*(120 × 15,000¢ = 1,800,000¢/hr; 1,800,000 × 8 = 14,400,000¢)* | Total: $144,000.00<br>Per Min: $300.00 | **PASS** |
| **3** | **Fractional Cent Rounding (Success Criteria 3)**<br>3 attendees @ $47.50/hr, 7 minutes | **Total:** $16.63<br>**Per Min:** $2.38<br>*(3 × 4,750¢ × 7 / 60 = 1,662.5¢ &rarr; rounds to 1,663¢; 14,250 / 60 = 237.5¢ &rarr; 238¢)* | Total: $16.63<br>Per Min: $2.38 | **PASS** |
| **4** | **Zero Duration Edge Case**<br>5 attendees @ $100.00/hr, 0 minutes | **Total:** $0.00<br>**Per Min:** $0.00<br>*(No NaN, Infinity, or division-by-zero errors)* | Total: $0.00<br>Per Min: $0.00 | **PASS** |
| **5** | **Zero Attendees Edge Case**<br>0 attendees @ $120.00/hr, 60 minutes | **Total:** $0.00<br>**Per Min:** $0.00<br>*(Empty meeting produces clean zero)* | Total: $0.00<br>Per Min: $0.00 | **PASS** |
| **6** | **Decimal Rates & Multi-Tier Committee**<br>Row 1: 2 Chairs @ $100.00/hr<br>Row 2: 4 Planners @ $62.75/hr<br>Duration: 30 minutes | **Total:** $225.50<br>**Per Min:** $7.52<br>*(Total rate: 20,000¢ + 25,100¢ = 45,100¢/hr; 45,100 × 30 / 60 = 22,550¢; 45,100 / 60 = 751.67¢ &rarr; 752¢)* | Total: $225.50<br>Per Min: $7.52 | **PASS** |
| **7** | **Large Meeting Upper Bound Threshold**<br>520 attendees @ $100.00/hr, 60 minutes | **Total:** $52,000.00<br>**Notice:** Displays friendly warning above 500 attendees confirming all-hands scale | Total: $52,000.00<br>Notice displayed: "Notice: Large meeting (520 attendees)..." | **PASS** |
| **8** | **Negative Input Validation**<br>Attendee: -3, Rate: $50.00, Minutes: 45 | **Refused with friendly error**<br>*(Total and Per Min display $0.00; error message shown)* | Total: $0.00<br>Error: "Attendee counts must be non-negative whole numbers." | **PASS** |
| **9** | **Non-Numeric / Invalid Rate Input**<br>Attendee: 4, Rate: "abc", Minutes: 45 | **Refused with friendly error**<br>*(Total and Per Min display $0.00; error message shown)* | Total: $0.00<br>Error: "Hourly rates must be valid positive numbers." | **PASS** |
