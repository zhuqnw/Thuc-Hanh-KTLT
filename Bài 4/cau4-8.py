print("Sinh viên : Phạm Phúc Hưng")
print("MSSV :235752021610057")
# Nhập một dãy các từ từ bàn phím
words = input("dãy các từ: ").split()

# Tìm độ dài của từ dài nhất
max_length = max(len(word) for word in words)

# Lấy tất cả các từ có độ dài bằng với từ dài nhất
longest_words = [word for word in words if len(word) == max_length]

# In ra từ dài nhất và tất cả các từ có cùng độ dài
print("từ dài nhất trong dãy:")
for word in longest_words:
    print(word)
