import sys
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

def predict_churn(filename, limiar=0.237, output_filename='saida.csv'):

    # Le o csv de entrada. Esse csv precisa ter a mesma estrutura de entrada (nome das colunas)
    df_teste = pd.read_csv(filename, sep=';')
    rownumber = df_teste['RowNumber'] #guarda RowNumber
    X_teste = df_teste[['CreditScore', 'Geography','Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard','IsActiveMember', 'EstimatedSalary']]

    # Lê o modelo salvo
    with open(r"modelo.pkl", "rb") as input_file:
        best_rf = pickle.load( input_file )

    # Faz a previsão usando o limiar. O default é de 0.237
    y_pred_probas = best_rf.predict_proba(X_teste)[:, 1]
    y_pred_teste = [ 1 if pred >= limiar else 0 for pred in y_pred_probas ]

    # Cria o arquivo com as saídas, o nome default é saida.csv
    output = pd.DataFrame()
    output['rowNumber'] = rownumber
    output['predictedValues'] = y_pred_teste
    output.to_csv(output_filename, index=False)
    print('Criado arquivo com os resultados: ', output_filename)
    

if len(sys.argv) < 2:
    print("Você precisa especificar o arquivo de entrada: predict.py entrada.csv")
elif len(sys.argv) == 2:
    predict_churn(sys.argv[1])

