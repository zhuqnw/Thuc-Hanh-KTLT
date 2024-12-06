print("Sinh Vien : Pham Phuc Hung")
print("MSSV: 235752021610057")
import datetime as dt

# Định dạng thời gian
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển đổi chuỗi thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
print('Day ' + str(t1.day))
print('Month ' + str(t1.month))
print('Minute ' + str(t1.minute))
print('Second ' + str(t1.second))

# Định nghĩa ngày và giờ hiện tại
t2 = dt.datetime.now()
diff = t2 - t1
print('How many days difference? ' + str(diff.days))
