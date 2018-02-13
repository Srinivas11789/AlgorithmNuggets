# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def process_date(datestring):
    calendar = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
                "Nov": 11, "Dec": 12}
    date = datestring.split("/")
    return date[2] + "-" + str(calendar[date[1]]) + "-" + date[0]


def process_time(timestring):
    time = timestring.split(":")
    return time[0] + ":" + time[1]


def main():
    result = {}
    while True:
        log = raw_input()
        uri = re.search("\"[A-Z]+\s(.+?)\s", log)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        if uri not in result:
            result[uri] = {}
        date = process_date(re.search("-\s\[(.+?):", log).group(1))
        if date not in result[uri]:
            result[uri][date] = {}
        time = process_time(re.search("-\s\[.+?:(.+?)\s", log).group(1))
        if time not in result[uri][date]:
            result[uri][date][time] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", log)
        status_code = status_code.group(1)
        if status_code:
            if "total" not in result[uri][date][time]:
                result[uri][date][time]["total"] = 0
            result[uri][date][time]["total"] += 1
            if "non500" not in result[uri][date][time]:
                result[uri][date][time]["non500"] = 0
            if status_code != 500:
                result[uri][date][time]["non500"] += 1
            if "ratio" not in result[uri][date][time]:
                result[uri][date][time]["ratio"] = "{0:.2f}".format(
                    float(result[uri][date][time]["non500"] / result[uri][date][time]["total"]) * 100)
        print result


main()



### Working - first attempt test 7 and 9 fail


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys


def process_date(datestring):
    calendar = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
                "Nov": 11, "Dec": 12}
    date = datestring.split("/")
    return date[2] + "-" + str(calendar[date[1]]) + "-" + date[0]


def process_time(timestring):
    time = timestring.split(":")
    return time[0] + ":" + time[1]


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        date = process_date(re.search("-\s\[(.+?):", data).group(1))
        time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1))
        key = date + "T" + time + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if status_code:
            if "total" not in result[key]:
                result[key]["total"] = 0
            result[key]["total"] += 1
            if "non500" not in result[key]:
                result[key]["non500"] = 0
            if status_code != "500":
                result[key]["non500"] += 1
            if "ratio" not in result[key]:
                result[key]["ratio"] = 0
            result[key]["ratio"] = "{0:.2f}".format(float(result[key]["non500"]) / result[key]["total"] * 100)
    for key in sorted(result):
        print key + " " + result[key]["ratio"]


main()


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def process_date(datestring):
    calendar = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
                "Nov": 11, "Dec": 12}
    date = datestring.split("/")
    return date[2] + "-" + str(calendar[date[1]]) + "-" + date[0]


def process_time(timestring):
    time = timestring.split(":")
    return time[0] + ":" + time[1]


def main():
    result = {}

    log = raw_input()
    uri = re.search("\"[A-Z]+\s(.+?)\s", log)
    uri = uri.group(1)
    if "?" in uri:
        uri = uri.split("?")[0]
    if uri not in result:
        result[uri] = {}
    date = process_date(re.search("-\s\[(.+?):", log).group(1))
    if date not in result[uri]:
        result[uri][date] = {}
    time = process_time(re.search("-\s\[.+?:(.+?)\s", log).group(1))
    if time not in result[uri][date]:
        result[uri][date][time] = {}
    status_code = re.search("HTTP.+?\s(.+?)\s", log)
    status_code = status_code.group(1)
    if status_code:
        if "total" not in result[uri][date][time]:
            result[uri][date][time]["total"] = 0
        result[uri][date][time]["total"] += 1
        if "non500" not in result[uri][date][time]:
            result[uri][date][time]["non500"] = 0
        if status_code != 500:
            result[uri][date][time]["non500"] += 1
        if "ratio" not in result[uri][date][time]:
            result[uri][date][time]["ratio"] = "{0:.2f}".format(
                float(result[uri][date][time]["non500"] / result[uri][date][time]["total"]) * 100)


main()









#### REsearch

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys, time


def process_datetime(dt):
    from datetime import datetime
    time = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S +0000")  # 27/Jan/2016:01:22:00 +0000
    # time = timestring.split(":")
    return time.strftime("%Y-%m-%dT%H:%M", time)


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        # date = process_date(re.search("-\s\[(.+?):", data).group(1))
        # time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1))
        dt = re.search("-\s\[(.+?)\]\s\"", data).group(1)
        datetime = process_datetime(dt)
        key = datetime + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if status_code:
            if "total" not in result[key]:
                result[key]["total"] = 0
            result[key]["total"] += 1
            if "non500" not in result[key]:
                result[key]["non500"] = 0
            if status_code != "500":
                result[key]["non500"] += 1
            if "ratio" not in result[key]:
                result[key]["ratio"] = 0
            result[key]["ratio"] = "{0:.2f}".format(float(result[key]["non500"]) / float(result[key]["total"]) * 100)
    for key in sorted(result):
        print key + " " + result[key]["ratio"]


