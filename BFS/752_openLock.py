from collections import deque
class Solution:
    def openLock(self, deadends, target):
        # 要处理deadends；要考虑重复走回头路的情况
        q = deque([])
        q.append("0000")
        count = 0
        visited = []
        visited.append("0000")
        while len(q) != 0:
            length = len(q)
            for i in range(length):
                temp = q.popleft()
                if temp in deadends:
                    continue
                if temp == target:
                    return count
                # 目前位置可拨动后的情况加入到队列中
                for n in range(4):
                    if temp[n] == "0":
                        choice = temp[:n] + "1" + temp[n+1:]
                        if choice not in visited:
                            q.append(choice)
                            visited.append(choice)
                        choice = temp[:n] + "9" + temp[n+1:]
                        if choice not in visited:
                            q.append(choice)
                            visited.append(choice)
                    elif temp[n] == "9":
                        choice = temp[:n] + "0" + temp[n+1:]
                        if choice not in visited:
                            q.append(choice)
                            visited.append(choice)
                        choice = temp[:n] + "8" + temp[n+1:]
                        if choice not in visited:
                            q.append(choice)
                            visited.append(choice)
                    else:
                        choice = temp[:n] + str(int(temp[n])+1) + temp[n+1:]
                        if choice not in visited:
                            q.append(choice)
                            visited.append(choice)
                        choice = temp[:n] + str(int(temp[n])-1) + temp[n+1:]
                        if choice not in visited:
                            q.append(choice)
                            visited.append(choice)
            count += 1
        return -1

