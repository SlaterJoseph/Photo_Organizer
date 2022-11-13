import os
import time
import shutil


direct = "C:/Users/josep/VS Code Files/Kayla Anniversary/images/dates"
created_files = set()

for file in os.scandir(direct):
    if file.is_file():
        file_name, file_extension = os.path.splitext(file)

        # if file_extension != '.jpg':
        #     continue

        ti_c = os.path.getctime(file)
        c_ti = time.ctime(ti_c)

        chunks = c_ti.split()

        date = "-".join([chunks[i] for i in [1, 2, 4]])

        path = os.path.join(direct, date)
        print(path)
        if path not in created_files:
            print('in creation')
            os.makedirs(path)
            created_files.add(path)

        path_to_pic = os.path.join(direct, file.name)
        path_to_new = os.path.join(path, file.name)
        # print(os.path.exists(path_to_pic))
        shutil.move(path_to_pic, path_to_new)
