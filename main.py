# The One Stop Insurance Company
# Brady Stringer
# November 29, 2021

# Imports

import time

# Reading OSICDef

while True:

    file = "OSICDef.dat"
    f = open("OSICDef.dat", "r")
    PolicyNumber = (f.readline())
    BasicPremiumRate = (f.readline())
    DiscountAddCar = (f.readline())
    ExtraLiabCov = (f.readline())
    GlassCoverageCost = (f.readline())
    LoanerCoverageCost = (f.readline())
    HSTRate = (f.readline())
    ProcessingFee = (f.readline())
    f.close()

    # Constants
    InsuranceDiscountRate = 651.75
    InsuranceBaseRate = int(869.00)
    ExtraLiabilityCostCon = int(130.00)
    GlassCoverageCostCon = int(86.00)
    LoanerCarCostCon = int(58.00)

    # Inputs

    CustFirstName = input("Enter the customer's first name:  ")
    CustLastName = input("Enter the Customer's last name:  ")
    CustAddress = input("Enter the customer's address:  ")
    CustCity = input("Enter the customers city:  ")
    CustProvince = input("Enter the customer's province:  ")
    CustPostalCode = input("Enter the customers postal code:  ")
    CustPhoneNum = input("Enter the customers phone number:  ")
    NumOfCars = int(input("Enter the number of cars being insured:  "))
    ExtraLiab = input("Enter if you want extra liability (Y/N):  ").upper()
    if ExtraLiab == "N":
        ExtraLiabilityCostCon = 0
    GlassCoverage = input("Enter if you want glass coverage (Y/N):  ").upper()
    if GlassCoverage == "N":
        GlassCoverageCostCon = 0
    LoanerCar = input("Enter if you want a loaner car (Y/N):  ").upper()
    if LoanerCar == "N":
        LoanerCarCostCon = 0
    PayType = input("Enter if you'd rather pay in full or monthly (F/M):  ").upper()

    # Calculations
    TotalPolicies = 1
    TotalPolicies = TotalPolicies + 1
    BaseRate = 869.00
    DiscountRate = 651.75
    PremiumCost = BaseRate + ((NumOfCars - 1) * 651.75)
    TotalExtraCost = NumOfCars * (ExtraLiabilityCostCon + GlassCoverageCostCon + LoanerCarCostCon)
    TotalInsurancePremium = PremiumCost + TotalExtraCost
    HSTTotal = TotalInsurancePremium * 0.15
    TotalCost = TotalInsurancePremium + HSTTotal
    MonthlyPayment = (TotalInsurancePremium + 39.99) / 12

    # Formatting
    PremiumCostStr = "${:,.2f}".format(PremiumCost)
    PremiumCostPad = "{:>10}".format(PremiumCostStr)

    ExtraCostStr = "${:,.2f}".format(TotalExtraCost)
    ExtraCostPad = "{:>10}".format(ExtraCostStr)

    HSTTotalStr = "${:,.2f}".format(HSTTotal)
    HSTTotalPad = "{:>10}".format(HSTTotalStr)

    TotalCostStr = "${:,.2f}".format(TotalCost)
    TotalCostPad = "{:>10}".format(TotalCostStr)

    MonthlyPaymentStr = "${:,.2f}".format(MonthlyPayment)
    MonthlyPaymentPad = "{:>10}".format(MonthlyPaymentStr)

    TotalInsurancePremiumStr = "${:,.2f}".format(TotalInsurancePremium)
    TotalInsurancePremiumPad = "{:>10}".format(TotalInsurancePremiumStr)

    TotalExtraCostStr = "${:,.2f}".format(TotalExtraCost)
    TotalExtraCostPad = "{:>10}".format(TotalExtraCostStr)

    # Receipt Output
    print()
    print("-" * 10, "The One Stop Insurance Company", "-" * 10)
    print("Premium Cost:  {}".format(PremiumCostPad))
    print("Extra Cost:    {}".format(ExtraCostPad))
    print("HST Cost:      {}".format(HSTTotalPad))
    print("Total Cost:    {}".format(TotalCostPad))
    print("-" * 52)
    print("Number of Cars:     {}".format(NumOfCars))
    print("Payment type (F/M): {}".format(PayType))
    print("Monthly Payment:    {}".format(MonthlyPaymentPad))
    print("Customer Name:   {} {}".format(CustFirstName, CustLastName))
    print("Customer Address:   {}".format(CustAddress))
    print("Customer CPP:    {}, {}, {}".format(CustCity, CustProvince, CustPostalCode))
    print("Customer Phone Number:   {}".format(CustPhoneNum))
    print("-" * 52)
    print()

    f = open("Policies.dat", "a")
    f.write("{},".format(str(PolicyNumber)))
    f.write("{},".format(str(CustFirstName)))
    f.write("{},".format(str(CustLastName)))
    f.write("{},".format(str(CustAddress)))
    f.write("{},".format(str(CustCity)))
    f.write("{},".format(str(CustProvince)))
    f.write("{},".format(str(CustPostalCode)))
    f.write("{},".format(str(CustPhoneNum)))
    f.write("{},".format(str(NumOfCars)))
    f.write("{},".format(ExtraLiab))
    f.write("{},".format(GlassCoverage))
    f.write("{},".format(LoanerCar))
    f.write("{},".format(str(PayType)))
    f.write("{}".format(str(TotalCost)))
    f.close()

    print("Saving ...   ", end="Policy Processed and saved")
    for wait in range(1, 11):
        print("*", end=" ")
        time.sleep(.3)
    print()

    PolicyNumber = int(PolicyNumber) + 1

