files = "test.txt"

with open(files, "a", encoding= "utf-8") as f:
    f.write("파일내용추가\n")

print(f"{files}이 수정됨")