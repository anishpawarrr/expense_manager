import streamlit as st
st.set_page_config("EXPMANA")
import streamlit_option_menu as om
import pandas as pd
import home
import enterrec
import data


# st.title("Expense Manager")
pm = 3000
opt = om.option_menu("Expense Manager", ['Home', 'Enter record', 'History'], key="main menu", icons=['🏠','🗃️','📂'], orientation='horizontal', default_index=0)
if opt == 'Home':
    home.hom()
elif opt == 'Enter record':
    enterrec.enrec()
else:
    data.dt()
