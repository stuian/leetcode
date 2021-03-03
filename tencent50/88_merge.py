class Solution:
    def merge(self, nums1, m, nums2, n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while j < n:
            while (nums1[i] < nums2[j]) and (i < m):
                i += 1
            if i == m:
                for d in range(j,n):
                    nums1[i] = nums2[d]
                    i += 1
                break
            for p in range(m-1,i-1,-1):
                nums1[p+1] = nums1[p]
            nums1[i] = nums2[j]
            m += 1
            i += 1
            j += 1
        return nums1

def main():
    test = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    result = test.merge(nums1,m,nums2,n)
    print(result)

if __name__ == '__main__':
    main()