#Jocelyn Lee and Alex Trudeau
#Choose Your Own Adventure Game
#November 12, 2016

import time
from random import *
import sys
from string import *

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        #time.sleep(0.015)

#introductions
print_slow( "Welcome to Jocelyn and Alex's Manage Your Money game!\n")
name = raw_input("Please enter your name: ")

print_slow( "Hello " + name + "!\n")
print_slow( "It's your high school graduation. Graduating high school was tough, but university will be much harder.\n")

#choosing degree
print_slow( "It's time to pick your major! Here are your choices:\n")
majors = ["(1) Business", "(2) Engineering", "(3) Science"]
for i in range(len(majors)):
    print_slow( majors[i])
    print

selection = input("Please type the number of the major you want to take: ")

newmajors = ["Business", "Engineering", "Science"]
major = newmajors[selection-1]
if major == newmajors[0]:
    print_slow( "You selected Business! Good choice! With a business degree, you can specialize in finance, management, or retail.\n")
    print_slow( "The median starting pay for business majors is $50,000. With the average degree costing around $25,000 over 4 years, it sure adds up!\n")
    studying = "business"
    pay = 50000
    schoolfeestotal = 25000
    
elif major == newmajors[1]:
    print_slow( "You selected Engineering! Good choice! With an engineering degree, there are many different specializations, such as mechanical engineering, software engineering, and civil engineering.\n")
    print_slow( "The median starting pay for engineering majors is around $80,000. With the average degree costing around $85,000 over 4 years, it sure adds up!\n")
    studying = "engineering"
    pay = 80000
    schoolfeestotal = 85000
    
elif major == newmajors[2]:
    print_slow( "You selected Science! Good choice! With a science degree, you can work towards becoming a chemist, physist, or botanist.\n")
    print_slow( "The median starting pay for science majors is around $60,000. With the average degree costing $60,000 over 4 years, it sure adds up!\n")
    studying = "science"
    pay = 60000
    schoolfeestotal = 60000

print
print_slow( "Since you are on your own now, you are going to need to find a way to pay for schooling. There are two different types of student loans: Federal and Private.\n")
print_slow( "Federal loans offer low, fixed interest rates. They are given based on need, so the amount you get is based on the gross income of your household.\n")
print_slow( "Private loans have variable interest rates. In addition, they are also given out based on your credit. If you have bad credit, banks may not lend you money.\n")
print
print_slow( "With this information, what kind of loan do you want to take out?\n")
loans = ["(1) Federal", "(2) Private"]
for i in range(len(loans)):
    print_slow( loans[i])
    print

loanchoice = input("Please type the number for the kind of loan you wish to take out: ")
loantype = ["Federal", "Private"]
loans = loantype[loanchoice-1]

if loans == loantype[0]:
    print_slow( "You have selected Federal Loans.\n")
    apr = 0.03
    print
    print_slow( "Federal Loans have a 3% APR (Annual Percentage Rate).\n")
    print_slow( "This means that every year, the total amount you owe for your loan increases by 3%.\n")
    paying = "federal"
    
if loans == loantype[1]:
    print_slow( "You have selected Private Loans.\n")
    print_slow( "You forget to do your research ahead of time, so you go into a bank, and they tell you their APR (Annual Percentage Rate).\n")
    apr1 = randrange(300,800,1)
    apr2 = apr1/100.0
    apr = apr1/10000.0
    print
    print_slow( "After waiting for a period of time, the banks tell you that your APR is " + str(apr2) + "%.\n")
    print_slow( "This means that every year, the total amount you owe for your loan increases by  " + str(apr2) + "%.\n")
    paying = "private"
    
print
print_slow( "Congratulations on picking a loan! This will definitely help you finish school and get one step closer to starting your life in the work force.\n")
print_slow( "In your " + studying + " major, you are going to need to take out a loan to cover the cost of schooling, wich will be $" + str(pay) + " over 4 years.\n")
print
jobchoice = str.upper(raw_input("Do you want to get a part time job? (Y/N): "))

