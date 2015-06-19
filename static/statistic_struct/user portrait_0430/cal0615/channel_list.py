__author__ = 'Administrator'

def get_channel_list():
    file_path = "channel.dat"
    file_in = open(file_path)
    channel_dict = dict()
    channel_list = []
    for line in file_in:
        stringArr = line.strip().split("\t")
        channel_dict[stringArr[0]] = int(stringArr[1])
    count = 0
    for key, value in sorted(channel_dict.items(), key=lambda d: d[1], reverse=True):
        count += int()
        if value > 10000:
            channel_list.append(key)
            # print(key, value)

    return channel_list



