"""CLI for Memory Leak Tracker."""
import argparse
from .core import DynamicMemoryLeakTracker

def main():
    parser = argparse.ArgumentParser(description="Memory Leak Tracker CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate leak detection")
    args = parser.parse_args()

    tracker = DynamicMemoryLeakTracker(threshold_growth_ratio=2.0)
    tracker.record_snapshot({"listeners": 20, "sessions": 5})
    alert = tracker.record_snapshot({"listeners": 50, "sessions": 5})

    if alert:
        print(f"ALERT: {alert.message}")
    else:
        print("Memory allocation healthy.")

if __name__ == "__main__":
    main()
