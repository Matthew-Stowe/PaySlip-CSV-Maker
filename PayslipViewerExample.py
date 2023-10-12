import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

Pay_Slip = open("Pay4.pdf", "rb")
Viewer = SimplePDFViewer(Pay_Slip)   #Creates instance of PDF Viewer to look at specific payslip

Viewer.navigate(1)                  #find page 1
Viewer.render()                     #renders page 1 for Viewer to see



#--Collecting PDF Text--
#
#collects string from all pages in doc
#we are only looking at one page so we dont need this
""""
for canvas in Viewer:
    PSInfo = canvas.strings
"""

#instead we can look straight at singlular canvas element
PS_Strings = Viewer.canvas.strings



#--Finding Net Pay Item from List--
#
""""
Net_Pay_Idx = int(PS_Strings.index("Net Pay"))     #find index of "Net Pay" Text
Net_Pay_int = float(PS_Strings[Net_Pay_Idx + 1])    #"Net Pay" ammount will allways be next item in list

print(Net_Pay_int)
"""
#
#Due to the large list size, this option is slow
#Instead give the index() method a starting and ending postion; making the method search through less items
#This method is not very scalable if payslip format were to change
#
Net_Pay_Idx = int(PS_Strings.index("Net Pay", 40, 50))      #placed index search between 40 and 50 as a median point
Net_Pay_Int = PS_Strings[Net_Pay_Idx + 1]

print(Net_Pay_Int)







#Allways do this :)
Pay_Slip.close()