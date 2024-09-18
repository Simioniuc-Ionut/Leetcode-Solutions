class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convertim toate numerele la string pentru a le putea compara
        number = [str(num) for num in nums]
        print("numbert is", number)
        number.sort(key=lambda x: x*10, reverse=True)
        print("sortez is",number)
        largest_num= ''.join(number)
        # Eliminam zerourile de la început , daca exista
        return '0' if largest_num[0] == '0' else largest_num