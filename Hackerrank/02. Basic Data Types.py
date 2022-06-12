# 01. List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([ [ i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if ( (i + j + k) != n )])



# 02. Find the Runner-Up Score! (Find Second Maximum Number in a List)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    first = max(arr)
    
    print(max(list(filter(lambda a: a != first, arr))))



# 03. Nested Lists
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        students.append([name, score])
    
    lowest = min([el[1] for el in students])
    second_low = min(list(filter(lambda a: a > lowest, [el[1] for el in students])))
    
    out = [el[0] for el in students if (el[1] == second_low)]
    out.sort()
    
    print("\n".join(out))



# 04. Finding the percentage
def get_avg(marks, student):
    return (sum(marks[student])/len(marks[student]))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("{:.2f}".format(get_avg(student_marks, query_name)))



# 05. Lists
if __name__ == '__main__':
    N = int(input())
    outlist = []
    for _ in range(N):
        args = input().strip().split(' ')
        cmd = args[0]
        if cmd == 'insert':
            outlist.insert(int(args[1]), int(args[2]))
        elif cmd == 'remove':
            outlist.remove(int(args[1]))
        elif cmd == 'append':
            outlist.append(int(args[1]))
        elif cmd == 'print':
            print(outlist)
        elif cmd == 'sort':
            outlist.sort()
        elif cmd == 'pop':
            outlist.pop()
        elif cmd == 'reverse':
            outlist.reverse()



# 06. Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    print(hash(tuple(integer_list)))


