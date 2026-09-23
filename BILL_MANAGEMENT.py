from reportlab.pdfgen import canvas
import os
from datetime import datetime

def bill_management(c_room,c_r_type,cr_bill,s_bill,c_name,c_phno):

    print("BILL MANAGEMENT")
    print(f'CUSTOMER NAME: {c_name}')
    print(f'CUSTOMER PHONE: {c_phno}')
    print(f'STAY TYPE: {c_r_type}')
    print(f'ROOM NO: {c_room}')
    print(f'TOTAL PRICE FOR THE ROOM: {cr_bill}')
    print(f'TOTAL SERVICE BILL: {s_bill}')
    print(f'INCLUDED GST: ',"18%")
    Total_bill = cr_bill + s_bill
    Final_bill = ((18/100)*Total_bill) + Total_bill
    print(f'TOTAL BILL: ',Final_bill)

    while True:
        p_bill = input("TYPE 'PAY' TO PAY THE BILL: ")
        if p_bill == 'PAY':
            print("PAYMENT SUCCESSFUL")
            now = datetime.now()
            pdf = canvas.Canvas(f'./Database/Customers_Billing_History/{c_name}({now.strftime("%d-%m-%Y_%H-%M")}).pdf')


            pdf.setFont('Helvetica-Bold', 12)
            pdf.drawString(250, 800,"HOTEL 7* STAR")
            pdf.setFont('Helvetica-Bold', 7)
            pdf.drawString(200, 850,"HOTEL BILL")

            pdf.setFont('Helvetica', 12)
            pdf.drawString(50, 750,f'Customer Name: {c_name}')
            pdf.drawString(50, 730,f'Customer Phone: {c_phno}')
            pdf.drawString(50, 710,f'Stay Type: {c_r_type}')

            pdf.line(50,690,550,690)

            pdf.drawString(50,660,f'Total Room Bill: ')
            pdf.drawString(450,660,f'{cr_bill}')
            pdf.drawString(50,630,f'Total Service Bill: ')
            pdf.drawString(450,630,f'{s_bill}')

            pdf.drawString(50,600,f'Total Included GST(18%)')
            pdf.drawString(450,600,f'{(18/100)*Total_bill}')

            pdf.line(50,570,550,570)

            pdf.setFont('Helvetica-Bold', 14)
            pdf.drawString(50, 540,"FINAL BILL:")
            pdf.drawString(450,540,f'{Final_bill}')

            pdf.drawString(50,500,f'PAYMENT STATUS: PAID')

            pdf.save()



            print("YOU BILL IS GENERATED")

            break
        else:
            print("PAYMENT FAILED")






