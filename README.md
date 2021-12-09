# _MachineMonitoring
Este projeto é um estudo de aplicação de processos de KDD(Knowledge Discovery in Databases). Onde o objetivo é analisar um dataset e apenas com as informações necessárias aplicar uma RNA supervisionada para predição do comportamento de saúde de um motor.

Referência de informações sobre o dataset : https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset

PASSOS DE PROCESSAMENTO :

1° - DADOS - Onde um dataset é definido como base de dados para obtenção de informações para as proximas etapas.
![image](https://user-images.githubusercontent.com/59672165/145488538-5cecae9f-a729-40ab-86fc-5af099bbef56.png)

2° - DADOS DE INTERESSE - Onde somente as informações pertinente ao que se quer analisar é utilizado para as proximas etapas.
![image](https://user-images.githubusercontent.com/59672165/145488584-1bf50b17-a0ec-4ac6-84d3-60cc7f62d0cc.png)

3° - DADOS PRÉ-PROCESSADOS
Criação de Buffer vazio para recebimento de dados de interesse: 
![image](https://user-images.githubusercontent.com/59672165/145488707-17cc6bee-87fd-4876-b1c6-bfa5451d0530.png)

Historização de dados de interesse no Buffer:
![image](https://user-images.githubusercontent.com/59672165/145488860-65dafcac-d446-45a6-aad4-03ad39b97ea6.png)

4° - FORMATAÇÃO DE DADOS PROCESSADOS
![image](https://user-images.githubusercontent.com/59672165/145489051-b5db2d39-c3b5-45ce-89ed-10ccaaba7b2c.png)

5° - DEFINIÇÃO DE PADRÕES E TREINAMENTO DA RNA
![image](https://user-images.githubusercontent.com/59672165/145489227-3dff6337-754a-4320-b9b4-25c87ca616ca.png)

6° - APLICAÇÃO DO CONHECIMENTO EM PRODUÇÃO
![image](https://user-images.githubusercontent.com/59672165/145489408-da3b143a-611d-402e-a7a9-2b56e869230d.png)
