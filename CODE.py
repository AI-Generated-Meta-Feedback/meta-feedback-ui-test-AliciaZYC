def sortBooks(books):
    for i in range(1, len(books)):
        curr = books[i]
        j = i - 1
        
        while j >= 0 and shouldSwap(books[j], curr):
            books[j + 1] = books[j]
            j -= 1
        
        books[j + 1] = curr
    
    return books


def shouldSwap(bookA, bookB):
    if bookA['shelfNumber'] > bookB['shelfNumber']:
        return True
    elif bookA['shelfNumber'] == bookB['shelfNumber']:
        if bookA['returnOrder'] > bookB['returnOrder']:
            return True
    return False
