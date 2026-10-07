import pytest
from inventory import InventoryItem, reserve_stock, release_stock, can_fulfil, reservation_summary


def test_reserve_exact_remaining_stock():
    """Requirement 1: A request equal to free stock must succeed."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=4)
    # free_stock is 6
    assert reserve_stock(item, 6) is True
    assert item.reserved == 10
    assert item.free_stock == 0


def test_reserve_less_than_free_stock():
    """Requirement 1: A request less than free stock must succeed."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=4)
    assert reserve_stock(item, 5) is True
    assert item.reserved == 9
    assert item.free_stock == 1


def test_reserve_greater_than_free_stock():
    """Requirement 2: A request greater than free stock must return False and not change state."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=4)
    assert reserve_stock(item, 7) is False
    # Ensure state did not change
    assert item.available == 10
    assert item.reserved == 4
    assert item.free_stock == 6


def test_reserve_zero_and_negative():
    """Requirement 3: Zero or negative requests must raise ValueError."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=4)
    with pytest.raises(ValueError, match="requested quantity must be positive"):
        reserve_stock(item, 0)
    with pytest.raises(ValueError, match="requested quantity must be positive"):
        reserve_stock(item, -5)


def test_reserved_does_not_exceed_available():
    """Requirement 4: Reserved stock must never exceed available stock."""
    item = InventoryItem(sku="SKU-100", available=5, reserved=0)
    assert reserve_stock(item, 5) is True
    assert reserve_stock(item, 1) is False
    assert item.reserved <= item.available


def test_release_stock_valid():
    """Requirement 5: Releasing valid quantity decreases reserved stock."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=6)
    release_stock(item, 4)
    assert item.reserved == 2
    assert item.free_stock == 8


def test_release_stock_invalid():
    """Requirement 5: Release quantity must be positive and cannot exceed currently reserved."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=4)
    with pytest.raises(ValueError, match="release quantity must be positive"):
        release_stock(item, 0)
    with pytest.raises(ValueError, match="release quantity must be positive"):
        release_stock(item, -1)
    with pytest.raises(ValueError, match="cannot release more than reserved"):
        release_stock(item, 5)


def test_out_of_stock_reporting_in_summary():
    """Requirement 6: When all free stock is consumed, out_of_stock must be True in summary."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=4)
    summary_initial = reservation_summary(item)
    assert summary_initial["out_of_stock"] is False

    # Consume all free stock
    assert reserve_stock(item, 6) is True
    summary_depleted = reservation_summary(item)
    assert summary_depleted["out_of_stock"] is True
    assert summary_depleted["free_stock"] == 0

    # Release 1 unit and verify out_of_stock returns to False
    release_stock(item, 1)
    summary_restored = reservation_summary(item)
    assert summary_restored["out_of_stock"] is False
    assert summary_restored["free_stock"] == 1


def test_can_fulfil():
    """Verify can_fulfil logic."""
    item = InventoryItem(sku="SKU-100", available=10, reserved=4)
    assert can_fulfil(item, 6) is True
    assert can_fulfil(item, 5) is True
    assert can_fulfil(item, 7) is False
    assert can_fulfil(item, 0) is False
    assert can_fulfil(item, -1) is False


def test_sequential_reservations():
    """Test multiple sequential reservations up to exhaustion."""
    item = InventoryItem(sku="SKU-100", available=6, reserved=0)
    assert reserve_stock(item, 2) is True
    assert reserve_stock(item, 2) is True
    assert reserve_stock(item, 2) is True
    assert reservation_summary(item)["out_of_stock"] is True
    assert reserve_stock(item, 1) is False
