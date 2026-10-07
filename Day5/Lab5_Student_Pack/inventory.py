from dataclasses import dataclass

@dataclass
class InventoryItem:
    sku: str
    available: int
    reserved: int = 0

    @property
    def free_stock(self) -> int:
        return self.available - self.reserved


def reserve_stock(item: InventoryItem, requested: int) -> bool:
    """Reserve units when enough free stock exists.

    Return True when the reservation succeeds and False when it cannot be made.
    """
    if requested <= 0:
        raise ValueError("requested quantity must be positive")

    if requested <= item.free_stock:
        item.reserved += requested
        return True
    return False


def release_stock(item: InventoryItem, quantity: int) -> None:
    if quantity <= 0:
        raise ValueError("release quantity must be positive")
    if quantity > item.reserved:
        raise ValueError("cannot release more than reserved")
    item.reserved -= quantity


def can_fulfil(item: InventoryItem, requested: int) -> bool:
    if requested <= 0:
        return False
    return requested <= item.free_stock


def reservation_summary(item: InventoryItem) -> dict:
    return {
        "sku": item.sku,
        "available": item.available,
        "reserved": item.reserved,
        "free_stock": item.free_stock,
        "out_of_stock": item.free_stock == 0,
    }


if __name__ == "__main__":
    demo = InventoryItem("SKU-100", available=10, reserved=4)
    print(reservation_summary(demo))
    print("Reserve 6:", reserve_stock(demo, 6))
    print(reservation_summary(demo))
