# Disk with 20 blocks
disk = [None] * 20

# Allocate file1 from block 2 to 6 (5 blocks)
for i in range(2, 7):
    disk[i] = "file1"

# Allocate file2 from block 8 to 11 (4 blocks)
for i in range(8, 12):
    if disk[i] is None:
        disk[i] = "file2"

# Show disk status
print("Disk blocks:")
for i in range(20):
    print(i, ":", disk[i] if disk[i] else "Free")

# Deallocate file1
for i in range(20):
    if disk[i] == "file1":
        disk[i] = None

# Show disk after deallocation
print("\nAfter deleting file1:")
for i in range(20):
    print(i, ":", disk[i] if disk[i] else "Free")
