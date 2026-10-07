# Brief v1: The Meeting Cost Calculator

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
Rounding: Round half up to the nearest whole cent.
If there are 0 attendees: Total cost and cost per minute should show $0.00.
If the length is 0 minutes: Total cost should show $0.00.
If unsure: Default to simple, clean vanilla JS with clear readable labels and reactive live updating.

EXAMPLES:
<example>
Input: 6 people at $85.00/hour for 45 minutes -> Total: $382.50 Per minute: $8.50
</example>
