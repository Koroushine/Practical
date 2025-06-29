def total(sales):
    sales_per_day = sales/7
    sales_per_month = sales_per_day*30
    comm = 0
    remark = ""

    if sales_per_month >= 50000:
        comm = 0.05*sales_per_month
    
    totalsales = sales_per_month + comm

    if sales_per_month >= 80000:
        remark = "Excellent"
    elif 60000 <= sales_per_month<80000:
        remark = "Good"
    elif 40000 <= sales_per_month<60000:
        remark = "Average"
    elif sales_per_month < 40000:
        remark = "Work hard"
    else:
        remark = "Invalid"
    return totalsales, comm, remark

if __name__=="__main__":
    salesmen = ['Tom', 'Jevin', 'Korou', 'John']
    sales = []

    for i in range(len(salesmen)):
        inp = float(input(f"Enter the sales of {salesmen[i]} : "))
        sales.append(inp)
        
    for i in sales:
        ts, c, r = total(i)
        print(f"The total sales is {round(ts, 2)}, commission is {round(c, 2)} and the remark is {r}")