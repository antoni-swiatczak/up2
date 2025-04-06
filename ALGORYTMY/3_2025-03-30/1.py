arrs = [
    31, 36, 217, 219, 517, 1039, 1097, 1112, 1190, 1305, 1374, 1378, 1381, 1470, 1484, 1712, 1738, 1798, 1832, 1891, 1944, 1960, 1987, 1995, 2186, 2395, 2406, 2508, 2648, 2766, 2813, 2853, 2920, 3010, 3273, 3314, 3378, 3406, 3647, 3651, 3675, 3681, 3822, 3895, 3948, 4305, 4492, 4603, 4812, 4819, 4837, 4911, 4920, 5128, 5491, 5687, 5774, 5835, 5848, 6061, 6069, 6092, 6113, 6182, 6203, 6239, 6351, 6478, 6519, 6571, 6608, 6761, 6769, 6840, 6853, 6965, 7123, 7269, 7353, 7372, 7619, 7634, 7760, 8254, 8543, 8700, 8735, 8765, 8897, 8958, 9000, 9066, 9123, 9171, 9203, 9432, 9490, 9515, 9547, 9921
]

arr = [
    9377, 2109, 7304, 525, 8179, 5939, 4918, 3044, 1405, 1743, 4534, 4522, 750, 7108, 7563, 7373, 9507, 615, 8280, 2298, 4639, 456, 9009, 6994, 1282, 3335, 7276, 861, 7530, 8569, 5835, 3482, 1418, 1350, 8977, 4125, 2749, 6339, 5484, 8476, 1061, 8154, 8126, 95, 6150, 5234, 3056, 863, 547, 9536, 6550, 4861, 7905, 716, 3810, 7009, 6823, 2581, 4794, 5295, 8385, 1027, 9511, 1236, 5308, 9246, 8466, 3717, 9428, 3683, 5875, 9634, 7985, 7462, 5244, 2498, 9816, 4255, 9963, 8505, 9489, 5987, 7910, 5182, 9588, 8663, 3924, 458, 3278, 5573, 9720, 8864, 8490, 5181, 801, 3247, 6644, 4601, 3393, 7571
]

#a -> C: O(1) / P: O(1)
def sorted(arr):
    counter = 0
    min = arr[0]
    counter += 1
    max = arr[len(arr) - 1]
    counter += 1
    print("\n#a:")
    print(f"m: {min}")
    print(f"M: {max}")
    print(f"c: {counter}")

sorted(arrs)

#b -> C: O(n) / P: O(n)
def unsorted(arr):
    counter = 0
    comparations = 0
    min = arr[0]
    counter += 1
    max = arr[0]
    counter += 1
    for i in range(1, len(arr)):
        if (arr[i] < min):
            min = arr[i]
            counter += 1
            comparations += 1
        elif (arr[i] > max):
            max = arr[i]
            counter += 1
            comparations += 2
        else:
            comparations += 2
    print("\n#b:")
    print(f"m: {min}")
    print(f"M: {max}")
    print(f"cr: {counter}")
    print(f"cs: {comparations}")

unsorted(arr)

#c -> C: O(n) / P: O(1)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def find_min(self):
        counter = 0
        current_node = self.root
        counter += 1
        while current_node.left:
            current_node = current_node.left
            counter += 1
        return current_node.value, counter

    def find_max(self):
        counter = 0
        current_node = self.root
        counter += 1
        while current_node.right:
            current_node = current_node.right
            counter += 1
        return current_node.value, counter

bst = BST()

for num in arr:
    bst.insert(num)

min, crm = bst.find_min()
max, crM = bst.find_max()
print("\n#c:")
print(f"m: {min}")
print(f"crm: {crm}")
print(f"M: {max}")
print(f"crM: {crM}")