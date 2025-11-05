

def test_sortBooks():
    
    # Test 1: Different shelves
    books1 = [
        {'shelfNumber': 5, 'returnOrder': 1},
        {'shelfNumber': 2, 'returnOrder': 1},
        {'shelfNumber': 8, 'returnOrder': 1}
    ]
    result1 = sortBooks(books1.copy())
    print(f"✓ PASS\n" if result1[0]['shelfNumber'] == 2 and result1[-1]['shelfNumber'] == 8 else f"✗ FAIL\n")
    
    # Test 2: Same shelf (stability test)
    books2 = [
        {'shelfNumber': 5, 'returnOrder': 3},
        {'shelfNumber': 5, 'returnOrder': 1},
        {'shelfNumber': 5, 'returnOrder': 2}
    ]
    result2 = sortBooks(books2.copy())
    print(f"✓ PASS\n" if result2 == books2 else f"✗ FAIL\n")
    
    # Test 3: Mixed shelves
    books3 = [
        {'shelfNumber': 5, 'returnOrder': 3},
        {'shelfNumber': 2, 'returnOrder': 1},
        {'shelfNumber': 5, 'returnOrder': 2}
    ]
    result3 = sortBooks(books3.copy())
    expected = [
        {'shelfNumber': 2, 'returnOrder': 1},
        {'shelfNumber': 5, 'returnOrder': 3},
        {'shelfNumber': 5, 'returnOrder': 2}
    ]
    print(f"✓ PASS" if result3 == expected else f"✗ FAIL")

test_sortBooks()
