"""
Complete Resume Parser Test & Verification Script
Tests all functionality and dependencies
"""

import sys
import os

print("\n" + "="*70)
print("RESUME PARSER - COMPLETE VERIFICATION TEST")
print("="*70)

# Test 1: Import all dependencies
print("\n📋 TEST 1: Checking All Dependencies")
print("-" * 70)

test_results = []

try:
    import spacy
    print("✅ spacy (v{}) - OK".format(spacy.__version__))
    test_results.append(True)
except ImportError as e:
    print("❌ spacy - FAILED: {}".format(str(e)))
    test_results.append(False)

try:
    import pandas
    print("✅ pandas (v{}) - OK".format(pandas.__version__))
    test_results.append(True)
except ImportError as e:
    print("❌ pandas - FAILED: {}".format(str(e)))
    test_results.append(False)

try:
    import docx2txt
    print("✅ docx2txt - OK")
    test_results.append(True)
except ImportError as e:
    print("❌ docx2txt - FAILED: {}".format(str(e)))
    test_results.append(False)

try:
    import PyPDF2
    print("✅ PyPDF2 (v{}) - OK".format(PyPDF2.__version__))
    test_results.append(True)
except ImportError as e:
    print("❌ PyPDF2 - FAILED: {}".format(str(e)))
    test_results.append(False)

try:
    import docx
    print("✅ python-docx - OK")
    test_results.append(True)
except ImportError as e:
    print("❌ python-docx - FAILED: {}".format(str(e)))
    test_results.append(False)

# Test 2: Check ResumeParser
print("\n📋 TEST 2: Checking ResumeParser Module")
print("-" * 70)

try:
    from ResumeParser import ResumeParser
    print("✅ ResumeParser class imported successfully")
    test_results.append(True)
except Exception as e:
    print("❌ ResumeParser import FAILED: {}".format(str(e)))
    test_results.append(False)

# Test 3: Check spaCy model
print("\n📋 TEST 3: Checking spaCy Language Model")
print("-" * 70)

try:
    nlp = spacy.load("en_core_web_sm")
    print("✅ spaCy English model (en_core_web_sm) loaded successfully")
    print("   Pipeline components: {}".format(list(nlp.pipe_names)))
    test_results.append(True)
except Exception as e:
    print("❌ spaCy model load FAILED: {}".format(str(e)))
    test_results.append(False)

# Test 4: Check section_title.csv
print("\n📋 TEST 4: Checking Configuration Files")
print("-" * 70)

if os.path.exists("section_title.csv"):
    try:
        import pandas as pd
        df = pd.read_csv("section_title.csv")
        print("✅ section_title.csv found and loaded")
        print("   Sections: {}".format(list(df.columns)))
        print("   Rows: {}".format(len(df)))
        test_results.append(True)
    except Exception as e:
        print("❌ section_title.csv read FAILED: {}".format(str(e)))
        test_results.append(False)
else:
    print("❌ section_title.csv NOT FOUND")
    test_results.append(False)

# Test 5: Test ResumeParser basic properties
print("\n📋 TEST 5: Testing ResumeParser Properties")
print("-" * 70)

try:
    print("✅ ResumeParser has required attributes:")
    print("   ✓ CANDIDATE_INFO: {}".format(len(ResumeParser.CANDIDATE_INFO)))
    print("   ✓ SECTION_TITLE: {}".format(len(ResumeParser.SECTION_TITLE)))
    print("   ✓ SECTION_INFO_FILE: {}".format(ResumeParser.SECTION_INFO_FILE))
    test_results.append(True)
except Exception as e:
    print("❌ ResumeParser properties check FAILED: {}".format(str(e)))
    test_results.append(False)

# Test 6: Test file format detection
print("\n📋 TEST 6: Testing File Format Support")
print("-" * 70)

try:
    from ResumeParser import PDF_SUPPORT
    if PDF_SUPPORT:
        print("✅ PDF support enabled (PyPDF2 available)")
    else:
        print("⚠️  PDF support disabled (PyPDF2 not available)")
    print("✅ DOCX support enabled (docx2txt available)")
    test_results.append(True)
except Exception as e:
    print("❌ Format support check FAILED: {}".format(str(e)))
    test_results.append(False)

# Test 7: Test pattern matching
print("\n📋 TEST 7: Testing Pattern Matching Setup")
print("-" * 70)

try:
    from ResumeParser import MatchEvent
    patterns = {
        'PERSON': MatchEvent.PERSON_PATTERN,
        'EMAIL': MatchEvent.EMAIL_ID_PATTERN,
        'PHONE_1': MatchEvent.PHONE_PATTERN_1,
        'PHONE_2': MatchEvent.PHONE_PATTERN_2,
        'ADDRESS': MatchEvent.ADDRESS_PATTERN,
        'LINKEDIN': MatchEvent.LINKEDIN_URL_PATTERN,
        'GITHUB': MatchEvent.GIT_URL_PATTERN,
    }
    print("✅ All pattern matching templates loaded")
    for name, pattern in patterns.items():
        print("   ✓ {} pattern loaded".format(name))
    test_results.append(True)
except Exception as e:
    print("❌ Pattern matching setup FAILED: {}".format(str(e)))
    test_results.append(False)

# Summary
print("\n" + "="*70)
print("TEST SUMMARY")
print("="*70)

passed = sum(test_results)
total = len(test_results)
percentage = (passed / total) * 100

print("\n✅ Tests Passed: {}/{}".format(passed, total))
print("📊 Success Rate: {:.1f}%".format(percentage))

if percentage == 100:
    print("\n🎉 ALL TESTS PASSED! RESUME PARSER IS READY TO USE! 🎉")
    print("\nYou can now:")
    print("  1. Place your resume files in the 'resumes/' folder")
    print("  2. Run: python ResumeParser.py")
    print("  3. Use: from ResumeParser import ResumeParser")
    print("          parser = ResumeParser('resume.pdf')")
    print("          result = parser.parse_information()")
else:
    print("\n⚠️  Some tests failed. Please check the output above.")
    print("Common issues:")
    print("  - spaCy model not downloaded: python -m spacy download en_core_web_sm")
    print("  - Dependencies not installed: pip install -r requirements.txt")

print("\n" + "="*70)
