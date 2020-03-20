import heapq

seq = [1, 3, 7, 5, 4, 2, 10]
heap_q = []
for i in range (len(seq)):
	heapq.heappush(heap_q, (seq[i], i))

while True:
	cur = heapq.heappop(heap_q)
	print (cur)
	if len(heap_q) == 0:
		break
