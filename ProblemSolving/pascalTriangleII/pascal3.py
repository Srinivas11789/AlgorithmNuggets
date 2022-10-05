class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        prev_row = []
        cur_row = [1]
        for i in range(1, rowIndex+1):
            cur_row = [1]*(i+1)
            if len(cur_row) > 2:
                for i in range(1, len(cur_row)-1):
                    cur_row[i] = prev_row[i-1] + prev_row[i]
            prev_row = cur_row

        return cur_row
