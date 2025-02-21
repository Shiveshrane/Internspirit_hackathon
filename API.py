import tensorflow as tf
import numpy as np
import os
import pandas as pd
from flask import Flask, request, jsonify
import joblib
import sklearn
from werkzeug.exceptions import RequestEntityTooLarge
model=tf.keras.models.load_model('model_beta2_1.keras')
preprocessor=joblib.load('preprocessor_beta2.pkl')
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
BATCH_SIZE=128
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data=request.get_json()
        if isinstance(data,dict):
            data=pd.DataFrame([data])
        else:
            data=pd.DataFrame(data)

        preds=[]
        for i in range(0,len(data), BATCH_SIZE):
            X=preprocessor.transform(data.iloc[i:i+BATCH_SIZE])
            pred_probs=model.predict(X)
            pred=(pred_probs>0.632).astype(int)
            preds.extend(zip(pred_probs.tolist(),pred.tolist()))
        return jsonify(preds)
    
    except RequestEntityTooLarge:
        return jsonify({'Error: Request Entity Too Large'}), 413
            

        
    except Exception as e:
        return f'Error: {e}', 500

if __name__ == '__main__': 
    app.run(port=5000, debug=True)


    
