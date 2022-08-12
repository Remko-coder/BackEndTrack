__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


# Add your code after this line
import os

def clean_cache():
    import shutil
    tmp_folder = os.getcwd()
    #print(f"tmp folder: {tmp_folder}")
    current_folder = os.path.join(tmp_folder, "files")
    target_folder = os.path.join(current_folder,"cache")
    #print(f"huidige folder = {current_folder}")
    folder_exist = os.path.exists(target_folder)
    #print(f"pad bestaat?: {folder_exist}")
    if folder_exist:
        #folder bestaat al
        #print(f"folder bestaat al")
        shutil.rmtree(target_folder)
    os.mkdir(target_folder)
    return

def cache_zip(zip_file_path:str, cache_dir_path:str):
    tmp_folder = os.getcwd()
    zip_file = os.path.join(tmp_folder, zip_file_path)
    cache_path = os.path.join(tmp_folder, cache_dir_path)
    from zipfile import ZipFile
    with ZipFile(zip_file, 'r') as zip:
        zip.printdir()
        zip.extractall(cache_path)
    return

def cached_files():
    tmp_folder = os.getcwd()
    cache_path = os.path.join(tmp_folder, "files/cache")
    file_list = os.listdir(cache_path)
    file_return_list = []
    for i in file_list:
        if os.path.isfile(os.path.join(cache_path,i)):
            file_return_list.append(os.path.join(cache_path, i))
    return(file_return_list)

def find_password(list):
    text = 'password'
    for file_name in list:
        #with open(file_name, 'r') as file:
        #    content = file.read()
        #    if text in content:
        #        print(file_name)
        #        print(content)
        file_read = open(file_name, 'r')
        lines = file_read.readlines()
        for line in lines:
            if text in line:
                #print(line)
                passwordje = line[line.find(text) + len(text) + 2:]
                #print(passwordje.strip())
    return(passwordje.strip())


def main():
    #clean_cache()
    #cache_zip("files/data.zip", "files/cache")
    file_list = cached_files()
    find_password(file_list)


if __name__ == '__main__':
    main()