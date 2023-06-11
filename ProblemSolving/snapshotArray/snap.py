# Logic 1: naive method of utilizing memory to store copies of arrays
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0]*length
        self.snaps = []

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        return

    def snap(self) -> int:
        self.snaps.append(self.array[:])
        return len(self.snaps)-1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id >= len(self.snaps):
            return 0
        return self.snaps[snap_id][index]
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
"""

# Logic 2: save snapshot of changes everytime - time limit exceeded
"""
class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0]*length
        self.snaps = []
        self.changes = {}

    def set(self, index: int, val: int) -> None:
        self.changes[index] = val
        self.array[index] = val
        return

    def snap(self) -> int:
        # save only the difference
        # compute difference
        self.snaps.append(self.changes.copy())
        self.changes = {}
        return len(self.snaps) - 1

    def get(self, index: int, snap_id: int) -> int:
        if snap_id >= len(self.snaps):
            return 0
        initial = 0
        for i in range(snap_id+1):
            if index not in self.snaps[i]:
                continue
            initial = self.snaps[i][index]
        return initial
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
"""

# Logic 3: for each element at index track the changes through the snaps
class SnapshotArray:

    def __init__(self, length: int):
        self.changes = {}
        self.snaps_of_elements = {}
        self.snaps = 0

    def set(self, index: int, val: int) -> None:
        self.changes[index] = val
        return

    def snap(self) -> int:
        for ind, val in self.changes.items():
            if ind not in self.snaps_of_elements:
                self.snaps_of_elements[ind] = []
            self.snaps_of_elements[ind].append([self.snaps, val])
        self.changes = {}
        self.snaps += 1
        return self.snaps - 1

    def get(self, index: int, snap_id: int) -> int:
        if index not in self.snaps_of_elements:
            return 0
        last_val = 0
        #print(self.snaps_of_elements, snap_id)
        for snaps in self.snaps_of_elements[index]:
            snap, val = snaps
            if snap > snap_id:
                return last_val
            elif snap == snap_id:
                return val
            last_val = val 
        return last_val
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
