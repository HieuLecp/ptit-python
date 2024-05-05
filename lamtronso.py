def round_number(N):
    if N <= 10:
        return N
    
    order_of_magnitude = 10
    while N > order_of_magnitude:
        order_of_magnitude *= 10

    if N <= 10 * order_of_magnitude / 2:
        return (N // (order_of_magnitude // 10)) * (order_of_magnitude // 10)
    elif N <= 100 * order_of_magnitude / 2:
        return (N // (order_of_magnitude // 100)) * (order_of_magnitude // 100)
    elif N <= 1000 * order_of_magnitude / 2:
        return (N // (order_of_magnitude // 1000)) * (order_of_magnitude // 1000)
    # Các quy tắc tiếp theo có thể thêm vào tại đây nếu cần
    
    return N
n=int(input());
print(round_number(n));
