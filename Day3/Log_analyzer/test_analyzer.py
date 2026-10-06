#!/usr/bin/env python3
"""
Test script for Log Analyzer.
Runs the analyzer against both sample logs (suspicious and clean)
without requiring the GUI.
"""

import os
import sys
from collections import defaultdict
import log_analyzer

def run_tests():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    sample_dir = os.path.join(base_dir, "Sample logs")
    
    suspicious_log = os.path.join(sample_dir, "Sample_Suspicious_log.log")
    clean_log = os.path.join(sample_dir, "Sample_unsuspicious_log.log")
    
    print("=" * 55)
    print(" LOG ANALYZER TEST SUITE")
    print("=" * 55)
    
    # Test 1: Suspicious log
    print("\n[TEST 1] Scanning Suspicious Log...")
    print(f"File: {suspicious_log}")
    if not os.path.exists(suspicious_log):
        print("ERROR: File not found!")
        return False
        
    threats, total_lines = log_analyzer.analyze_log_file(suspicious_log)
    print(f"-> Total lines scanned: {total_lines}")
    print(f"-> Suspicious activities found: {sum(threats.values())}")
    for threat, count in threats.items():
        remedy = log_analyzer.remedies.get(threat, "No remedy specified.")
        print(f"   • {threat} ({count} occurrences)")
        print(f"     {remedy}")
        
    if threats:
        print("✔ Test 1 Passed: Detected threats as expected.")
    else:
        print("✘ Test 1 Failed: Expected threats, but none were detected.")

    # Test 2: Clean log
    print("\n[TEST 2] Scanning Clean Log...")
    print(f"File: {clean_log}")
    if not os.path.exists(clean_log):
        print("ERROR: File not found!")
        return False

    clean_threats, clean_lines = log_analyzer.analyze_log_file(clean_log)
    print(f"-> Total lines scanned: {clean_lines}")
    print(f"-> Suspicious activities found: {len(clean_threats)}")
    
    if len(clean_threats) == 0:
        print("✔ Test 2 Passed: 0 suspicious activities detected in clean log.")
    else:
        print("✘ Test 2 Failed: False positives detected in clean log.")

    print("\n" + "=" * 55)
    print(" ALL TESTS COMPLETE")
    print("=" * 55)
    return True

if __name__ == "__main__":
    run_tests()
