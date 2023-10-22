from flask import Flask, render_template, request
import imagegen
#import invoiceprinter
import payment
import order

app = Flask(__name__)
#model = pickle.load(open('expense_model.pkl','rb')) #read mode
@app.route("/")
def home():
    order={}
    order['price']="N/A"
    #imageurl="Picasso"
    imageurl="""<IMG align="center" src="""+imagegen.genimage("Coffee Shop logo with animal")+"""></IMG>"""
    return render_template('cashierscreen.html',image=imageurl,orderobj=order)

@app.route("/takeorder", methods=['GET','POST'])
def takeorder():
    objorder={}

    if request.method == 'POST':
        # access the data from form view using the request object
        drinktype = str(request.form["drinktype"])
        size = str(request.form["Size"])
        FCNo=str(request.form["FCNo"])

        #Making calls to models

        #Doing an image
        imageurl="""<IMG align="center" src="""+imagegen.genimage("Coffee Shop logo")+"""></IMG>"""

        #Placing Order
        objorder=order.placeorder(drinktype,size,FCNo)

        #If available checking price
        if (objorder['status'] == "Available"):
            objorder['price']=str(order.pricecalc(drinktype,size,FCNo))
        else:
            objorder['price']="Not Avbl"
            print("This order is Not available")

        #checking to see if print button was pressed. if yes then printing invoice
        #pricepressed = request.form.get("PrintReceipt")

        #if ((request.method == 'POST') and (pricepressed is not None)):
        #price = str(request.form["Price"])
        #printmessage=invoiceprinter.print("123456",price)


        #transferring control back to view with some variables
        #return render_template("index.html", prediction_text='Your predicted annual Healthcare Expense is $ {}'.format(output))
        return render_template("paymentscreen.html", image=imageurl, orderobj=objorder)


@app.route("/processpayment", methods=['GET','POST'])
def processpayment():

    #Doing an image
    imageurl="""<IMG align="center" src="""+imagegen.genimage("Coffee Shop logo")+"""></IMG>"""

    paymentcard=str(request.form["PaymentCard"])
    order=str(request.form["OrderID"])
    confirmmsg=payment.processpay(paymentcard,order)
    return render_template("confirmation.html",paymentmsg=confirmmsg,image=imageurl,)

if __name__ == "__main__":
    app.run(debug=True)