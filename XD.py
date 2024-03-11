import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from cfdToFunction import CdFun



##Definicja danych modelu
T0=308 #temperatura dla h=0 [K]
T=223 #temperatura dla h=10000 [K]
Rp=287.05 #stała gazowa [J/(kg*K)]
Mp=0.0289644 #masa molowa powietrza [kg/mol]
g=9.80 #przyspieszenie ziemskie [m/s^2]
p0=101300 #ciśnienie dla h=0 [Pa]
MR=8.314 #uniwersalna stała gazowa [J/(mol*K)]
d=0.17 #średnica rakiety [m]
ms=35 #sucha masa rakiety [kg]
mp=20 #masa paliwa [kg]
Cx=0.3 #współczynnik oporu aerodynamicznego rakiety
k=1.4 #współczynnik adiabatyczny

df = pd.read_csv('SilnikCSV.csv')


def calculate_optimal_speed(df):
    for v in range(60,550,5):
        df[v] =(df['Siła ciążenia (Fg [N])']*(10000/v)+CdFun(df["Temperatura (T [K])"], v)*v*df['Gęstość powietrza (ρ [kg/m^3])']*math.pi*d**2*10000/8)
    df['min'] = df.iloc[:, 5:].min(axis=1)
    df['idx'] = np.argmin(df.iloc[:, 5:], axis=1) +1
    return df

def get_optimal_speeds(df):
    idxs = df['idx'].to_list()
    vopt=[]
    for i in idxs:
        vopt.append(i*5 + 55)
    vopt.pop()  # For some reason the last value is 0, so we delete it
    return vopt

def get_altitudes():
    h=[]
    for i in range(0,10000,10):
        h.append(i)
    return h

def plot_optimal_speed_vs_altitude(h, vopt):
    plt.plot(h, vopt)
    plt.xlabel('h')
    plt.ylabel('vopt')
    plt.title('Optimal Speed vs Altitude')
    plt.show()

# Function calls
df = calculate_optimal_speed(df)
vopt = get_optimal_speeds(df)
h = get_altitudes()
plot_optimal_speed_vs_altitude(h, vopt)