if jobchoice == 'Y':
    print_slow( "In your area, the only jobs that are available are minimum wage jobs, covering 10 hours per week.\n")
    print_slow( "This means that you will be earning $5,850 per year, and you can start paying back your loans.\n")
    yourjob = raw_input("Please enter the job you want to have: ")
    print_slow( "Congrats! You are now employed as a " + yourjob + "!\n")

elif jobchoice == 'N':
    print_slow( "Ok. This means that you will not start earning money until after you graduate from university.\n")

print

#functions
def RandomEvents(schoolevent, cost, i):
    if schoolevent[i] == 1:
        print_slow( "You are walking to class and you drop your laptop in a puddle! You have to pay $1000 to get a new one.\n")
        cost -= 1000
        
    elif schoolevent[i] == 2:
        print_slow( "You do really well in your math class and are offered a scholarship! The scholarship is worth $2500.\n")
        cost += 2500
        
    elif schoolevent[i] == 3:
        print_slow( "Your team is going to the finals this year in Calgary! You have to pay $1500 for travel fees.\n")
        cost -= 1500

    elif schoolevent[i] == 4:
        print_slow( "On a rock climbing trip with your friends, you broke your leg and health insurance won't cover it! You are charged $500.\n")
        cost -= 500

    elif schoolevent[i] == 5:
        print_slow( "Your lottery ticket won at the grocery store! You won $350.\n")
        cost += 350

    elif schoolevent[i] == 6:
        print_slow( "Your hometown team planned in the NBA finals this year! You bought tickets with your friends for $350.\n")
        cost -= 350

    elif schoolevent[i] == 7:
        print_slow( "In a case competition, your team won the grand prize! The prize was $1000.\n")
        cost += 1000

    elif schoolevent[i] == 8:
        print_slow( "You found a loophole in your tuition that allows you to opt out of dental fees. You get $300.\n")
        cost += 300

    elif schoolevent[i] == 9:
        print_slow( "You and all your friends decide to go on a spring break trip. The total cost of the trip was $950.\n")
        cost -= 950

    elif schoolevent[i] == 10:
        print_slow( "Your community involvement gets noticed by some important people! You were nominated for a Citizenship Award, valued at $750.\n")
        cost += 750

    return cost

def SchoolFee(newmajors, schoolfeestotal):
    startschoolfee = schoolfeestotal/4
    return startschoolfee

def GiveMeMoney(PlsMoney, schoolfees, loanstartbalance, loanendbalance):
    if PlsMoney == "Y":
        loanstart = loanendbalance + schoolfees/2
    if PlsMoney == "N":
        loanstart = loanendbalance + loanstartbalance
    return loanstart

def LoanTakeOut(loanstart, apr):
    loanend = loanstart *(1+apr)
    return loanend

def DollaBills(jobchoice, monies):
    if jobchoice == "Y":
        monies = 5850
    elif jobchoice =="N":
        monies = 0
    return monies

def CheckOut(PlsMoney, loanendbalance, loanremaining):
    if PlsMoney == "Y":
        loanremaining = loanendbalance - loanremaining
    if PlsMoney == "N":
        loanremaining = loanendbalance
    return loanremaining

def PayingSucks(PlsMoney, moneylefttopay, jobsalary, extracosts, loanstartbalance):
    if PlsMoney == "Y":
        totalz = startbalance - moneylefttopay + jobsalary + extracosts
    elif PlsMoney == "N":
        totalz = startbalance + jobsalary + extracosts
    return totalz

print_slow( "At the beginning of every school year, you have to pay for your school fees and you recieve a payment of your loan.\n")
print_slow( "The loan covers 50% of your tuition every year.\n")
print_slow( "At the end of every year, you get paid and you can use it to pay back your loan if you want to. Any additional costs incurred are added to your end balance. \n")
print_slow( " When you start university, you have $20,000 in the bank, and you don't have to start paying back your loan until 4 years after you graduate if you don't want to.\n")
print
schoolevent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(schoolevent)

