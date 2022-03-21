import os
import check_folder
from consts import MAIN_DIRECTORYS
import json_to_txt


def main():
    check_folder.checking()

    parent_directory = list(
        filter((lambda x: os.path.isdir(MAIN_DIRECTORYS + x)),
               os.listdir(MAIN_DIRECTORYS)))

    for parent in parent_directory:
        child_directory = list(
            filter(lambda x: os.path.isdir(MAIN_DIRECTORYS + parent + '/' + x),
                   os.listdir(MAIN_DIRECTORYS + parent + '/')))
        for child in child_directory:
            child_directorys = MAIN_DIRECTORYS + parent + '/' + child + '/'

            file_list = json_to_txt.find_filename(child_directorys)

            json_to_txt.convert(child_directorys, file_list, child)

            json_to_txt.move_jpg(child_directorys, file_list, child)


if __name__ == '__main__':
    main()
