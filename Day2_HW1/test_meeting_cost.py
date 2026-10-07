"""
test_meeting_cost.py - Unit test suite for The Meeting Cost Calculator

Day 2 Session 1 Homework: "The Missing Penny"
Validates all 8+ edge cases and PDF success criteria numbers.
"""

import pytest
from meeting_cost import dollars_to_cents, format_cents, calculate_meeting_cost


class TestDollarsToCents:
    """Tests parsing and converting dollar strings into integer cents."""

    def test_standard_formats(self):
        assert dollars_to_cents("$85.00") == 8500
        assert dollars_to_cents("85") == 8500
        assert dollars_to_cents("$47.50") == 4750
        assert dollars_to_cents("62.75") == 6275
        assert dollars_to_cents("150.00") == 15000

    def test_comma_formatting(self):
        assert dollars_to_cents("$1,250.50") == 125050
        assert dollars_to_cents("1,000") == 100000

    def test_single_decimal_digit(self):
        assert dollars_to_cents("47.5") == 4750

    def test_negative_rates_raise_error(self):
        with pytest.raises(ValueError, match="cannot be negative"):
            dollars_to_cents("-50.00")

    def test_non_numeric_rates_raise_error(self):
        with pytest.raises(ValueError, match="Invalid hourly rate"):
            dollars_to_cents("abc")


class TestCurrencyFormatting:
    """Tests formatting integer cents into standard dollar strings."""

    def test_zero(self):
        assert format_cents(0) == "$0.00"

    def test_cents_under_dollar(self):
        assert format_cents(5) == "$0.05"
        assert format_cents(50) == "$0.50"

    def test_thousand_separator(self):
        assert format_cents(38250) == "$382.50"
        assert format_cents(14400000) == "$144,000.00"


class TestMeetingCostEdgeCases:
    """
    Test all 8 required edge cases and success criteria:
    1. Standard meeting (6 people, $85/hr, 45 mins)
    2. Large meeting (120 people, $150/hr, 480 mins)
    3. Fractional half-cent (3 people, $47.50/hr, 7 mins)
    4. Multi-role meeting with decimal rates ($62.75/hr)
    5. Zero attendees
    6. Zero minutes (division by zero safeguard)
    7. Negative attendees/rates
    8. Non-numeric input
    """

    def test_success_criterion_1_standard(self):
        """6 people at $85.00 an hour for 45 minutes -> $382.50 and $8.50 per min."""
        roles = [{"name": "Consultant", "attendees": 6, "hourly_rate": 85.00}]
        res = calculate_meeting_cost(roles, minutes=45)
        assert res["total_cost_formatted"] == "$382.50"
        assert res["cost_per_minute_formatted"] == "$8.50"

    def test_success_criterion_2_large_meeting(self):
        """120 people at $150.00 an hour for 8 hours (480 mins) -> $144,000.00."""
        roles = [{"name": "Participant", "attendees": 120, "hourly_rate": "$150.00"}]
        res = calculate_meeting_cost(roles, minutes=480)
        assert res["total_cost_formatted"] == "$144,000.00"
        assert res["cost_per_minute_formatted"] == "$300.00"

    def test_success_criterion_3_fractional_half_cent(self):
        """
        3 people at $47.50 an hour for 7 minutes:
        3 * 4750 * 7 / 60 = 1,662.5 cents -> Round half-up to 1,663 cents = $16.63.
        Cost per minute: 3 * 4750 / 60 = 237.5 cents -> Round half-up to 238 cents = $2.38.
        """
        roles = [{"name": "Associate", "attendees": 3, "hourly_rate": "47.50"}]
        res = calculate_meeting_cost(roles, minutes=7)
        assert res["total_cost_cents"] == 1663
        assert res["total_cost_formatted"] == "$16.63"
        assert res["cost_per_minute_cents"] == 238
        assert res["cost_per_minute_formatted"] == "$2.38"

    def test_multi_role_with_decimals(self):
        """Multi-role team with decimal rate of $62.75."""
        roles = [
            {"name": "Manager", "attendees": 2, "hourly_rate": "100.00"},  # 200/hr
            {"name": "Developer", "attendees": 4, "hourly_rate": "62.75"},  # 251/hr
        ]
        # Total rate = 200 + 251 = 451 dollars/hr = 45100 cents/hr
        # For 60 mins: 45100 cents = $451.00
        # Cost per minute: 45100 / 60 = 751.666... -> 752 cents ($7.52)
        res = calculate_meeting_cost(roles, minutes=60)
        assert res["total_cost_formatted"] == "$451.00"
        assert res["cost_per_minute_formatted"] == "$7.52"

    def test_zero_attendees(self):
        """0 attendees returns $0.00 for both total and per minute."""
        roles = [{"name": "Lead", "attendees": 0, "hourly_rate": 120.00}]
        res = calculate_meeting_cost(roles, minutes=45)
        assert res["total_cost_formatted"] == "$0.00"
        assert res["cost_per_minute_formatted"] == "$0.00"

    def test_all_rows_empty(self):
        """Completely empty role list returns $0.00."""
        res = calculate_meeting_cost([], minutes=60)
        assert res["total_cost_formatted"] == "$0.00"
        assert res["cost_per_minute_formatted"] == "$0.00"

    def test_zero_minutes_safeguard(self):
        """0 minutes must return $0.00, NEVER NaN, Infinity, or error."""
        roles = [{"name": "Director", "attendees": 5, "hourly_rate": 150.00}]
        res = calculate_meeting_cost(roles, minutes=0)
        assert res["total_cost_formatted"] == "$0.00"
        assert res["cost_per_minute_formatted"] == "$0.00"
        assert "NaN" not in res["cost_per_minute_formatted"]
        assert "Infinity" not in res["cost_per_minute_formatted"]

    def test_negative_minutes_refused(self):
        """Negative meeting duration raises ValueError."""
        roles = [{"name": "Team", "attendees": 2, "hourly_rate": 50.00}]
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_meeting_cost(roles, minutes=-15)

    def test_negative_attendees_refused(self):
        """Negative attendees count raises ValueError."""
        roles = [{"name": "Team", "attendees": -3, "hourly_rate": 50.00}]
        with pytest.raises(ValueError, match="cannot be negative"):
            calculate_meeting_cost(roles, minutes=30)

    def test_upper_limit_warning(self):
        """Exceeding 24 hours triggers friendly upper-limit warning."""
        roles = [{"name": "Retreat", "attendees": 10, "hourly_rate": 50.00}]
        res = calculate_meeting_cost(roles, minutes=1500)
        assert res["warning"] is not None
        assert "exceeds" in res["warning"]
