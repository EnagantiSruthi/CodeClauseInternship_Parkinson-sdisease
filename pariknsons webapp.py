import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/91939/Downloads/deploy/pariknsons_model.sav','rb'))

#creating a function for prediction

def parkinsons_model(input_data):
    
    # changing input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the numpy array
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)


    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)


    if (prediction[0] == 0):
      return "The Person does not have Parkinsons Disease"

    else:
      return "The Person has Parkinsons"
    
 
      
def main():
    
    #giving a title
    st.title("Parkinson's Disease Prediction")
    
    fo = st.text_input('MDVP:Fo(Hz)')        
    fhi = st.text_input('MDVP:Fhi(Hz)')
    flo = st.text_input('MDVP:Flo(Hz)')
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    RAP = st.text_input('MDVP:RAP')
    PPQ = st.text_input('MDVP:PPQ')
    DDP = st.text_input('Jitter:DDP')
    Shimmer = st.text_input('MDVP:Shimmer')
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    APQ3 = st.text_input('Shimmer:APQ3')
    APQ5 = st.text_input('Shimmer:APQ5')
    APQ = st.text_input('MDVP:APQ')
    DDA = st.text_input('Shimmer:DDA')
    NHR = st.text_input('NHR')
    HNR = st.text_input('HNR')
    RPDE = st.text_input('RPDE')
    DFA = st.text_input('DFA')
    spread1 = st.text_input('spread1')
    spread2 = st.text_input('spread2')
    D2 = st.text_input('D2')
    PPE = st.text_input('PPE')
        
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_diagnosis = parkinsons_model([fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE])                        
                
    st.success(parkinsons_diagnosis)
    
if __name__=='__main__':
    main()

    