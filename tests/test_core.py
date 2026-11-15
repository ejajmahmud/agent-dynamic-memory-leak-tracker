"""Automated test suite for Memory Leak Tracker."""
import unittest
from agent_dynamic_memory_leak_tracker.core import DynamicMemoryLeakTracker

class TestDynamicMemoryLeakTracker(unittest.TestCase):
    def test_leak_detection_trigger(self):
        tracker = DynamicMemoryLeakTracker(threshold_growth_ratio=2.0)
        self.assertIsNone(tracker.record_snapshot({"cache": 100}))
        alert = tracker.record_snapshot({"cache": 250})
        self.assertIsNotNone(alert)
        self.assertIn("Monotonic leak", alert.message)
