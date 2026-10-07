"""
meeting_cost.py - The Meeting Cost Calculator (Core Arithmetic Engine)

Day 2 Session 1 Homework: "The Missing Penny"
Author: Mani Subramanian

Core Bookkeeping Principles:
1. Never calculate money as floating-point dollars (prevents IEEE 754 precision drift).
2. All input dollar rates are parsed and converted immediately into integer cents.
3. Total rate per hour = Sum of (attendees * hourly_rate_in_cents) across all roles.
4. Meeting duration is tracked in integer minutes.
5. Exact formula:
     Total Cost (cents) = round((total_hourly_rate_cents * minutes) / 60)
     Cost Per Minute (cents) = round(total_hourly_rate_cents / 60) if minutes > 0 else 0
6. Rounding Rule:
     Standard Financial Rounding (Round Half Up):
     Half-cents (0.5 cents) round up to the next nearest whole cent.
     e.g., 1,662.5 cents -> 1,663 cents ($16.63).
7. Zero-Minute Invariant:
     When minutes == 0, cost per minute must return 0 cents ($0.00),
     NEVER division by zero, NaN, or Infinity.
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import List, Dict, Tuple, Union


def dollars_to_cents(amount_str: Union[str, float, int]) -> int:
    """
    Parses a dollar input string/number into an exact integer number of cents.
    
    Examples:
        "$85.00" -> 8500
        "47.50"  -> 4750
        "$62.75" -> 6275
        "150"    -> 15000
    
    Raises:
        ValueError: If input is negative, non-numeric, or contains invalid format.
    """
    if amount_str is None:
        raise ValueError("Hourly rate cannot be empty.")
    
    # Strip whitespace, dollar sign, and comma separators
    cleaned = str(amount_str).strip().replace("$", "").replace(",", "")
    
    if not cleaned:
        raise ValueError("Hourly rate cannot be empty.")
    
    try:
        val = Decimal(cleaned)
    except Exception:
        raise ValueError(f"Invalid hourly rate: '{amount_str}'. Must be a valid positive number.")
    
    if val < 0:
        raise ValueError(f"Hourly rate cannot be negative: '{amount_str}'.")
    
    # Convert dollars to cents using exact Decimal scaling
    # quantize to 1 cent using ROUND_HALF_UP
    cents = int((val * 100).quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    return cents


def format_cents(cents: int) -> str:
    """
    Formats integer cents into a standard human-readable currency string with commas.
    
    Examples:
        38250   -> "$382.50"
        14400000 -> "$144,000.00"
        1663    -> "$16.63"
        0       -> "$0.00"
    """
    if cents < 0:
        sign = "-"
        cents = abs(cents)
    else:
        sign = ""
    
    dollars = cents // 100
    remaining_cents = cents % 100
    
    # Format with comma thousand-separators and leading zero for cents
    return f"{sign}${dollars:,}.{remaining_cents:02d}"


def calculate_meeting_cost(
    roles: List[Dict[str, Union[str, int, float]]],
    minutes: int,
    max_attendees: int = 500,
    max_minutes: int = 1440  # 24 hours
) -> Dict[str, Union[int, str, bool]]:
    """
    Calculates total meeting cost and cost per minute in integer cents.
    
    Args:
        roles: List of dicts representing role rows.
               Each row: {"name": str, "attendees": int, "hourly_rate": str/float}
        minutes: Total meeting duration in integer minutes.
        max_attendees: Sensible upper limit safeguard.
        max_minutes: Sensible upper limit for meeting duration.
        
    Returns:
        A dictionary containing:
        - "total_cost_cents": int
        - "total_cost_formatted": str (e.g. "$382.50")
        - "cost_per_minute_cents": int
        - "cost_per_minute_formatted": str (e.g. "$8.50")
        - "total_attendees": int
        - "total_hourly_rate_cents": int
        - "warning": Optional string for large meetings
    """
    # 1. Validation for meeting minutes
    if minutes is None:
        raise ValueError("Meeting minutes cannot be empty.")
    
    if minutes < 0:
        raise ValueError("Meeting duration cannot be negative.")
        
    warning_msg = None
    if minutes > max_minutes:
        warning_msg = f"Notice: Meeting length exceeds {max_minutes // 60} hours. Verify if this is an all-day multi-session event."
    
    total_attendees = 0
    total_hourly_rate_cents = 0
    
    # 2. Accumulate attendees and hourly rates across valid roles
    for row in roles:
        raw_name = str(row.get("name", "")).strip()
        raw_attendees = row.get("attendees", 0)
        raw_rate = row.get("hourly_rate", 0)
        
        # If whole row is empty, skip gracefully
        if not raw_name and (raw_attendees == 0 or raw_attendees == "") and not raw_rate:
            continue
            
        try:
            attendees = int(raw_attendees)
        except (ValueError, TypeError):
            raise ValueError(f"Attendees count must be a non-negative integer, got '{raw_attendees}'.")
            
        if attendees < 0:
            raise ValueError(f"Attendees count cannot be negative: '{attendees}'.")
            
        rate_cents = dollars_to_cents(raw_rate) if raw_rate else 0
        
        total_attendees += attendees
        total_hourly_rate_cents += (attendees * rate_cents)
    
    # Safeguard check for massive meetings
    if total_attendees > max_attendees and not warning_msg:
        warning_msg = f"Notice: High attendance count ({total_attendees} people). Ensure figures reflect an all-hands or plenary event."
    
    # 3. Handle 0-minute edge case:
    # Cost per minute MUST NOT produce Division by Zero / NaN / Infinity!
    if minutes == 0 or total_hourly_rate_cents == 0:
        return {
            "total_cost_cents": 0,
            "total_cost_formatted": "$0.00",
            "cost_per_minute_cents": 0,
            "cost_per_minute_formatted": "$0.00",
            "total_attendees": total_attendees,
            "total_hourly_rate_cents": total_hourly_rate_cents,
            "warning": warning_msg
        }
    
    # 4. Standard Financial Calculation with Decimal precision (Round Half Up):
    # Total Cost = (total_hourly_rate_cents * minutes) / 60
    unrounded_total_cents = Decimal(total_hourly_rate_cents * minutes) / Decimal(60)
    total_cost_cents = int(unrounded_total_cents.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    
    # Cost Per Minute = total_hourly_rate_cents / 60
    unrounded_cost_per_min = Decimal(total_hourly_rate_cents) / Decimal(60)
    cost_per_minute_cents = int(unrounded_cost_per_min.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    
    return {
        "total_cost_cents": total_cost_cents,
        "total_cost_formatted": format_cents(total_cost_cents),
        "cost_per_minute_cents": cost_per_minute_cents,
        "cost_per_minute_formatted": format_cents(cost_per_minute_cents),
        "total_attendees": total_attendees,
        "total_hourly_rate_cents": total_hourly_rate_cents,
        "warning": warning_msg
    }


if __name__ == "__main__":
    print("=" * 65)
    print("THE MEETING COST CALCULATOR - PYTHON VERIFICATION ENGINE")
    print("=" * 65)

    # Test Case 1: 6 people at $85.00/hr for 45 minutes
    # Expected: $382.50 total, $8.50 per min
    res1 = calculate_meeting_cost([{"name": "Consultant", "attendees": 6, "hourly_rate": "$85.00"}], minutes=45)
    print(f"Test 1 (Success Criteria 1): Total={res1['total_cost_formatted']}, PerMin={res1['cost_per_minute_formatted']}")
    assert res1["total_cost_formatted"] == "$382.50"
    assert res1["cost_per_minute_formatted"] == "$8.50"

    # Test Case 2: 120 people at $150.00/hr for 8 hours (480 minutes)
    # Expected: $144,000.00 with comma formatting
    res2 = calculate_meeting_cost([{"name": "Senior Staff", "attendees": 120, "hourly_rate": 150.00}], minutes=480)
    print(f"Test 2 (Success Criteria 2): Total={res2['total_cost_formatted']}, PerMin={res2['cost_per_minute_formatted']}")
    assert res2["total_cost_formatted"] == "$144,000.00"

    # Test Case 3: 3 people at $47.50/hr for 7 minutes
    # 3 * 4750 * 7 / 60 = 1,662.5 cents -> Round half-up = 1,663 cents ($16.63)
    res3 = calculate_meeting_cost([{"name": "Planner", "attendees": 3, "hourly_rate": 47.50}], minutes=7)
    print(f"Test 3 (Success Criteria 3): Total={res3['total_cost_formatted']}, PerMin={res3['cost_per_minute_formatted']}")
    assert res3["total_cost_formatted"] == "$16.63"

    # Test Case 4: 0 minutes
    res4 = calculate_meeting_cost([{"name": "Director", "attendees": 5, "hourly_rate": 100.00}], minutes=0)
    print(f"Test 4 (0 Minutes): Total={res4['total_cost_formatted']}, PerMin={res4['cost_per_minute_formatted']}")
    assert res4["cost_per_minute_formatted"] == "$0.00"

    # Test Case 5: 0 attendees
    res5 = calculate_meeting_cost([{"name": "Director", "attendees": 0, "hourly_rate": 100.00}], minutes=60)
    print(f"Test 5 (0 Attendees): Total={res5['total_cost_formatted']}, PerMin={res5['cost_per_minute_formatted']}")
    assert res5["total_cost_formatted"] == "$0.00"

    print("\nAll core verification assertions passed successfully!")
