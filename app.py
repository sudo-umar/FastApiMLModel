import pandas as pd
import xgboost
import numpy as np
import uvicorn
from fastapi import FastAPI
from model import PenguinsFeatureValues

app = FastAPI()

model = xgboost.XGBClassifier()
model.load_model("xgb_class.json")

@app.get('/')
def index():
    """This is home page
    """
    return{'message':'Hello, stranger'}

@app.post('/pred')
def get_name(features:PenguinsFeatureValues):
    data = features.dict()
    # data = [[data['bill_length_mm'], data['bill_depth_mm'],
    #         data['flipper_length_mm'],data['body_mass_g'],data['species_Adelie'],data['species_Chinstrap'],data['species_Gentoo'],
    #         data['island_Biscoe'],data['island_Dream'],data['island_Torgersen']]]
    df = pd.DataFrame(data, index = [0])
    prediction = model.predict(df)[0]
    return{"prediction":f"Label{prediction}"}


    



if __name__ =='__main__':
    uvicorn.run(app)

