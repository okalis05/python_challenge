import os
import csv

#defining my file"s path
file=os.path.join("PyBank/Resources/budget_data.csv")

#reading my file using csv module
with open(file,"r") as csvfile:

    #specifying delimiter and variables to hold contents
        csv_reader = csv.reader(csvfile, delimiter=",")
       # print(csv_reader)

        # reading the header rows first
        csv_header = next(csv_reader)
       # print(f"csv header:{csv_header}")

        #declaring my variables
        total_months=''
        total_profit=''
        average_profit_change=''
        max_increase_profit=''
        max_decrease_profit=''

        #creating variables to store in lists
        months_list=[]
        profits_list=[]
        monthly_profit_change=[]

        #appending lists to their corresponding rows
        for row in csv_reader:
            months_list.append(row[0])
            profits_list.append(int(row[1]))

        #determine the monthly_profit_change
        for i in range(len(profits_list)-1):
            monthly_profit_change.append(profits_list[i+1] - profits_list[i])

        #calculatate total_months,average_profit_change and total_profit.
        total_months = len(months_list)
        total_profit = sum(profits_list)
        average_profit_change = total_profit/total_months

        #determine the max_increase_profit and the max_decrease_profit.
        max_increase_profit = max(monthly_profit_change)
        max_decrease_profit = min(monthly_profit_change)

        #determine the max_ncrease_month and the max_decrease_month.
        max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
        max_decrease_month = monthly_profit_change.index(min(monthly_profit_change))+ 1

        #printing financial statements
        print(f"Financial Analysis")
        print(f"--------------------------------------------")
        print(f"Total Months :{len(months_list)}")
        print(f"Total : $ {sum(profits_list)}")
        print(f"Average Change : $ {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
        print(f"Greatest Increase in Profits: {months_list[max_increase_month]}   ${str(max_increase_profit)}")
        print(f"Greatest Decrease in Profits : {months_list[max_decrease_month]}   ${str(max_decrease_profit)}")

#printing financial statements
with open("PyBank/Analysis/analysis_pybank" ,"w")  as txt_file:
        txt_file.write(f"Financial Analysis\n")
        txt_file.write(f"--------------------------------------------\n")
        txt_file.write(f"Total Months : {len(months_list)}\n")
        txt_file.write(f"Total : ${sum(profits_list)}\n")
        txt_file.write(f"Average Change : ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
        txt_file.write(f"Greatest Increase in Profits: {months_list[max_increase_month]}   ${str(max_increase_profit)}\n")
        txt_file.write(f"Greatest Decrease in Profits : {months_list[max_decrease_month]}   ${str(max_decrease_profit)}\n")
