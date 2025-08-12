"""
冒泡排序
li01 = [10, 1, 7, 4, 6, 2]

算法原理：
- 相邻两组数两两排序，每次得到一个较大的值
- 排序轮数为数组长度减1
"""
li01 = [10, 1, 7, 4, 6, 2]
def bubbling(li_a, is_bubbling = True):
    def fn_sort(li):
        for idx, item in enumerate(li):
            if idx <= len(li) - 2:
                if is_bubbling:
                    if li[idx + 1] - li[idx] < 0:
                        li01[idx], li01[idx + 1] = li[idx + 1], li[idx]
                else:
                    if li[idx + 1] - li[idx] > 0:
                        li01[idx], li01[idx + 1] = li[idx + 1], li[idx]

    for i in range(len(li_a) - 1):
        fn_sort(li_a)

bubbling(li01)

print(li01)
