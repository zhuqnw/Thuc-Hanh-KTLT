print("Sinh Vien : Pham Phuc Hung")
print("MSSV:235752021610057")
class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

def main():
    atm = ATM(1000)  # Khởi tạo máy ATM với số dư ban đầu là 1000

    while True:
        print("\nChào mừng đến với máy ATM!")
        print("1. Kiểm tra số dư")
        print("2. Gửi tiền")
        print("3. Rút tiền")
        print("4. Thoát")

        choice = input("Vui lòng chọn một tùy chọn: ")

        if choice == '1':
            print(f"Số dư hiện tại của bạn là: {atm.check_balance()} VND")
        elif choice == '2':
            amount = float(input("Nhập số tiền bạn muốn gửi: "))
            if atm.deposit(amount):
                print(f"Bạn đã gửi thành công {amount} VND")
            else:
                print("Số tiền không hợp lệ. Vui lòng thử lại.")
        elif choice == '3':
            amount = float(input("Nhập số tiền bạn muốn rút: "))
            if atm.withdraw(amount):
                print(f"Bạn đã rút thành công {amount} VND")
            else:
                print("Số tiền không hợp lệ hoặc không đủ. Vui lòng thử lại.")
        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng máy ATM. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")

if __name__ == "__main__":
    main()
