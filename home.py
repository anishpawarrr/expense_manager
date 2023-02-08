import plotly.graph_objects as go
from main import *


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