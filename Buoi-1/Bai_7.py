print("Nhập các dòng văn bản(Nhập '0' để kết thúc):")
lines = []
while True:
    line = input()
    if line() == '0':
        break
    lines.append(line)
print("\n Các dòng đã nhập sau khi in hoa thì nó thành: ")
for line in lines:
    print(line.upper())