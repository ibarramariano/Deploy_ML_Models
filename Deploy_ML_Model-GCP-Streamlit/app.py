import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
from sklearn import svm
import streamlit as st

#enconding: utf-8
# Path del modelo preentrenado
MODEL_PATH = 'models/pickle_model.pkl'


# Se recibe la imagen y el modelo, devuelve la prediccion
def model_prediction(x_in, model):
    # SEXO(0,1),
    # DOLOR DE PECHO(0,1,2,3),
    # 7,9,10,11,12,13
    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)

    return preds


def main():
    
    model=''

    # Se carga el modelo
    if model=='':
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
    
    # Titulo
    # html_temp = """
    # <h1 style="color:#181082;text-align:center;">SISTEMA DE PREDICCION PARA ENFERMEDADES CARDIACAS </h1>
    ##</div>
    #"""
    #st.markdown(html_temp,unsafe_allow_html=True)

    st.image('corazon.jpg') 
    st.subheader('SISTEMA DE PREDICCION PARA ENFERMEDADES CARDIACAS')

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores: edad, sexo, dolor de pecho:")
    EDAD = st.text_input("Edad:")
    SEXO = st.selectbox('Sexo (Hombre=1,Mujer=0):',('1', '0')),
    #SEXO = st.text_input("Sexo:")
    DOLOR_DE_PECHO = st.selectbox('Dolor de pecho (Asintomatico=0, Angina Atipica=1, Dolor no anginoso=2, Angina Tipica=3):',('0', '1', '2', '3')),
    PRESION = st.text_input("Presion:")
    COLESTEROL = st.text_input("Colesterol:")
    #GLUCEMIA = st.text_input("Glucemia:")
    GLUCEMIA = st.selectbox('Glucemia de la persona en ayunas: (Menor 120 mg/dl=0, Mayor 120 mg/dl=1):',('0', '1')),
    #ECG_RESULTADO = st.text_input("ECG:")
    ECG_RESULTADO = st.selectbox('Resultados electrocardiograficos en reposo: (Hipertrofia ventricular izq=0, Normal=1, Anormal onda ST=2):',('0', '1', '2')),
    FC = st.text_input("Frecuencia cardiaca:")
    #ANGINA_BOOLEAN = st.text_input("Angina:")
    ANGINA_BOOLEAN = st.selectbox('Angina inducida por el ejercicio: (NO=0, Si=1):',('0', '1')),
    #SEG_ST = st.text_input("Segmento ST:")
    SEG_ST = st.text_input("Depresion del segmento ST:")
    #PEN_ST = st.text_input("Pendiente ST:")
    PEN_ST = st.selectbox('Pendiente maxima del segmento ST en ejercicio: (Pendiente descendente=0, Plano=1, Pendiente ascendente=2):',('0', '1', '2')),
    #VASOS = st.text_input("Vasos:")
    VASOS = st.selectbox('Numero de vasos principales colorados por fluoroscopia: (0, 1, 2, 3):',('0', '1', '2', '3')),
    #TALASEMIA = st.text_input("Talasemia:")
    TALASEMIA = st.selectbox('Talasemia: (Defecto irreversible=0, Flujo normal=1, Defecto reversible=2):',('0', '1', '2')),

    # El boton prediccion se usa para iniciar el procesamiento
    if st.button("Prediccion :"): 
        #x_in = list(np.float_((Datos.title().split('\t'))))
        x_in =[np.int_(EDAD.title()),
                    np.int_(DOLOR_DE_PECHO),
                    np.int_(PRESION.title()),
                    np.int_(COLESTEROL.title()),
                    np.int_(GLUCEMIA),
                    np.int_(ECG_RESULTADO),
                    np.int_(FC.title()),
                    np.float_(SEG_ST),
                    np.int_(PEN_ST),
                    np.int_(VASOS),
                    np.int_(TALASEMIA),
                    np.int_(SEXO),
                    np.int_(ANGINA_BOOLEAN),
                    ]
        predictS = model_prediction(x_in, model)

        if predictS[0]==1:
            #resultado = "enfermo"
            resultado = "enfermo.png"
        else:   
            #resultado = "sano"
            resultado = "sano.jpg"
        
        #st.success('LA PREDICCION SOBRE LA APARICION DE ENFERMEDAD CARDIACA ES: {}'.format(resultado).upper())
        st.image(resultado)

if __name__ == "__main__":
    main()
