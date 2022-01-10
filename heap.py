heap_size = 0


def heapify(array, i):
    global heap_size

    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left <= heap_size and array[left] < array[smallest]:
        smallest = left

    if right <= heap_size and array[right] < array[smallest]:
        smallest = right

    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        heapify(array, smallest)


def build_min_heap(array):
    global heap_size

    heap_size = len(array) - 1

    for i in range(heap_size // 2, 0, -1):
        heapify(array, i)


def heap_dequeue(array):
    global heap_size

    if heap_size < 1:
        return array.pop()

    smallest, array[0] = array[0], array.pop()
    heap_size -= 1

    heapify(array, 0)

    return smallest


def heap_enqueue(array, key):
    array.append(key)
    build_min_heap(array)
