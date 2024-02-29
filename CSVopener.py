import csv
import math

def open_csv_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for i in range(0, len(row)):
                    print(row[i])

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", e)

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

f0=g*(ms+mp*(1-((0)/10000)))
ρ0=row=(p0*math.exp(-g*Mp*(((0)*10)/MR/(T0-(T0-T)*(((0)*10)/(10000))))))/(Rp*(T0-(T0-T)*(((0)*10)/(10000))))

def save_to_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("Data has been successfully saved to CSV file.")
    except Exception as e:
        print("An error occurred:", e)

file_path = r'C:\Users\siwirus\PycharmProject\WykresyDoSilników\SilnikCSV.csv'

#Nazwy kolumn
data_to_save = [["Wysokość (h [m])","Siła ciążenia (Fg [N])", "Temperatura (T [K])", "Ciśnienie (p [Pa])", "Gęstość powietrza (ρ [kg/m^3])"],
                [0,f0,T0,p0,ρ0]]

# Wysokość (h [m])
for i in range(1,1001):
    row=[i*10]
    data_to_save.append(row)

# Siła ciążenia (Fg [N])
for i in range(2,1001):
    row=[g*(ms+mp*(1-(((i-1)*10)/10000)))]
    data_to_save[i].append(row[0])


# Temperatura (T [K])
for i in range(2,1001):
    row=[T0-(T0-T)*(((i-1)*10)/(10000))]
    data_to_save[i].append(row[0])

# Ciśnienie (p [Pa])
for i in range(2,1001):
    row=[p0*math.exp(-g*Mp*(((i-1)*10)/MR/(T0-(T0-T)*(((i-1)*10)/(10000)))))]
    data_to_save[i].append(row[0])

# Gęstość powietrza (ρ [kg/m^3])
for i in range(2,1001):
    row=[(p0*math.exp(-g*Mp*(((i-1)*10)/MR/(T0-(T0-T)*(((i-1)*10)/(10000))))))/(Rp*(T0-(T0-T)*(((i-1)*10)/(10000))))]
    data_to_save[i].append(row[0])

save_to_csv(file_path, data_to_save)

file_path = r'C:\Users\siwirus\PycharmProject\WykresyDoSilników\SilnikCSV.csv'
open_csv_file(file_path)
