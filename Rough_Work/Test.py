import datetime
def merge_date_ranges(data):
    result = []
    t_old = data[0]
    for t in data[1:]:
        if t_old[1] >= t[0]:  #I assume that the data is sorted already
            t_old = ((min(t_old[0], t[0]), max(t_old[1], t[1])))
        else:
            result.append(t_old)
            t_old = t
    else:
        result.append(t_old)
    return result
data = [
["15012021_T_13:50:59", "28012021_T_23:59:59"],
["26022021_T_23:59:59", "03032021_T_20:31:10"],
["18012021_T_01:50:32", "18012021_T_23:59:59"],
["28022021_T_23:59:59", "06032021_T_12:19:50"],
["28012021_T_21:51:12", "04022021_T_23:50:22"],
["18042021_T_14:19:51", "28042021_T_11:02:31"]
]

data = [(datetime.datetime(2016, 1, 10, 13, 0), datetime.datetime(2016, 1, 10, 16, 0)), (datetime.datetime(2016, 1, 10, 14, 0), datetime.datetime(2016, 1, 10, 14, 0)), (datetime.datetime(2016, 1, 10, 22, 0), datetime.datetime(2016, 1, 10, 22, 0)), (datetime.datetime(2016, 1, 10, 23, 0), datetime.datetime(2016, 1, 11, 0, 30)), (datetime.datetime(2016, 1, 11, 2, 30), datetime.datetime(2016, 1, 11, 3, 30)), (datetime.datetime(2016, 1, 11, 13, 0), datetime.datetime(2016, 1, 11, 16, 0)), (datetime.datetime(2016, 1, 11, 14, 0), datetime.datetime(2016, 1, 11, 14, 0)), (datetime.datetime(2016, 1, 11, 20, 30), datetime.datetime(2016, 1, 11, 21, 30)), (datetime.datetime(2016, 1, 11, 22, 0), datetime.datetime(2016, 1, 11, 22, 0)), (datetime.datetime(2016, 1, 12, 2, 30), datetime.datetime(2016, 1, 12, 3, 30)), (datetime.datetime(2016, 1, 12, 13, 0), datetime.datetime(2016, 1, 12, 16, 0)), (datetime.datetime(2016, 1, 12, 14, 0), datetime.datetime(2016, 1, 12, 14, 0)), (datetime.datetime(2016, 1, 12, 19, 30), datetime.datetime(2016, 1, 12, 20, 30)), (datetime.datetime(2016, 1, 12, 22, 0), datetime.datetime(2016, 1, 12, 22, 0)), (datetime.datetime(2016, 1, 13, 2, 30), datetime.datetime(2016, 1, 13, 3, 30)), (datetime.datetime(2016, 1, 13, 13, 0), datetime.datetime(2016, 1, 13, 16, 0)), (datetime.datetime(2016, 1, 13, 14, 0), datetime.datetime(2016, 1, 13, 14, 0)), (datetime.datetime(2016, 1, 13, 20, 0), datetime.datetime(2016, 1, 13, 21, 0)), (datetime.datetime(2016, 1, 13, 21, 30), datetime.datetime(2016, 1, 13, 22, 0)), (datetime.datetime(2016, 1, 13, 22, 0), datetime.datetime(2016, 1, 13, 22, 0)), (datetime.datetime(2016, 1, 14, 2, 30), datetime.datetime(2016, 1, 14, 3, 30)), (datetime.datetime(2016, 1, 14, 13, 0), datetime.datetime(2016, 1, 14, 16, 0)), (datetime.datetime(2016, 1, 14, 14, 0), datetime.datetime(2016, 1, 14, 14, 0)), (datetime.datetime(2016, 1, 14, 22, 0), datetime.datetime(2016, 1, 14, 22, 0)), (datetime.datetime(2016, 1, 14, 22, 0), datetime.datetime(2016, 1, 14, 23, 0)), (datetime.datetime(2016, 1, 15, 2, 30), datetime.datetime(2016, 1, 15, 3, 30)), (datetime.datetime(2016, 1, 15, 13, 0), datetime.datetime(2016, 1, 15, 16, 0)), (datetime.datetime(2016, 1, 15, 14, 0), datetime.datetime(2016, 1, 15, 14, 0)), (datetime.datetime(2016, 1, 15, 20, 30), datetime.datetime(2016, 1, 15, 22, 0)), (datetime.datetime(2016, 1, 15, 22, 0), datetime.datetime(2016, 1, 15, 22, 0)), (datetime.datetime(2016, 1, 16, 2, 30), datetime.datetime(2016, 1, 16, 3, 30)), (datetime.datetime(2016, 1, 16, 13, 0), datetime.datetime(2016, 1, 16, 16, 0)), (datetime.datetime(2016, 1, 17, 2, 30), datetime.datetime(2016, 1, 17, 3, 30))]
print(merge_date_ranges(data))