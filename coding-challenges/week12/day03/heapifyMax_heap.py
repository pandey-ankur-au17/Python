heap = [1,2,3,4,5,6,7,8,9]

def heapify(i):
    global heap
    
    left_idx = 2*i+1
    right_idx = 2*i+2
    
    
    if left_idx >len(heap)-1 and right_idx > len(heap)-1: ## leaf node
        return
    max_idx = i
    if left_idx < len(heap) and heap[i] < heap[left_idx]:
        max_idx = left_idx
    
    if right_idx < len(heap) and heap[max_idx] < heap[right_idx]:
        max_idx = right_idx
        
    
    if max_idx != i:
        heap[max_idx],heap[i] = heap[i],heap[max_idx]
        heapify(max_idx)

    


if __name__=="__main__":
    n = len(heap)
    
    for i in range(n-1, -1, -1):
        heapify(i)
        
    print(heap)
