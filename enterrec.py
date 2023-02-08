from datetime import date
from main import *

b = False
def getfile():
    td = date.today()
    mon = td.month
    return str(mon)

def enrec():
    with st.form("Enter details"):
        st.subheader("Enter Details")
        reason = st.text_input("Reason")
        amount = st.number_input("Amount")
        rdate = st.date_input("Date")
        button = st.form_submit_button("Enter")
        if button:
            with st.spinner("Wait a sec"):
                fn = getfile()
                fn += ".csv"
                f = open(fn, 'a+')
                s = f"{rdate},{amount},{reason}\n"
                f.write(s)
                f.close()
                db = pd.read_csv(fn, index_col=False)
                # st.table(db)
                amlist = db['amount']
                # st.table(amlist)
                amlist = list(map(float, amlist))
                totam = sum(amlist)
                cf = open("curr.csv", 'r+')
                cl = cf.readlines()
                index = cl[0]
                s = totam
                r = 3000 - totam
                stri = f"{s},{r}"
                cf.close()
                cf = open("curr.csv", 'w')
                cf.writelines([index, stri])
                cf.close()
                b = True

enrec()
if b:
    st.write("Expense stored successfully!")
