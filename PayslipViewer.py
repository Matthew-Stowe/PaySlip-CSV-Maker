import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
import os
import shutil
import csv


class PaySlips:
    def __init__(self, FileName, PayWeek = 0, PayAmount = 0.00, PayDate = "", FindDetailsFlag = False, CSVData = []):
        self.FileName = FileName
        self.PayWeek = PayWeek
        self.PayAmount = PayAmount
        self.PayDate = PayDate
        self.CSVData = CSVData

        self.FindDetailsFlag = FindDetailsFlag

    def __str__(self):                                              #returns the following string if PaySlip refrenced
        return f"{self.PayAmount} {self.PayWeek} {self.PayDate}"

    #To be ran to for each instace to get details of PaySlip
    #This could be put in __init__ to create less instances of SimplePDFViewer
    def FindDetails(self):                      
        with open(self.FileName, "rb") as PDF:
            Viewer = SimplePDFViewer(PDF)       #creates instace of PDF Viewer
            Viewer.navigate(1)                  #open page 1 (the only page in current pay slip format)
            Viewer.render()

            PDF_Strings = Viewer.canvas.strings #creats list of all strings in PDF

            PDF_PayAmountIDX = 0    #Index of Pay Total
            PDF_PayAmount = 0.00    #Pay Total
            PDF_PayDateIDX = ""     #Index of Pay Date
            PDF_PayDate = ""        #Pay Date
            PDF_PayWeekIDX = 0
            PDF_PayWeek = 0
            

            #Strings to index for are:
            #   "Net Pay"
            #   "Pay Date"
            #
            #   Pay Amount = Net Pay Index + 1
            #   Pay Date = Pay Date + 9
            
            # These index interation amounts should stay the same as long as the format stay the same


            #--Finding Index's and Amounts--
            PDF_PayAmountIDX = PDF_Strings.index("Net Pay") + 1
            PDF_PayAmount = PDF_Strings[PDF_PayAmountIDX]
            
            PDF_PayDateIDX = PDF_Strings.index("Pay Date") + 9
            PDF_PayDate = PDF_Strings[PDF_PayDateIDX]

            PDF_PayWeekIDX = PDF_Strings.index("Week") + 9
            PDF_PayWeek = PDF_Strings[PDF_PayWeekIDX]

            #--Assigning Atributes--
            self.PayAmount = float(PDF_PayAmount)
            self.PayDate = str(PDF_PayDate)
            self.PayWeek = int(PDF_PayWeek)

            self.FindDetailsFlag = True     #changes flag to True to allow for other methods to work

    def FormatFileName(self):
        if self.FindDetailsFlag == True:                            #checks if FindDetails has been called yet
            OldFileDir = self.FileName                              #current file directory
            NewFileName = f"Payslip_Week_{self.PayWeek}.PDF"        #format string of what the new file name should be

            print(OldFileDir)
            print(NewFileName)


            os.rename(OldFileDir, NewFileName)                  #changes name to new formated name
            self.FileName = NewFileName                         #change current FileName atribute to the new formated name

            shutil.move(self.FileName, "PaySlips/")             #moves PDF file to PaySlips Folder


        else:
            raise Exception("self.FindDetailsFlag if flase | Try running self.FindDetails to set flag to true")     #must run FindDetails stirng first in order to get PayWeek number Detials

    def GetCSVData(self):
        if self.FindDetailsFlag == True:
            data = [f"{self.PayDate}",f"{self.PayWeek}",f"{self.PayAmount}"]
            self.CSVData = data

        else:
            raise Exception("self.FindDetailsFlag if flase | Try running self.FindDetails to set flag to true")     #must run FindDetails stirng first in order to get PayWeek number Detials


#This should be made into a class
def FormatFiles():                                  #formats all files in PaySlips Folder
    PaySlipList = os.listdir("PaySlips/")
    for PaySlip in PaySlipList:
        PaySlipFileName = f"PaySlips/{PaySlip}"     #PaySlipDir

        PaySlip = PaySlips(PaySlipFileName)         #Creats Instance of PaySlips for each Payslip in folder

        PaySlip.FindDetails()
        PaySlip.FormatFileName()

        print("Complete")

    return 0



def MakeCSV():
    PaySlipList = os.listdir("PaySlips/")

    filename = "CombinedPayslipInfo.csv"

    feilds=["Date","Week","AmountPaid"]           #Feild of CSV
    rows=[]                                       #Rows of CSV (empty of the moment)


    #--Getting Data From Payslips--
    for PaySlip in PaySlipList:
        PaySlipFileName = f"PaySlips/{PaySlip}"     #PaySlipDir

        PaySlip = PaySlips(PaySlipFileName)         #Creates Instance of PaySlips for each Payslip in folder

        PaySlip.FindDetails()
        PaySlip.GetCSVData()

        rows.append(PaySlip.CSVData)

    #--Ammeding to Correct File--
    with open("PayslipInfo.csv", "w") as CSVFile:
        #creates an instace of csv writer OBJ
        csvwrtier = csv.writer(CSVFile)

        #writing feilds (first line)
        csvwrtier.writerow(feilds)

        #writing rows/data (going down from feilds)
        csvwrtier.writerows(rows)

    return 0

