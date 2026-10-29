from datetime import datetime

import pytest

from app.scheduler import Schedule, overlaps


def t(hour):
    return datetime(2026, 11, 2, hour, 0)


def test_overlapping_intervals():
    assert overlaps(t(9), t(11), t(10), t(12)) is True


def test_adjacent_intervals_do_not_overlap():
    assert overlaps(t(9), t(10), t(10), t(11)) is False


def test_invalid_interval_raises():
    with pytest.raises(ValueError):
        overlaps(t(11), t(9), t(10), t(12))


def test_schedule_accepts_free_slot():
    s = Schedule()
    assert s.add(t(9), t(10), "Boiler check") is True
    assert s.count() == 1


def test_schedule_rejects_busy_slot():
    s = Schedule()
    s.add(t(9), t(11), "Boiler check")
    assert s.add(t(10), t(12), "Pump repair") is False
    assert s.count() == 1
