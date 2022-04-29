class Solution:
    def reverseString(self, s: List[str]) -> None:
        # 양쪽에서 가운데로 만나기전까지 스와프
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1