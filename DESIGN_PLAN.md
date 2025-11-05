I am going to choose Insertion Sort, as there are only 25 books, and it's a stable sorting algorithm.

We're gonna first compare the shelfNumber: the smaller shelf would be at the beginning. For the same shelfNumber, the one with smaller returnOrder would be at the beginning.

Thus, Book A < Book B only when:
- shelfNumber < B.shelfNumber OR
- shelfNumber == B.shelfNumber AND A.returnOrder < B.returnOrder

Complexity:
Time： O(n²) , Best case O(n) with already sorted.
