import re
import joblib

from TextPreProcessor import TextInputProcessor

with open('./static/spam_model.pkl', 'rb') as f:
    spamModel = joblib.load(f)


print(spamModel)

print(spamModel.predict(["""
FROM INTERNATIONAL MONETARY FUND (IMF)
Address: 700 19th St NW, Washington, DC 20431, USA
Ref Swift: IMFDUS3W2021
FASN: OSB / 629578 / NIG / GFS64G
Working Hours: Open 8am - Closes 5:30 PM
Attn: Beneficiary
We hope this notification arrives meeting your good health and mind. Series of meetings has been held over the past 2 months with the Director Federal Bureau of  Investigation(FBI) this ended 3 days ago.
This is to intimate you of a very important information which will be of a great help to redeem you from all the difficulties you have been experiencing in getting your long overdue payment due to excessive demand for money from you by both corrupt Bank officials and Courier Companies after which your fund remain unpaid to you.
I am Mrs.Kristalina Georgieva, Managing Director (MD) of the International Monetary Fund (IMF). It may interest you to know that reports have reached our office by so many correspondences on the uneasy way which people like you are treated by Various Banks and Courier Companies Diplomat (s) across Europe to Africa and Asia London UK, and we have decided to put a stop to that and that is why I was appointed to handle your transaction here in Washington, DC 20431, USA.
I am delighted to inform you that your forgotten social security deposits, uncashed overtime checks, over-due/contract/Inheritance Lottery winning, Palliative benefits, lost insurance, and tax refunds payment has been approved. All Governmental and Non-Governmental prostates, NGO's, Finance Companies, Banks, Security Companies and Diplomat (s) which have been in contact with you of late have been instructed to back off from your transaction and you have been advised NOT to respond to them anymore since the International Monetary Fund (IMF) Head Office is now directly in charge of your Contract,Lottery ; Inheritance payment  of US $ 15,500,000.00 (fifteen Million five hundred thousand United State Dollars) You are hereby advised to STOP further contact with any institutions immediately with respect to your transaction as your fund will be transferred to you directly from our source. I hope this is clear. Any action contrary to this instruction is at your own risk.
In order for us to proceed you / must get back to us with the information requested below:
Your Full Name:
Your Address:
Your Age:
Your Direct Phone Numbers:
Your Country:
Your Profession:
and we shall give you further details on how your fund will be released to you.
Regards,
Mrs.Kristalina Georgieva
Managing Director (MD)
Communications Department, IMF.
Cc: Gerry Rice, Director,
Chief Economist
Cc: Gita Gopinath
"""]))
