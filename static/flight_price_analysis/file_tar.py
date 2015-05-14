__author__ = 'Administrator'
import datetime
import tarfile
import os


def get_today():
    s_today = datetime.datetime.now().strftime("%Y%m%d")
    return s_today


def get_path(folder, s_date=get_today()):
    # get_path("/homezhangc/data/flight_price_analysis/", get_today())
    path_temp = folder + s_date
    return path_temp
    pass


def tar_file(file_path_in, file_path_out):
    tar = tarfile.open(file_path_out, "w|gz")
    tar.add(file_path_in)
    tar.close()
    pass

def main():
    folder1 = "/homezhangc/data/flight_price_analysis/"
    folder2 = "/homezhangc/data/flight_price_analysis_qunar/"
    file_1_in = get_path(folder1)
    file_2_in = get_path(folder2)
    file_1_out = file_1_in + ".tar.gz"
    file_2_out = file_2_in + ".tar.gz"
    print(file_1_in,file_1_out)
    print(file_2_in,file_2_out)
    pass

if __name__ == "__main__":
    file_1_in = "BJS_SHA_2015-02-07.json"
    file_1_out = "test.tar.gz"
    # tar_file(file_1_in, file_1_out)
    main()
