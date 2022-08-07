import pandas as pd
from wqchartpy import gibbs,triangle_piper,rectangle_piper,color_piper,durvo,hfed,chadha,schoeller

# Load the template data
def graph():
    url = 'https://raw.githubusercontent.com/jyangfsu/WQChartPy/main/data/data_template.csv'
    df = pd.read_csv(url)
    #commemt


    gibbs.plot(df, unit='mg/L', figname='Gibbs diagram', figformat='jpg')


    triangle_piper.plot(df, unit='mg/L', figname='triangle Piper diagram', figformat='jpg')

    rectangle_piper.plot(df, unit='mg/L', figname='rectangle Piper diagram', figformat='jpg')

    rgb = color_piper.plot(df, unit='mg/L', figname='color-coded Piper diagram', figformat='jpg')

    durvo.plot(df, unit='mg/L', figname='Durvo diagram', figformat='jpg')

    hfed.plot(df, unit='mg/L', figname='HFE-D diagram', figformat='jpg')

    chadha.plot(df, unit='mg/L', figname='Chadha diagram', figformat='jpg')

    schoeller.plot(df, unit='mg/L', figname='Schoeller diagram', figformat='jpg')
