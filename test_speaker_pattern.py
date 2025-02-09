from ast import main
import sys
from pathlib import Path
project_root = str(Path(__file__).parent)
sys.path.append(project_root)

import re
from utils.speaker import is_new_speaker, get_speaker_name

# Test cases with diverse name patterns
test_cases = [
    # Single letter initial patterns
    "K Krithivasan: This is a test",
    "K. Krithivasan: With period",
    "N Shah: Single letter with name",
    "N. Shah: Single letter with period and name",
    "K Krithivasan: Single letter initial",
    "V Raju: Another single letter name",
    
    # Initials patterns
    "R.K. Chaudhary: This is a test",
    "R.K.Chaudhary: No space between initials",
    "A.B.C. Kumar: Multiple initials",
    "P. Kumar: Single initial",
    "G. S. Chahal: Single initial with space",
    "G.S. Chahal: Single initial with no space between initials",
    "K. R. S. Murthy: Multiple initials with spaces",
    "K.R.S. Murthy: Multiple initials without spaces",
    "Laxman Rao J: Single letter parts of a name not having period(.)",
    
    # Traditional Indian names
    "Rajesh Kumar: Simple two-part name",
    "Ram Prasad Singh: Three-part name",
    
    # Western names
    "John Smith: Western name",
    "Mary J. Williams: Western name with middle initial",
    "Robert A. B. Johnson: Western name with multiple initials",
    
    # Professional titles
    "Dr. Patel: With title",
    "Dr.Patel: Title without space",
    "Mr. S.K. Sharma: Title with initials",
    "Mr.S.K.Sharma: Title and initials without spaces",
    "Mr. K Krithivasan: Title with single letter initial",
    "Dr. N Shah: Title with single letter initial",
    
    # Names that should not match
    "Subject: This should not match",
    "Symbol: This should not match",
    "MODERATOR: This should not match",
    "MANAGEMENT: This should not match",
    "Scrip Code: This should not match",
    "Series: This should not match"
]

def run_speaker_pattern_tests():
    print("Testing speaker recognition patterns:")
    print("-" * 50)
    
    passed = 0
    total = len(test_cases)
    
    for test in test_cases:
        result = is_new_speaker(test)
        # Determine if this is a negative test case (should not match)
        should_match = not any(test.startswith(x) for x in ["Subject:", "Symbol:", "MODERATOR:", "MANAGEMENT:", "Scrip Code:", "Series:"])
        is_correct = result == should_match
        
        status = "✓" if is_correct else "✗"
        print(f"{status} '{test}' -> {result}")
        
        if is_correct:
            passed += 1
    
    print("-" * 50)
    print(f"Results: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")

def run_name_normalization_tests():
    print("\nTesting speaker name normalization:")
    print("-" * 50)
    
    test_normalization = [
        ("G.S. Chahal: Test", "G. S. Chahal"),
        ("K.R.S. Murthy: Test", "K. R. S. Murthy"),
        ("R.K.Chaudhary: Test", "R. K. Chaudhary"),
        ("John Smith: Test", "John Smith"),
        ("Dr.A.B.Shah: Test", "Dr. A. B. Shah"),
        ("Mr.S.K.Sharma: Test", "Mr. S. K. Sharma"),
        ("Dr.Patel: Test", "Dr. Patel"),
        ("K Krithivasan: Test", "K Krithivasan"),
        ("K. Krithivasan: Test", "K. Krithivasan"),
        ("N Shah: Test", "N Shah"),
        ("N. Shah: Test", "N. Shah"),
        ("Mr. K Krithivasan: Test", "Mr. K Krithivasan"),
        ("Dr. N Shah: Test", "Dr. N Shah")
    ]
    
    passed = 0
    total = len(test_normalization)
    
    for test_input, expected in test_normalization:
        result = get_speaker_name(test_input)
        is_correct = result == expected
        status = "✓" if is_correct else "✗"
        print(f"{status} '{test_input}' -> '{result}' (Expected: '{expected}')")
        
        if is_correct:
            passed += 1
    
    print("-" * 50)
    print(f"Results: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")

if __name__ == "__main__":
    run_speaker_pattern_tests()
    run_name_normalization_tests()