main()



########################

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys


def process_date(datestring):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    date = datestring.split("/")
    return date[2] + "-" + calendar[date[1]] + "-" + date[0]


def process_time(timestring, tz):
    time = timestring.split(":")
    if tz[1:3] != "00":
        if tz[0] == "+":
            time[0] = time[0] + tz[1:3]
        else:
            time[0] = time[0] - tz[1:3]
    return time[0] + ":" + time[1]


def process_datetime(dt):


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        date = process_date(re.search("-\s\[(.+?):", data).group(1))
        time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1),
                            re.search("-\s\[.+?:.+?\s(.+?)\]", data).group(1))
        key = date + "T" + time + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if status_code:
            if "total" not in result[key]:
                result[key]["total"] = 0
            result[key]["total"] += 1
            if "non500" not in result[key]:
                result[key]["non500"] = 0
            if status_code != "500":
                result[key]["non500"] += 1
            if "ratio" not in result[key]:
                result[key]["ratio"] = 0
            result[key]["ratio"] = "{0:.2f}".format(float(result[key]["non500"]) / result[key]["total"] * 100)
    for key in sorted(result):
        print key + " " + result[key]["ratio"]


main()

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys, time


def process_date(datestring):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    date = datestring.split("/")
    return date[2] + "-" + calendar[date[1]] + "-" + date[0


def process_time(timestring, tz):
    time1 = timestring.split(":")
    if tz[1:3] != "00":
        if tz[0] == "+":
            time1[0] = time1[0] + tz[1:3]
        else:
            time1[0] = time1[0] - tz[1:3]
    return time1[0] + ":" + time1[1]


def process_datetime(dt):
    from datetime import datetime, timezone
    # time1 = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S %z")  # 27/Jan/2016:01:22:00 +0000
    # utc = datetime.astimezone(UTC).replace(tzinfo=None).isoformat()
    # t = dt.split("+")
    # utc = time.strftime("%Y-%m-%dT%H:%M",time.gmtime(time.mktime(time.strptime(dt, "%d/%b/%Y:%H:%M:%S %z"))))
    time1 = time.mktime(datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S %z").timetuple())
    utc = datetime.utcfromtimestamp(time1)
    return utc.isoformat()[:-3]


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        dt = re.search("-\s\[(.+?)\]\s\"", data).group(1)
        datetime = process_datetime(dt)
        key = datetime + " " + uri
        # date = process_date(re.search("-\s\[(.+?):", data).group(1))
        # time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1), re.search("-\s\[.+?:.+?\s(.+?)\]",data).group(1))
        # key = date + "T" + time + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if status_code:
            if "total" not in result[key]:
                result[key]["total"] = 0
            result[key]["total"] += 1
            if "non500" not in result[key]:
                result[key]["non500"] = 0
            if status_code != "500":
                result[key]["non500"] += 1
            if "ratio" not in result[key]:
                result[key]["ratio"] = 0
            result[key]["ratio"] = "{0:.2f}".format(float(result[key]["non500"]) / result[key]["total"] * 100)
    for key in sorted(result):
        print (key + " " + result[key]["ratio"])


main()


# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys, time
from calendar import timegm
from datetime import datetime


def process_date(datestring):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    date = datestring.split("/")
    return date[2] + "-" + calendar[date[1]] + "-" + date[0]


def process_time(timestring, tz):
    time1 = timestring.split(":")
    if tz[1:3] != "00":
        if tz[0] == "+":
            time1[0] = time1[0] + tz[1:3]
        else:
            time1[0] = time1[0] - tz[1:3]
    return time1[0] + ":" + time1[1]


def process_datetime(dt):
    from datetime import datetime, timezone
    # time1 = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S %z")  # 27/Jan/2016:01:22:00 +0000
    # utc = datetime.astimezone(UTC).replace(tzinfo=None).isoformat()
    # t = dt.split("+")
    # utc = time.strftime("%Y-%m-%dT%H:%M",time.gmtime(time.mktime(time.strptime(dt, "%d/%b/%Y:%H:%M:%S %z"))))
    # time1 = time.mktime(datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S %z").timetuple())
    # utc = datetime.utcfromtimestamp(time1)
    # return utc.isoformat()[:-3]
    timestamp = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S %z").isoformat()
    print (timestamp)
    return datetime.utcfromtimestamp(timestamp).isoformat()[:-3]


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        dt = re.search("-\s\[(.+?)\]\s\"", data).group(1)
        datetime = process_datetime(dt)
        key = datetime + " " + uri
        # date = process_date(re.search("-\s\[(.+?):", data).group(1))
        # time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1), re.search("-\s\[.+?:.+?\s(.+?)\]",data).group(1))
        # key = date + "T" + time + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if status_code:
            if "total" not in result[key]:
                result[key]["total"] = 0
            result[key]["total"] += 1
            if "non500" not in result[key]:
                result[key]["non500"] = 0
            if status_code != "500":
                result[key]["non500"] += 1
            if "ratio" not in result[key]:
                result[key]["ratio"] = 0
            result[key]["ratio"] = "{0:.2f}".format(float(result[key]["non500"]) / result[key]["total"] * 100)
    for key in sorted(result):
        print (key + " " + result[key]["ratio"])


main()



###Python2

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys


def process_date(datestring):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    date = datestring.split("/")
    return date[2] + "-" + calendar[date[1]] + "-" + date[0]


def process_time(timestring, tz):
    time = timestring.split(":")
    if tz[1:3] != "00":
        if tz[0] == "+":
            time[0] = time[0] + tz[1:3]
        else:
            time[0] = time[0] - tz[1:3]
    return time[0] + ":" + time[1]


def process_datetime(dt):


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        date = process_date(re.search("-\s\[(.+?):", data).group(1))
        time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1),
                            re.search("-\s\[.+?:.+?\s(.+?)\]", data).group(1))
        key = date + "T" + time + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if status_code:
            if "total" not in result[key]:
                result[key]["total"] = 0
            result[key]["total"] += 1
            if "non500" not in result[key]:
                result[key]["non500"] = 0
            if status_code != "500":
                result[key]["non500"] += 1
            if "ratio" not in result[key]:
                result[key]["ratio"] = 0
            result[key]["ratio"] = "{0:.2f}".format(float(result[key]["non500"]) / result[key]["total"] * 100)
    for key in sorted(result):
        print key + " " + result[key]["ratio"]


