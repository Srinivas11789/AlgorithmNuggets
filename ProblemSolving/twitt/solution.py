################# Quesrion 1


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re, sys
from datetime import datetime, tzinfo, timedelta


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


def process_datetime1(dt, tz):
    timer = datetime.strptime(dt, "%d/%b/%Y:%H:%M:%S")  # 27/Jan/2016:01:22:00 +0000
    if tz[1:3] != "00" or tz[3:] != "00":
        if tz[0] == "+":
            timer += timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
        elif tz[0] == "-":
            timer -= timedelta(hours=int(tz[1:3]), minutes=int(tz[3:]))
        else:
            print "WrongTime"
    return timer.isoformat()[:-3]


class timeZone(tzinfo):

    def __init__(self, value):
        if value[0] == '-':
            delta = -1
            value = value[1:]
        elif value[0] == '+':
            delta = +1
            value = value[1:]
        else:
            delta = +1
            value = value
        hour = int(value[0:2], 10)
        minute = int(value[2:3], 10)
        minute = hour * 60 + minute
        minute = delta * minute

        self.__offset = timedelta(minutes=minute)
        self.__name = value

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return timedelta(0)

    def __repr__(self):
        return repr(self.__name)


def process_datetime2(dt, tz):
    calendar = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08",
                "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
    dtobject = datetime(year=int(dt[7:11]), month=int(calendar[dt[3:6]]), day=int(dt[0:2]), hour=int(dt[12:14]),
                        minute=int(dt[15:17]), second=int(dt[18:20]), tzinfo=timeZone(tz))
    utc = timeZone('0000')
    utctime = dtobject.astimezone(utc)
    return utctime.isoformat()[:-9]


def main():
    result = {}
    content = sys.stdin.readlines()
    for data in content:
        uri = re.search("\"[A-Z]+\s(.+?)\s", data)
        uri = uri.group(1)
        if "?" in uri:
            uri = uri.split("?")[0]
        datetime = process_datetime2(re.search("-\s\[(.+?)\s", data).group(1),
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


####################### Question 2

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re,sys
def main():
        content = sys.stdin.readlines()
        for data in content:
            data = data.strip()
            if data[:1] == "E":
                answer = data[:3]+"*****"+data[data.find("@")-1:]
            if data[:1] == "P":
                result = data[2:]
                result = ''.join([i for i in result if i.isdigit()])
                if len(result) > 10:
                    answer = "P:"+"+"+"*"*(len(result)-10)+"-"+"***"+"-"+"***"+"-"+result[len(result)-4:]
                else:
                    answer = "P:"+"***"+"-"+"***"+"-"+result[len(result)-4:]
            print answer
main()


