import os
import pathlib


current_file_path = pathlib.Path(__file__).resolve().parent

if __name__ == '__main__':
    print(current_file_path)