main()


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys, time


def process_date(datestring):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    date = datestring.split("/")
    return date[2] + "-" + calendar[date[1]] + "-" + date[0]


def process_time(timestring, tz):
    from datetime import datetime, timedelta
    t = timestring.split(":")
    utc = datetime.strptime(t[0] + ":" + t[1], "%H:%M", )
    if tz[1:3] != "00":
        if tz[0] == "+":
            t[0] = str(int(t[0]) + int(tz[1:3]))
            utc += timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
        elif tz[0] == "-":
            t[0] = str(int(t[0]) - int(tz[1:3]))
            utc -= timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
        else:
            print time[0]
    return utc.


def process_datetime(dt, tz):
    from datetime import datetime, timedelta
    timer = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S")  # 27/Jan/2016:01:22:00 +0000
    if tz[1:3] != "00" or tz[3:] != "00":
        if tz[0] == "+":
            timer += timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
        else:
            timer -= timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
    return timer.isoformat()[:-3]


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        date = process_date(re.search("-\s\[(.+?):", data).group(1))
        time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1),
                            re.search("-\s\[.+?:.+?\s(.+?)\]", data).group(1))
        key = date + "T" + time + " " + uri
        # dt = re.search("-\s\[(.+?)\]\s\"", data).group(1)
        ##datetime = process_datetime(re.search("-\s\[(.+?)\s", data).group(1), re.search("-\s\[.+?:.+?\s(.+?)\]",data).group(1))
        ##key = datetime + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if "total" not in result[key]:
            result[key]["total"] = 0
        result[key]["total"] += 1
        if "non500" not in result[key]:
            result[key]["non500"] = 0
        if status_code[0] != "5":
            result[key]["non500"] += 1
        if "ratio" not in result[key]:
            result[key]["ratio"] = 0
        result[key]["ratio"] = "{0:.2f}".format((float(result[key]["non500"]) / float(result[key]["total"])) * 100)
    for key in sorted(result):
        print key + " " + result[key]["ratio"]


main()


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys


def process_date(datestring):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    date = datestring.split("/")
    return date[2] + "-" + calendar[date[1]] + "-" + date[0]


def process_time(timestring, tz):
    time = timestring.split(":")
    if tz[1:3] != "00":
        if tz[0] == "+":
            time[0] = time[0] + tz[1:3]
        else:
            time[0] = time[0] - tz[1:3]
    return time[0] + ":" + time[1]


