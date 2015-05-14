__author__ = 'Administrator'
import os

class File(object):

    def __init__(self,file_path):
        self._file_path = file_path

    def __str__(self):
        return self._file_path

    @staticmethod
    def line_count(file_path):
        num_lines = sum(1 for line in open(str(file_path)))
        return num_lines

    @staticmethod
    def get_file_name(file_path):
        return os.path.basename(file_path)

    @staticmethod
    def get_file_path(file_path):
        return file_path

    #statis line number
    def get_count(self):
        count = File.line_count(self._file_path)
        return count


class Folder(object):

    def __init__(self, folder_path):
        self.folder_path = folder_path




