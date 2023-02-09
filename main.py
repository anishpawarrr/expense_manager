import streamlit as st
import plotly.graph_objects as go
import streamlit_option_menu as om
import pandas as pd
from datetime import date
st.set_page_config("EXPMANA")

def piechart(dicti):
    fig = go.Figure(data=[go.Pie(labels=list(dicti.keys()), values=list(dicti.values()))])
    return fig
def showpiechart(fig):
    st.plotly_chart(fig)

def hom():
    st.subheader("This month's Overview")
    cf = open('curr.csv', 'r')
    pc = cf.readlines()
    ind = pc[0].split(',')
    si = ind[0]
    ri = ind[1]
    con = pc[1].split(',')
    s = con[0]
    r = con[1]
    dict = {si: s, ri: r}
    showpiechart(piechart(dict))



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
                amlist = db['Amount']
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


@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')



def dt():
    st.subheader("This month's history")
    fn = getfile()
    fn += '.csv'
    df = pd.read_csv(fn)
    st.table(df)

    for i in range(1,13,1):
        f = f"{i}.csv"
        csv = pd.read_csv(f)
        csv = convert_df(csv)
        st.download_button(
            f"Press to Download {i}/23 expenses",
            csv,
            "file.csv",
            "text/csv",
            key=f'download-csv{i}'
        )
# st.title("Expense Manager")


pm = 3000
opt = om.option_menu("Expense Manager", ['\nHomee', 'Record', 'History'], key="main menu", icons=['bi bi-house', 'bi bi-box-arrow-in-left', 'bi bi-clock-history'], orientation='horizontal', default_index=0)
if opt == 'Home':
    hom()
elif opt == 'Record':
    enrec()
else:
    dt()
