"""Core dynamic memory leak tracker implementation."""
from typing import Dict, List, Optional

class LeakAlert:
    def __init__(self, key: str, growth_rate: float, message: str):
        self.key = key
        self.growth_rate = growth_rate
        self.message = message

class DynamicMemoryLeakTracker:
    def __init__(self, threshold_growth_ratio: float = 2.0):
        self.threshold = threshold_growth_ratio
        self.snapshots: List[Dict[str, int]] = []

    def record_snapshot(self, object_counts: Dict[str, int]) -> Optional[LeakAlert]:
        self.snapshots.append(dict(object_counts))
        if len(self.snapshots) < 2:
            return None

        prev = self.snapshots[-2]
        curr = self.snapshots[-1]

        for k, curr_count in curr.items():
            prev_count = prev.get(k, 0)
            if prev_count > 10 and curr_count >= prev_count * self.threshold:
                return LeakAlert(k, curr_count / prev_count, f"Monotonic leak detected on '{k}': grew from {prev_count} to {curr_count}")
        return None