schoolfees = 0
loanstart = 0
startbalance = 20000
loanend = 0
jobsalary = 0
extracosts = 0
endbalance = 0
PlsMoney = "Y"
print
print_slow( "Starting Account Balance = $20,000\n")
print
print_slow( "**********YEAR ONE**********\n")
schoolfees = SchoolFee(major,schoolfeestotal)
print_slow( "School Fees = $" + str(schoolfees) + "\n")

loanstartbalance = schoolfees/2
print_slow( "Loan Balance = $" + str(loanstartbalance)+ "\n")

startbalance = -schoolfees + loanstartbalance + startbalance
print_slow( "Starting Account Balance = $" + str(startbalance)+ "\n")
print
print_slow( "Your first year is going well, " + name + " ! You are doing well in a lot of your classes, and are making lots of friends.\n")
print
extracosts = RandomEvents(schoolevent, extracosts, 0)
print

loanendbalance =LoanTakeOut(loanstartbalance, apr)
PlsMoney = str.upper(raw_input("Do you want to use your money to pay back your loan now? (Y/N): "))
loanremaining = 0
moneylefttopay = CheckOut(PlsMoney, loanendbalance, loanremaining)
print_slow( "Loan End = $" + str(moneylefttopay)+ "\n")

monies = 0
jobsalary = DollaBills(jobchoice, monies)
print_slow( "Job Salary = $" + str(jobsalary)+ "\n")

print_slow( "Extra Costs = $" + str(extracosts)+ "\n")

monies = 0
endbalance = PayingSucks(PlsMoney, loanendbalance, jobsalary, extracosts, loanstartbalance)
print_slow( "Ending Account Balance = $" + str(endbalance)+ "\n")
print

print_slow( "**********YEAR TWO**********\n")
schoolfees = (SchoolFee(major,schoolfeestotal))
print_slow( "School Fees = $" + str(schoolfees)+ "\n")

loanstartbalance = moneylefttopay + schoolfees/2
print_slow( "Loan Balance = $" + str(loanstartbalance)+ "\n")

startbalance = endbalance - schoolfees + loanstartbalance
print_slow( "Starting Account Balance = $" + str(startbalance)+ "\n")
print
print_slow( "You are rocking your second year, " + name + " ! You have started to develop an idea of what you want to do with your life once you graduate.\n")
print
extracosts = 0
extracosts = RandomEvents(schoolevent, extracosts, 1)

print

loanendbalance =LoanTakeOut(loanstartbalance, apr)
PlsMoney = str.upper(raw_input("Do you want to use your money to pay back your loan now? (Y/N): "))
moneylefttopay = CheckOut(PlsMoney, loanendbalance, loanremaining)
print_slow( "Loan End = $" + str(moneylefttopay)+ "\n")

jobsalary = DollaBills(jobchoice,monies)
print_slow( "Job Salary = $" + str(jobsalary)+ "\n")

print_slow( "Extra Costs = $" + str(extracosts)+ "\n")

endbalance = PayingSucks(PlsMoney, loanendbalance, jobsalary, extracosts, loanstartbalance)
print_slow( "Ending Account Balance = $" + str(endbalance)+ "\n")
print

print_slow( "**********YEAR THREE**********\n")
schoolfees = (SchoolFee(major,schoolfeestotal))
print_slow( "School Fees = $" + str(schoolfees)+ "\n")

loanstartbalance = GiveMeMoney(PlsMoney, schoolfees, loanstartbalance,loanendbalance)
print_slow( "Loan Balance = $" + str(loanstartbalance)+ "\n")

startbalance = endbalance - schoolfees + loanstartbalance
print_slow( "Starting Account Balance = $" + str(startbalance)+ "\n")
print
print_slow( "You're third year is going great , " + name + "! It's time to hit the books and really buckle down to prepare for your last year!\n")
print
extracosts = 0
extracosts = RandomEvents(schoolevent, extracosts, 2)

print

