'''
용량별 정리 후 정렬하여 txt로 출력
'''
import os

def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            try:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
            except:
                continue
    return total_size

def list_folders_by_size(main_folder):
    folder_sizes = []

    for folder_name in os.listdir(main_folder):
        folder_path = os.path.join(main_folder, folder_name)
        if os.path.isdir(folder_path):
            size = get_folder_size(folder_path)
            folder_sizes.append((folder_name, size))

    # 크기가 큰 순서대로 정렬
    folder_sizes.sort(key=lambda x: x[1], reverse=True)

    return folder_sizes

def save_to_txt(folder_sizes, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for folder_name, size in folder_sizes:
            file.write(f"{folder_name}: {size} bytes\n")

if __name__ == "__main__":
    main_folder = "."  # 현재 스크립트 파일이 위치한 디렉토리
    output_file = "folder_sizes.txt"

    folder_sizes = list_folders_by_size(main_folder)
    save_to_txt(folder_sizes, output_file)

    print(f"Folder sizes saved to {output_file}")