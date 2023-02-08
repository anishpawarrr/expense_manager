from main import *
import pandas as pd
from enterrec import getfile

# df = pd.read_csv("dir/file.csv")

@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')



def dt():
    st.subheader("This month's history")
    fn = getfile()
    fn += '.csv'
    df = pd.read_csv(fn)
    st.table(df)
    csv = convert_df(df)
    st.download_button(
        "Press to Download",
        csv,
        "file.csv",
        "text/csv",
        key='download-csv'
    )

