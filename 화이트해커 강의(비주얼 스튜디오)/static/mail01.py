import os
import time

DIR_WATCH = "static"

previous_files = set(os.listdir(DIR_WATCH))

while True:
    time.sleep(1)
    print("모티터링중")
    current_files = set(os.listdir(DIR_WATCH))
    new_files = current_files - previous_files
    detected_files = "detected_files.txt"
    for file in new_files:
        if file.endswith('.php') or file.endswith('.html'):
            print(f"새로운 파일 생성: {file}")
            file_path = os.path.join(DIR_WATCH, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith("#") or line.startswith("//"):
                        with open(detected_files, 'a', encoding='utf-8') as f:
                            print(f"주석처리된 라인 {line}")
                            f.write(f"{file_path} : {line}")

    previous_files = current_files 