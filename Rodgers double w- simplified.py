print("Congraulations on taking the steps towards financial independence.")
invest = float(input("\nHow much will you be investing today? \n"))
orig_invest = invest
interest = float(input("\nHow much is the proposed annual interest rate, as a percentage?\n"))
interest = interest * 0.01       
count_Years = 0
double_inv = 2*invest
while invest <= double_inv:
    invest = (orig_invest * interest) + invest
    count_Years +=1
    if count_Years == 45:
        break
print("\nIt will take you at least ",count_Years,"years to at least double your investment of $",orig_invest, " using simplified interest.")
