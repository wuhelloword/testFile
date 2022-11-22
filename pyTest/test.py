from collections.abc import Iterable
class Solution:
    """
    无法吃午餐的学生数量
    """
    def countStudents(self, students, sandwiches):
        if len(students) == 0:
            return 0
        else:
#             while循环
            flag = 1
            while flag:
                flag = 0
                for index, student in enumerate(students):
                    if student == sandwiches[0]:
                        sandwiches.pop(0)
                        students.pop(index)
                        flag = 1
            return len(sandwiches)

# 尾递归优化的斐波那契数列
def fibonacii(n):
    # 优化前
    if (n<=2):
        return 1
    return fibonacii(n-1) + fibonacii(n-2)
# 递归函数改写成尾递归，确保最后一步只调用自身。
# 把所有用到的内部变量改写成函数的参数，
# def fibonacii2(n):
#     if n<=2:
#         return 1


def kthGrammar(n: int, k: int) -> int:
    """
    第k个语法符号
    :param n:
    :param k:
    :return:
    """
    result = 0
    if n == 1:
        return 0
    for i in range(n):
        tem = ""
        for item in str(result):
            if item == '0':
                tem += '01'
            if item == '1':
                tem += '10'
        result = tem
    return int(result[k-1])



class StockSpanner:
    """股票价格跨度"""
    def __init__(self):
        self.result = []

    def next(self, price):
        self.result.insert(0, price)
        count = 0
        for i in self.result:
            if i <= price:
                count = count+1
            else:
                break
        return count



def nextGreaterElement(nums1, nums2):
    """
    下一个更大元素
    :param nums1:
    :param nums2:
    :return:
    """
    results = []
    for i in nums1:
        index = nums2.index(i)
        result = -1
        for j in range(index, len(nums2)):
            if nums2[j] > i:
                result = nums2[j]
                break
        results.append(result)
    return results

def nextGreaterElement2(nums1, nums2):
    """
    下一个更大元素
    :param nums1:
    :param nums2:
    :return:
    """
    res = {}
    stack = []  # 栈
    for num in reversed(nums2):
        while stack and num >= stack[-1]:       # 栈顶元素
            stack.pop()
        res[num] = stack[-1] if stack else -1
        stack.append(num)
    return [res[num] for num in nums1]


def partitionDisjoint(nums:list):
    """
    分割数组
    :param nums:
    :return:
    """
    nums.reverse()
    middle = min(nums)
    middle = nums.index(middle)
    right = nums[0:middle]
    left = nums[middle:]
    _max = max(left)
    print(left, right)
    for i in right[::-1]:
        if i <= _max:
            left
            _max = max(left)


def testItrable():
    """测试迭代器"""
    print(isinstance('a',Iterable))
    print(isinstance('a', str))




if __name__ == '__main__':
    # print(kthGrammar(2, 2))
    # print(nextGreaterElement2([4,1,2],[1,3,4,2]))
    # partitionDisjoint([1,1,1,0,6,12])
    testItrable()
