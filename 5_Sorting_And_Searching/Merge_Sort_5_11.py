__author__ = "niketanrane"

class MergeSort:

    def sort(self, data):
        return self._sort(data)

    def _sort(self, data):
        if len(data) < 2:
            return data

        mid = len(data) // 2
        leftArr = data[:mid]
        rightArr = data[mid:]
        leftArr = self._sort(leftArr)
        rightArr = self._sort(rightArr)
        return self._merge(leftArr, rightArr)

    def _merge(self, leftArr, rightArr):
        l = 0
        r = 0
        result = []
        while l < len(leftArr) and r < len(rightArr):
            if leftArr[l] < rightArr[r]:
                result.append(leftArr[l])
                l += 1
            else:
                result.append(rightArr[r])
                r += 1

        while l < len(leftArr):
            result.append(leftArr[l])
            l += 1

        while r < len(rightArr):
            result.append(rightArr[r])
            r += 1

        return result


merge_sort = MergeSort()
data = [5, 1, 7, 2, 6, -3, 5, 7, -1]
print(merge_sort.sort(data))

