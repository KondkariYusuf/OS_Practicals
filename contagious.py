disk = [None] * 20  
files = [("file1", 2, 5), ("file2", 8, 4), ("file3", 17, 4)]

for name, start, length in files:
    if start + length <= len(disk) and all(disk[i] is None for i in range(start, start + length)):
        for i in range(start, start + length):
            disk[i] = name
        print(f"{name} allocated from {start} to {start + length - 1}")
    else:
        print(f"{name} not allocated")

print("\nDisk status:")
for i in range(len(disk)):
    print(f"Block {i}: {disk[i] if disk[i] else 'Free'}")

