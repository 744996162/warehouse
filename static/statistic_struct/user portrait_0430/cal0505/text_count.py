__author__ = 'Administrator'
from collections import Counter
def main():
    file_in = open("result.data")
    file_out_ticket = open("ticket_count.data","a")
    file_out_user = open("user_count.data", "a")

    ticket_num_list = []
    user_num_list = []
    for line in file_in:
        stringArr = line.strip().split("\t")
        uid = stringArr[0]

        ticket_num = int(stringArr[1])
        user_num = int(stringArr[2])

        ticket_num_list.append(ticket_num)
        user_num_list.append(user_num)
    ticket_count = Counter(ticket_num_list)
    user_count = Counter(user_num_list)

    for k, v in ticket_count.iteritems():
        file_out_ticket.write(str(k) + "\t" + str(v) + "\n")

    for k, v in user_count.iteritems():
        file_out_user.write(str(k) + "\t" + str(v) + "\n")
    pass

if __name__ == "__main__":
    main()