loanendbalance =LoanTakeOut(loanstartbalance, apr)
PlsMoney = str.upper(raw_input("Do you want to use your money to pay back your loan now? (Y/N): "))
moneylefttopay = CheckOut(PlsMoney, loanendbalance, loanremaining)
print_slow( "Loan End = $" + str(moneylefttopay)+ "\n")

jobsalary = DollaBills(jobchoice, monies)
print_slow( "Job Salary = $" + str(jobsalary)+ "\n")

print_slow( "Extra Costs = $" + str(extracosts)+ "\n")

endbalance = PayingSucks(PlsMoney, loanendbalance, jobsalary, extracosts, loanstartbalance)
print_slow( "Ending Account Balance = $" + str(endbalance)+ "\n")
print

print_slow( "**********YEAR FOUR**********\n")
schoolfees = (SchoolFee(major,schoolfeestotal))
print_slow( "School Fees = $" + str(schoolfees)+ "\n")

loanstartbalance = GiveMeMoney(PlsMoney, schoolfees, loanstartbalance,loanendbalance)
print_slow( "Loan Balance = $" + str(loanstartbalance)+ "\n")

startbalance = endbalance - schoolfees + loanstartbalance
print_slow( "Starting Account Balance = $" + str(startbalance)+ "\n")
print
print_slow( "You are blazing through your fourth and final year, " + name + "! You're ready to enter the work force and find your dream job!.\n")
print
extracosts = 0
extracosts = RandomEvents(schoolevent, extracosts, 3)

print

loanendbalance =LoanTakeOut(loanstartbalance, apr)
PlsMoney = str.upper(raw_input("Do you want to use your money to pay back your loan now? (Y/N): "))
moneylefttopay = CheckOut(PlsMoney, loanendbalance, loanremaining)
print_slow( "Loan End = $" + str(moneylefttopay)+ "\n")

jobsalary = DollaBills(jobchoice, monies)
print_slow( "Job Salary = $" + str(jobsalary)+ "\n")

print_slow( "Extra Costs = $" + str(extracosts)+ "\n")

#total before graduating
endbalance = PayingSucks(PlsMoney, moneylefttopay, jobsalary, extracosts, loanstartbalance)
print_slow( "Ending Account Balance = $" + str(endbalance) + "\n")
if jobchoice == "Y":
    print_slow("That part-time job really helped to pay off of some of your student loans! It has really made a differece over the four years.\n")
elif jobchoice == "N":
    print_slow("That is a big total! Maybe if you had a part-time job, you could have paid off more of your student loans!\n")
print

#done graduation starting transition to working force
print
print_slow( "After four years of university, you have graduated with an end account balance of $" + str(endbalance) + " .\n")
print_slow( "The total cost you have to pay on your loan is $" + str(moneylefttopay) +" .\n")
print
GradPayment = str.upper(raw_input("Would you like to pay the remainder of your loan now? (Y/N): "))

if GradPayment == "Y":
    total = endbalance - moneylefttopay
    print_slow( "The new total you have in your bank account is $" + str(total) + ".\n")
elif GradPayment == "N":
    while(GradPayment == "N"):
        print_slow( "Are you sure that's a good idea? If you don't pay the remainder now, it will continue to compound interest, and will cost you more later down the road.\n")
        GradPayment = str.upper(raw_input("Would you like to pay the remainder of your loan now? (Y/N): "))
    total = endbalance - moneylefttopay
    print_slow( "The new total you have in your bank account is $" + str(total) + ".\n")



#worktime!! money time!


