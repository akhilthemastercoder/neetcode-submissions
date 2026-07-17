class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       newArr = []
       for i in range(len(arr)):
            current_max = -1
            for j in range(i + 1, len(arr)):
                if current_max < arr[j]:
                    current_max = arr[j]
            newArr.append(current_max)
       return newArr