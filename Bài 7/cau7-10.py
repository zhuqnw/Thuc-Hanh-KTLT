print("Sinh Viên: Phạm Phúc Hưng")
print("MSSV: 235752021610057")

def find_longest_words(fname):
    with open(fname, 'r', encoding='utf-8') as file:
        words = file.read().split()
        max_length = len(max(words, key=len))
        longest_words = [word for word in words if len(word) == max_length]
    return longest_words

filename = 'abc.txt'
longest_words = find_longest_words(filename)
print(f"The longest words in the file {filename} are: {longest_words}")
