class Solution:
    def reformatDate(self, date: str) -> str:
        
        # Logic 1: Hacky way to accomplish - 100 pass - 93.56% faster
        
        # Holder for months to count 1->12
        months = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        #months = {"Jan": "1", "Feb":"2", "Mar":"3", "Apr":"4", "May":"5", "Jun":"6", "Jul":"7", "Aug":"8", "Sep":"9", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        dateList = date.split(" ")
        
        # Calculate day
        day = ""
        i = 0
        while dateList[0][i].isdigit():
            day += dateList[0][i]
            i += 1
        
        # Calculate month --> Use a dictionary for being faster
        month = str(months.index(dateList[1]))
        #month = months[dateList[1]]
        
        # Year
        year = dateList[2]
        
        # Return with formatting 2 digits
        return year + "-" + month.zfill(2) + "-" + day.zfill(2)
        
