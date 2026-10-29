"""Tiny maintenance-booking logic used as a demo project for CI/CD (LW5)."""
from datetime import datetime


def overlaps(start_a: datetime, end_a: datetime, start_b: datetime, end_b: datetime) -> bool:
    """Return True if two time intervals overlap."""
    if end_a <= start_a or end_b <= start_b:
        raise ValueError("end must be later than start")
    return start_a < end_b and start_b < end_a


class Schedule:
    """Stores maintenance bookings for one technician."""

    def __init__(self):
        self._bookings = []

    def add(self, start: datetime, end: datetime, title: str) -> bool:
        """Add a booking. Returns False if the slot is already taken."""
        for b_start, b_end, _ in self._bookings:
            if overlaps(start, end, b_start, b_end):
                return False
        self._bookings.append((start, end, title))
        return True

    def count(self) -> int:
        return len(self._bookings)
