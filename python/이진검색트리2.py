import sys
sys.setrecursionlimit(10**9)

def get_input_numbers():
    numbers = []
    while True:                            
        try:
            numbers.append(int(sys.stdin.readline())) # 리스트에 더하기
        except:
            break#멈춘다. 예외 발생하면
    return numbers#입력받은 거 리스트에 담아서 리턴해

def print_postorder_traversal(start, end, numbers):
    if start > end:# 
        return
    
    right_node_index = end + 1

    for i in range(start + 1, end + 1):
        if numbers[start] < numbers[i]:
            right_node_index = i
            break

    print_postorder_traversal(start + 1, right_node_index - 1, numbers)
    print_postorder_traversal(right_node_index, end, numbers)
    print(numbers[start])

if __name__ == "__main__":
    input_numbers = get_input_numbers()
    print_postorder_traversal(0, len(input_numbers) - 1, input_numbers)
