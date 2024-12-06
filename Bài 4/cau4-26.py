# Yêu cầu người dùng nhập các giao dịch
transactions = []
print("Nhập các giao dịch (D 100, W 200), kết thúc nhập bằng cách để trống:")
while True:
    transaction = input()
    if not transaction:
        break
    transactions.append(transaction)

# Tính số tiền thực của tài khoản
balance = 0
for transaction in transactions:
    type, amount = transaction.split()
    amount = int(amount)
    if type == 'D':
        balance += amount
    elif type == 'W':
        balance -= amount

print("Số tiền thực của tài khoản là:", balance)