def process_datetime(dt, tz):
    from datetime import datetime, timedelta
    timer = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S")  # 27/Jan/2016:01:22:00 +0000
    if tz[1:3] != "00" or tz[3:] != "00":
        if tz[0] == "+":
            timer += timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
        else:
            timer -= timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
    return timer.isoformat()[:-3]


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        # date = process_date(re.search("-\s\[(.+?):", data).group(1))
        # time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1), re.search("-\s\[.+?:.+?\s(.+?)\]",data).group(1))
        # key = date + "T" + time + " " + uri
        # dt = re.search("-\s\[(.+?)\]\s\"", data).group(1)
        datetime = process_datetime(re.search("-\s\[(.+?)\s", data).group(1),
                                    re.search("-\s\[.+?:.+?\s(.+?)\]", data).group(1))
        key = datetime + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if "total" not in result[key]:
            result[key]["total"] = 0
        result[key]["total"] += 1
        if "non500" not in result[key]:
            result[key]["non500"] = 0
        if status_code[0] != "5":
            result[key]["non500"] += 1
        if "ratio" not in result[key]:
            result[key]["ratio"] = 0
        result[key]["ratio"] = "{0:.2f}".format((float(result[key]["non500"]) / float(result[key]["total"])) * 100)
    for key in sorted(result):
        print key + " " + result[key]["ratio"]


main()


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
from datetime import datetime, tzinfo, timedelta
def process_date(datestring):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10","Nov": "11", "Dec": "12"}
    date = datestring.split("/")
    return date[2] + "-" + calendar[date[1]] + "-" + date[0]


def process_time(timestring, tz):
    time = timestring.split(":")
    if tz[1:3] != "00":
        if tz[0] == "+":
            time[0] = time[0]+tz[1:3]
        else:
            time[0] = time[0]-tz[1:3]
    return time[0] + ":" + time[1]


class FixedOffset(tzinfo):
    """Fixed offset in minutes east from UTC."""

    def __init__(self, string):
        #import pudb ; pudb.set_trace()
        if string[0] == '-':
            direction = -1
            string = string[1:]
        elif string[0] == '+':
            direction = +1
            string = string[1:]
        else:
            direction = +1
            string = string

        hr_offset = int(string[0:2], 10)
        min_offset = int(string[2:3], 10)
        min_offset = hr_offset * 60 + min_offset
        min_offset = direction * min_offset

        self.__offset = timedelta(minutes = min_offset)

        self.__name = string

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return timedelta(0)

    def __repr__(self):
        return repr(self.__name)


def process_datetime(dt, tz):
    from datetime import datetime,timedelta
    timer = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S") #27/Jan/2016:01:22:00 +0000
    """
    if tz[1:3] != "00" or tz[3:] != "00":
        if tz[0] == "+":
            timer += timedelta(hours=int(tz[1:3]),minutes=int(tz[3:]))
            print "hi"
        elif tz[0] == "-":
            timer -= timedelta(hours=int(tz[1:3]),minutes=int(tz[3:]))
            print "hi2"
        else:
            print "WrongTime"
    return timer.isoformat()[:-3]"""
    #obj = datetime(year=int(timer[7:11]), month=month_map[s[3:6]], day=int(s[0:2]),hour=int(s[12:14]),minute=int(s[15:17]), second=int(s[18:20]),tzinfo=tz)
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10","Nov": "11", "Dec": "12"}
    obj = datetime(year=int(dt[7:11]), month=int(calendar[dt[3:6]]), day=int(dt[0:2]),hour=int(dt[12:14]),minute=int(dt[15:17]), second=int(dt[18:20]),tzinfo=FixedOffset(tz))
    utc = FixedOffset('0000')
    utc_obj = obj.astimezone(utc)
    return utc_obj.isoformat()[:-9]

def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        #date = process_date(re.search("-\s\[(.+?):", data).group(1))
        #time = process_time(re.search("-\s\[.+?:(.+?)\s", data).group(1), re.search("-\s\[.+?:.+?\s(.+?)\]",data).group(1))
        #key = date + "T" + time + " " + uri
        #dt = re.search("-\s\[(.+?)\]\s\"", data).group(1)
        datetime = process_datetime(re.search("-\s\[(.+?)\s", data).group(1), re.search("-\s\[.+?:.+?\s(.+?)\]",data).group(1))
        key = datetime + " " + uri
        if key not in result:
            result[key] = {}
        status_code = re.search("HTTP.+?\s(.+?)\s", data)
        status_code = status_code.group(1)
        if "total" not in result[key]:
                result[key]["total"] = 0
        result[key]["total"] += 1
        if "non500" not in result[key]:
                result[key]["non500"] = 0
        if status_code[0] != "5":
                result[key]["non500"] += 1
        if "ratio" not in result[key]:
                result[key]["ratio"] = 0
        result[key]["ratio"] = "{0:.2f}".format((float(result[key]["non500"]) / float(result[key]["total"])) * 100)
    for key in sorted(result):
        print key + " " + result[key]["ratio"]


main()




