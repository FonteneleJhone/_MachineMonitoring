"""
Created on Sat Dec 04 2021 - @author: Jhone Fontenele
"""
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier
import pandas as pd
import timeit
import time


data_frame = pd.read_csv('pdm.csv')

df = data_frame[['UDI', 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Machine failure']]
print("\n --INÍCIO-------------------------LEITURA DO DATASET COMPLETO------------------------------")
print(df)
print(" --FIM-------------------------LEITURA DO DATASET COMPLETO------------------------------")
time.sleep(2)
print("\n --INÍCIO-------------------------ARRAY BUFFER PARA DATASET FILTRADO------------------------------")
t = np.zeros((len(df), 6), 'int')
print(t)
print("\n --INÍCIO-------------------------ARMAZENAMENTO DO DATASET FILTRADO NO ARRAY BUFFER------------------------------")
for j in range(len(df)):
    for i in range(6):
        if (i == 1) or (i == 2):
            t[j,i] = float(df.iloc[j,i])-273.15
        else:
           t[j, i] = float(df.iloc[j, i])
print(t)
print(" --FIM-------------------------ARMAZENAMENTO DO DATASET FILTRADO NO ARRAY BUFFER------------------------------")
time.sleep(2)
#Separa as colunas do conjunto de treinamento em sintomas (p) e diagnóstico (d)
#p = df.iloc[0:len(df), 0:5]
#d = df.iloc[0:len(df), 5:6]
p = t[:, 1:5]
d = t[:, 5]
X_train = p
y_train = d
X_test = p
y_test = d
print("\n --INÍCIO-------------------------SEPARAÇÃO DE DADOS DE ENTRADA DA MLP------------------------------")
print("\n ---------------------------ENTRADAS - PARA ANÁLISE DA REDE NEURAL------------------------------")
print(p)
print("\n ---------------------------SAÍDAS - RESULTADOS SUPERVISIONADOS------------------------------")
print(d)
print(" --FIM-------------------------SEPARAÇÃO DE DADOS DE ENTRADA DA MLP------------------------------")
time.sleep(2)
#Cria a RNA do tipo Multi-layer Perceptron com a configuração indicada
clf = MLPClassifier(hidden_layer_sizes=(5,), learning_rate='constant',learning_rate_init=0.001, max_iter=3000)
#Treina a RNA
clf.fit(X_train, y_train)
#Calcula e imprime a acurácia do treinamento
acuracia_trein = clf.score(X_test, y_test)
print("\n Acurácia do Treinamento = %.2f%%" % (acuracia_trein*100.0))
#Função de Ativação
def funcaoAtivacao(valor):
    #A função de ativação a degrau 
    if valor < 1:
        return(0)
    else:
        return(1)
valor_predicao_usuario = np.zeros(4)
continuar = "sim"
while continuar == "sim":
    print("\n --INÍCIO-------------------------APLICAÇÃO EM PRODUÇÃO COM RNA MLP TREINADA------------------------------")
    input_temp_ar = input("Insira o valor para Temperatura do Ar: ")
    input_temp_ar_i = float(input_temp_ar)
    input_temp_pro = input("Insira o valor para Temperatura do Processo: ")
    input_temp_pro_i = float(input_temp_pro)
    input_vel_mot = input("Insira o valor para Velocidade do Motor: ")
    input_vel_mot_i = float(input_vel_mot)
    input_tor_mot = input("Insira o valor para Torque do Motor: ")
    input_tor_mot_i = float(input_tor_mot)
    valor_predicao_usuario = [input_temp_ar_i, input_temp_pro_i, input_vel_mot_i,input_tor_mot_i]

    print(valor_predicao_usuario)
    resp = clf.predict([valor_predicao_usuario])

    print("\nPredição da RNA MLP para Novo Caso: ")
    f_transferencia = funcaoAtivacao(resp)
    if f_transferencia < 1:
        print("\n ----O Motor não possui Falha !!!----\n")
    else:
        print("\n ----O Motor possui Falha !!!---- \n")
    print("--FIM---------------------------APLICAÇÃO EM PRODUÇÃO COM RNA MLP TREINADA------------------------------")
    time.sleep(2)
    continuar = input("\n Digite sim para continuar e não para Finalizar!: ")