if major == newmajors[0]:
    print_slow( "Congratulations on your business degree! What job would you like to apply for?\n")
    print
    businessjobs = ["(1) Sales Manager: $60,000/year", "(2) Financial Analyst: $66,000/year", "(3) Public Relations Coordinator: $50,000/year"]
    print
    for i in range(len(businessjobs)):
        print_slow( businessjobs[i])
        print
    businessSelection = input("Please type the number of the business job you want to apply for: ")
    print
    print_slow( "Wow! The company was really impressed by your degree and skills, " + name + "! They want to hire you right away!\n")
    newBusinessjobs = ["Sales Manager", "Financial Analyst", "Public Relations Coordinator"]
    businessjobs = newBusinessjobs[businessSelection-1]
    if businessjobs == newBusinessjobs[0]:
        print_slow( "You are going to love you new position as a Sales Manager. With a $60,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 60000
    elif businessjobs == newBusinessjobs[1]:
        print_slow( "You are going to love your new position as a Financial Analyst. With a $66,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 66000
    elif businessjobs == newBusinessjobs[2]:
        print_slow( "You are going to love your new position as a Public Relations Coordinator. With a $50,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 50000
    print
print

if major == newmajors[1]:
    print_slow( "Congratulations on your engineering degree! What job would you like to apply for?\n")
    print 
    engineeringjobs = ["(1) Civil Engineer: $60,000/year", "(2) Software Developer: $69,000/year", "(3) Materials Engineer: $70,000/year"]
    print
    for i in range(len(engineeringjobs)):
        print_slow( engineeringjobs[i])
        print
    engineeringSelection = input("Please type the number of the engineering job you would like to apply for: ")
    print
    print_slow( "Wow! The company was really impressed by your degree and skills, " + name + "! They want to hire you right away!\n")
    newEngineeringjobs = ["Civil Engineer", "Software Developer", "Materials Engineer"]
    engineeringjobs = newEngineeringjobs[engineeringSelection-1]
    print
    if engineeringjobs == newEngineeringjobs[0]:
        print_slow( "You are going to love you new position as a Civil Engineer. With a $60,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 60000
    elif engineeringjobs == newEngineeringjobs[1]:
        print_slow( "You are going to love your new position as a Software Developer. With a $69,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 69000
    elif engineeringjobs == newEngineeringjobs[2]:
        print_slow( "You are going to love your new position as a Materials Engineer. With a $70,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 70000
    print
print

if major == newmajors[2]:
    print_slow( "Congratulations on your science degree! What job would you like to apply for?\n")
    print
    sciencejobs = ["(1) Chemist: $40,000/year", "(2) Physicist: $60,000/year", "(3) Botanist: $80,000/year"]
    print
    for i in range(len(sciencejobs)):
        print_slow( sciencejobs[i])
        print
    scienceSelection = input("Please type the number of the science job you want to apply for: ")
    print
    print_slow( "Wow! The company was really impressed by your degree and skills, " + name + "! They want to hire you right away!\n")
    print
    print
    newSciencejobs = ["Chemist", "Physicist", "Botanist"]
    sciencejobs = newSciencejobs[scienceSelection-1]
    if sciencejobs == newSciencejobs[0]:
        print_slow( "You are going to love you new position as a Chemist. With a $40,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 40000
    elif sciencejobs == newSciencejobs[1]:
        print_slow( "You are going to love your new position as a Physicist. With a $60,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 60000
    elif sciencejobs == newSciencejobs[2]:
        print_slow( "You are going to love your new position as a Botanist. With a $80,000 salary, you should start thinking about what to do with your money!\n")
        JobMoney = 80000
    print
    
print
print_slow( "Your first month at your job is great! Your boss offers to give you a 10% bonus for this month.\n")
total = total + (JobMoney* 0.10)
print_slow( "Your total is now: $" + str(total) + "\n")
print

print_slow( "Remember when we talked about thinking about what to do with your money? There is no better time than now!\n")
print_slow( "There are a few different investment types to choose from, and they are dependent on your preferences.\n")
print_slow( "There are three main types of investments in relation to time: short term goals, mid-term goals, and long-term goals.\n")
print

#exerpts taken from finra.org
#short term
print_slow( "With short term goals, the focus is on safety and liquidity rather than growth in your short-term portfolio.\n")
print_slow( "You will be more inclined to put your money into federally insured bank or credit union accounts or cash equivalent investments.\n")
print_slow( "This is because they are less likely to lose much value in short periods of time.\n")
print_slow( "Cash investments typically pay lower interest rates than longer-term bonds.\n")
print

shortInvestment = [["Short-Term Government Bonds", "Money Market Funds", "Guaranteed Investment Certificate"],[0.50, 1.00, 0.33]]
for i in range(len(shortInvestment) + 1):
    print_slow("(" + str(i+1) + ")" + str(shortInvestment[0][i]) + " costs $" + str(shortInvestment[1][i]) + " per share.\n")
    print
print_slow("Short-Term Government Bonds are issued by the government with a promise of repayment upon the security's mature date.\n")
print_slow("Money Market Funds are mutual funds that invest in short-term debt securities. They are regarded to be as safe as bank deposits, but have higher yields. \n")
print_slow("Guaranteed Investment Certificates are investments that offer a guaranteed rate of return over a fixed period of time.\n")
print

quote = "N"
answer = quote
while answer == "N":
    sChosenIndex = input("Enter the number of the bond you would like to buy: ")
    sChosen = shortInvestment[0][sChosenIndex -1]
    sQuantity = input("Enter the quantity of bond you would like to buy of " + str(sChosen) + ": ")
    sstockTotalPrice = sQuantity * shortInvestment[1][sChosenIndex -1]
    print_slow( "The quote for this transaction is " + str(sstockTotalPrice) + "\n.")
    answer = str.upper(raw_input("Would you like to proceed with this transaction? (Y/N): "))
print_slow( "You have spent " + str(sstockTotalPrice) + " on bond " + str(sChosen)+ "\n.")
total = total - sstockTotalPrice
print

#mid term
print_slow( "With mid-term goals, a balance needs to be struck between protecting assets you have accumulated and maintaining growth to build your assets and offset inflation.\n")
print_slow( "The more time you have, the more risk you can afford to take. You may want to invest some of your assets in stocks through mutual funds or exchange-traded funds.\n")
print_slow( "Consider using balanced funds, which invest in a mix of around 60 % stock to 40% bonds, growth and income funds, or equity income funds.\n")
print_slow( "The key is to achieve modest growth while minimizing risk. This can be done by keeping a close eye on performance and gradually shifting to mroe stable, income-producing investments.\n")
print

midInvestment = [["Savings Account", "Bond Index Fund", "Stock Index Fund"],[0.01, 0.05, 0.10]]
for i in range(len(midInvestment) + 1):
    print_slow("(" + str(i+1) + ")" + str(midInvestment[0][i]) + "has an interest rate of " + str(midInvestment[1][i]))
    print
print_slow("Savings account are bank accounts that earn interest over time. \n")
print_slow("Bond Index Funds invest in bonds or other debt securities. They pay periodic dividents that include interest payments. \n")
print_slow("Stock Index Funds are a fund with a portfolio constructed to match or track components of a market index. \N")
print

quote = "N"
answer = quote
while answer == "N":
    mChosenIndex = input("Enter the number of the investement you would like to invest in: ")
    mChosen = midInvestment[0][mChosenIndex -1]
    mQuantity = input("Enter the amount of money you would like to invest in a " + str(mChosen) + ": ")
    mOneYear = mQuantity * midInvestment[1][mChosenIndex -1]
    print_slow( "The quote for this transaction is " + str(mQuantity) + "\n.")
    answer = str.upper(raw_input("Would you like to proceed with this transaction? (Y/N): "))
print_slow( "You have spent " + str(mQuantity) + " on stock " + str(mChosen) + "\n.")
total = total - mQuantity
print


#long term
print_slow( "Long term goals are goals with a long time horizon. It is important to make your money work for you.\n")
print_slow( "This means earning a rate of return that outpaces inflation, and allows your principal investment to grow over time.\n")
print_slow( "Since it is a long period of time, you can afford to take more risk. This can mean allocating most of the principal stock you set aside for growth investments.\n")
print

longInvestment = [["Avid Technology (AVID)","Louisiana-Pacific Corporation (LPX)","Southwest Airlines (LUV)"],[ 9.20, 18.60, 31.36]]
for i in range(len(longInvestment)+1):
    print_slow("(" + str(i+1) + ")" + str(longInvestment[0][i]) + " costs $" + str(longInvestment[1][i]) + " per share.\n")
    print

print_slow("Stocks are bought individually, and their prices fluctuate with the market.They are high risk, but high reward. \n")
print

quote = "N"
answer = quote
while answer == "N":
    lChosenIndex = input("Enter the number of the stock you would like to buy: ")
    lChosen = longInvestment[0][lChosenIndex - 1]
    lPrice = longInvestment[1][lChosenIndex - 1]
    lQuantity = input("Enter the quantity of stock you would like to buy of " + str(mChosen) + ": ")
    lstockTotalPrice = lQuantity * lPrice
    print_slow( "The quote for this transaction is " + str(lstockTotalPrice) + "\n.")
    answer = str.upper(raw_input("Would you like to proceed with this transaction? (Y/N): "))
print_slow( "You have spent " + str(lstockTotalPrice) + " on stock " + str(lChosen) + "\n.")
total = total - lstockTotalPrice
print


stockevent = [1, 2, 3, 4, 5, 6]


def StockEvents(stockevent, cost, i):
    if stockevent[i] == 1:
        print_slow( "Britan has left the European Union! Markets around the world crash, and your stock plummets by $4.03.\n")
        cost -= -4.03
        
    elif stockevent[i] == 2:
        print_slow("New products have been released for the company! Your stock increases by $2.30.\n")
        cost += 2.30
        
    elif stockevent[i] == 3:
        print_slow(" The company announcned plans to expand today. Your stock increases by $0.54. \n")
        cost += 0.54
        
    elif stockevent[i] == 4:
        print_slow(" The comapny announced plans to downsize. Your stock goes down by $0.73.\n")
        cost -= 0.73
                   
    elif stockevent[i] == 5:
        print_slow("The CEO of the company resigned. Your stock goes down by $0.21. \n")
        cost -= 0.21

    elif stockevent[i] == 6:
        print_slow("The company annouces its new strategic plan with goals of achieving better sustainability metrics. Your stock increases by $0.43. \n")
        cost += 1.43
    return cost
yearsPassed = randint(1,4)
for i in range(yearsPassed):
    shuffle(stockevent)
    gainInInvestment = (StockEvents(stockevent, lPrice, 0) - lPrice)*lQuantity
    lstockTotalPrice += gainInInvestment
print_slow("... \n")
print_slow(str(yearsPassed) + " year(s) later \n")
print_slow("... \n")


answer = str.upper(raw_input("Would you like to sell your stock and make " + str(lstockTotalPrice) + " back? (Y/N) : "))

gainOnMidInvestment = 0
for i in range(yearsPassed):
    gainOnMidInvestment = (gainOnMidInvestment + mQuantity) * midInvestment[1][mChosenIndex -1]
if answer == "Y":
    total = '%.2f'%(float(total) - float(lstockTotalPrice) + float(gainOnMidInvestment) + float(JobMoney*yearsPassed))
else:
    total = '%.2f'%(float(total) + float(gainOnMidInvestment) + float(JobMoney*yearsPassed))

print_slow("You have an ending account balance of: " + str(total) +" after " + str(yearsPassed) +"\n")
print_slow( "This was calculated by your ending account balance after university, your loss/gain on investments and stocks, your student loan debt, and your salary after " + str(yearsPassed) + " years\n")
print_slow("The financial world is always full of surprises, and some can be predicted through market analysis, while others are rather spontaneous and unpredicated.\n")
print_slow("As an investor, you must respect the integrity of the market and play your cards right if you want to make a positive return on your investments.\n")
print_slow("At the end of the day, it's you and your money, so you can invest it how you like. Hopefully after playing this game, you'll have learned a few things about investing and will apply them to the real world.\n")
#end comments
print_slow( "\n Thank you for playing the Money Management Game by Jocelyn Lee and Alex Trudeau! Remember, this is only the start to becoming financially literate.\n")
print_slow( "There are many more [accurate] resources online that you can access to learn more about how to manage your money.\n")
