
blocks = [100, 500, 200, 300, 600]

processes = [212, 417, 112, 426]

allocation = [-1] * len(processes) 

for i in range(len(processes)):
    for j in range(len(blocks)):
        if blocks[j] >= processes[i]:
            allocation[i] = j
            blocks[j] -= processes[i]  
            break
        
# Print allocation result
for i in range(len(processes)):
    print(f"Process {i+1} (Size {processes[i]}) -> ", end="")
    if allocation[i] != -1:
        print(f"Block {allocation[i]+1}")
    else:
        print("Not Allocated")