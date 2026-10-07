Blast radius: Low technical blast radius / isolated code change. The bug is localized strictly to reserve_stock() (and summary reporting in reservation_summary()). Existing data and other functions (release_stock, can_fulfil) are unaffected. Operationally, it affects orders attempting to claim 100% of remaining stock.

Core module ( inventory.py
): Manages stock items, free stock calculation (available - reserved), reservations, releases, and summaries in memory.

Symptom (

bug_report.txt
): Attempting to reserve the exact remaining stock (e.g., 6 units when 6 are free) fails silently and returns False.

Rules (

requirements.txt
):
Requests must succeed when requested quantity is less than or equal to free stock.
Hidden business rule: When reservations deplete free stock completely, the summary must report the SKU as out_of_stock.

Key Insight: can_fulfil() already uses <= correctly, but reserve_stock() uses a strict < check, creating an inconsistency and causing the reported bug
----

1. Boundary condition flaw in reserve_stock() (Line 22): The check requested < item.free_stock uses strict < instead of <=, causing exact-match orders to fail.
2. Incomplete summary logic in reservation_summary() (Lines 42–48): Fails to report out_of_stock status when all remaining free stock is consumed (violating Requirement 6).

Confirmation evidence:
When tested with available=10, reserved=4 (free_stock=6):

reserve_stock(demo, 5) $\rightarrow$ 5 < 6 is True (succeeds).
reserve_stock(demo, 6) $\rightarrow$ 6 < 6 is False (fails incorrectly).
Furthermore, can_fulfil() on Line 39 already uses <= (requested <= item.free_stock), proving the discrepancy within the module itself.
---

Here are the precise changes to make in 

inventory.py
:

Change 1: Fix boundary check in reserve_stock()
Change line 22 from < to <= so orders for all remaining free stock are accepted:
Change 2: Add out_of_stock reporting in reservation_summary()
Update reservation_summary() (lines 42–48) to satisfy Business Rule #6: