import os, sys

class FileUtils:

    ###
    # @params string path_to_dir, string extensions
    # ex get_files_by_dir('/home/user/somepath', '.txt')
    ###
    @staticmethod
    def get_files_by_dir(path_to_dir, ext):
        data = []
        for root, dirs, files in os.walk(path):
            for item in files:
                ### get all files irrespective of file extension
                if ext is None:
                    data.append({'path': r, 'filename':item})
                #only get files that match a certain extension
                if ext is not None and ext in item:
                    data.append({'path': r, 'filename':item})
        return data
