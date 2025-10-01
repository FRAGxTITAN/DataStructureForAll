def bucket_search(arr, key):
    if not arr:
        return -1

    # Step 1: Find range of elements
    max_val = max(arr)
    min_val = min(arr)
    bucket_count = len(arr) // 2 or 1  # number of buckets
    bucket_size = (max_val - min_val) / bucket_count + 1

    # Step 2: Create empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Step 3: Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) // bucket_size)
        buckets[index].append(num)

    # Step 4: Sort each bucket
    for b in buckets:
        b.sort()

    # Step 5: Search in correct bucket
    bucket_index = int((key - min_val) // bucket_size)
    if 0 <= bucket_index < bucket_count:
        if key in buckets[bucket_index]:
            return True  # Found
    return False  # Not found


# Example usage
arr = [29, 25, 3, 49, 9, 37, 21, 43]
key = 37

if bucket_search(arr, key):
    print(f"{key} is found in the array.")
else:
    print(f"{key} is NOT found in the array.")
