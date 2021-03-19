from Expense import model


class app():
    choice = 0
    l = []
    e = []

    def __init__(self):
        while True:
            self.printOptions()
            if app.choice == 1:
                self.addCategory()
            elif app.choice == 2:
                self.categoryListing()
            elif app.choice == 3:
                self.expenseEntry()
            elif app.choice == 4:
                self.expenseListing()
            elif app.choice == 5:
                self.reportCatWise()
            elif app.choice == 6:
                self.reportMonWise()
            elif app.choice == 7:
                self.reportMonRange()
            elif app.choice == 8:
                break

    def printOptions(self):

        print("-------------------")
        print("1. Add Category")
        print("2. Category Listing")
        print("3. Expense Entry")
        print("4. Expense Listing")
        print("5. Report: Cat-Wise")
        print("6. Report: Month-Wise")
        print("7. Report: MonthRange")
        print("8. Exit")
        app.choice = int(input("Enter your Choice: "))

    def addCategory(self):
        print("----------------------")

        cateid = int(input("Enter Category ID: "))
        catename = input("Enter Category Name: ")

        cn = []
        ci = []
        for i in app.l:
            ci.append(i.getCatid())
            cn.append(i.getCatName())

        if cateid in ci:
            print("Id already exist")
        else:
            if catename in cn:
                print("Category Name already exist")
            else:
                c = model.Category()
                c.setCatid(cateid)
                c.setCatName(catename)
                app.l.append(c)
                print("Category Added")
                print("----------------------")

    def categoryListing(self):
        count = 1
        print("----------------------")
        for i in app.l:
            print(count, ".", i.getCatName())
            count += 1
        print("----------------------")

    def expenseEntry(self):
        print("-------------------")
        self.categoryListing()
        selNum = int(input("select category num to add expenses: "))
        catObj = app.l[selNum - 1]

        id = catObj.getCatid()
        amount = float(input("Enter Amount: "))
        remark = input("Enter Remark: ")
        date = input("Enter Date (dd/mm/yyyy)")

        e = model.Expense()
        e.setAmount(amount)
        e.setRemark(remark)
        e.setDate(date)
        e.setCategoryId(id)

        app.e.append(e)
        print("Expenses Added!")
        print("-------------------")

    def expenseListing(self):
        count = 1
        print("-------------------")
        for i in app.e:
            catN = self.getCatNameById(i.getCategoryId())
            print(count, ".", catN, "Amount: ", i.getAmount(), "Remark: ", i.getRemark(), "Date: ", i.getDate())
            count += 1
        print("-------------------")

    def getCatNameById(self, catid):
        for i in app.l:
            if i.getCatid() == catid:
                return i.getCatName()

    def reportCatWise(self):
        print("-------------------")
        self.categoryListing()
        num = int(input("select category: "))
        catObj = app.l[num - 1]
        cid = catObj.getCatid()

        for i in app.e:
            if i.getCategoryId() == cid:
                print("Amount: ", i.getAmount(), "Remark: ", i.getRemark(), "Date: ", i.getDate())
        print("-------------------")

    def reportMonWise(self):
        print("-------------------")
        year = input("Enter Year: ")
        month = input("Enter Month: ")
        y = []
        for i in app.e:
            date = i.getDate()
            res = date.split("/")
            y.append(res[2])

        if year in y:
            for i in app.e:
                date = i.getDate()
                res = date.split("/")
                if year == res[2] and month == res[1]:
                    print("Amount: ", i.getAmount(), "Remark: ", i.getRemark(), "Date: ", i.getDate())
        else:
            print("no data found")
        print("-------------------")

    def reportMonRange(self):
        year = input("Enter Year: ")
        startmonth = int(input("Enter start Month: "))
        endmonth = int(input("Enter end Month: "))

        if startmonth > endmonth:
            print("start month should be less than end month")
        else:
            y = []
            for i in app.e:
                date = i.getDate()
                res = date.split("/")

                y.append(res[2])

            if year in y:
                for i in app.e:
                    date = i.getDate()
                    res = date.split("/")
                    if year == res[2]:
                        for j in range(startmonth, endmonth + 1):
                            if str(j) == res[1]:
                                print("Amount: ", i.getAmount(), "Remark: ", i.getRemark(), "Date: ", i.getDate())
            else:
                print("no data found")


app()