# Write to Default File

    f = open("OSICDef.dat", "w")
    f.write("{}\n".format(str(PolicyNumber)))
    f.write("{}\n".format(str(BasicPremiumRate)))
    f.write("{}\n".format(str(DiscountAddCar)))
    f.write("{}\n".format(str(ExtraLiabCov)))
    f.write("{}\n".format(str(GlassCoverageCost)))
    f.write("{}\n".format(str(LoanerCoverageCost)))
    f.write("{}\n".format(str(HSTRate)))
    f.write("{}\n".format(str(ProcessingFee)))
    f.close()

    Choice = input("If you would like to enter another policy please enter Continue, If you wish to quit enter Exit:  ").title()
    if Choice == "Continue":
        break
    elif Choice == "Exit":
        exit("Thank you for using the program...")

print()
print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF dd-Mon-yy")
print()
print("POLICY CUSTOMER              INSURANCE    EXTRA      TOTAL")
print("NUMBER NAME                   PREMIUM     COSTS     PREMIUM")
print("=" * 59)
print("{} {} {}  {}  {}  {}".format(PolicyNumber, CustFirstName, CustLastName, PremiumCostPad, ExtraCostPad, TotalCostPad))
print(" " * 36, ":")
print(" " * 36, ":")
print("{} {} {}  {}  {}  {}".format(PolicyNumber, CustFirstName, CustLastName, PremiumCostPad, ExtraCostPad, TotalCostPad))
print("=" * 59)
print("Total policies: {}         {} {} {}".format(TotalPolicies, TotalInsurancePremiumPad, TotalExtraCostPad, TotalCostPad))

print()
print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF dd-Mon-yy")
print()
print("POLICY CUSTOMER               TOTAL                 TOTAL      MONTHLY")
print("NUMBER NAME                  PREMIUM      HST       COST       PAYMENT")
print("=" * 59)
print("{} {} {}  {}   {}  {}".format(PolicyNumber, CustFirstName, CustLastName, HSTTotalPad, PremiumCostPad,  TotalCostPad))
print(":")
print("{} {} {}  {}   {}  {}".format(PolicyNumber, CustFirstName, CustLastName, HSTTotalPad, PremiumCostPad,  TotalCostPad))
print("=" * 59)
print("Total policies: {}       {} {}  {}  {}".format(TotalPolicies, TotalInsurancePremiumPad, HSTTotalPad, TotalCostPad, MonthlyPaymentPad))
