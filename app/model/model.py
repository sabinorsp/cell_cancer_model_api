from pathlib import Path
import joblib
import json
from sklearn.preprocessing import MinMaxScaler

__version__ = 'model_beta_xgb'

BASE_DIR = Path(__file__).resolve(strict=True).parent

scaler = joblib.load(f'{BASE_DIR}/scaler_transform.pkl')
model = joblib.load(f'{BASE_DIR}/{__version__}.pkl')


def predict(data):
    prev = model.predict(scaler.transform(data))[0]
    if prev == 0:
        return 'Benigna'
    return 'Maligna'


def sample_default():
    with open(f'{BASE_DIR}/sample_default.json') as f:
        sample_default = json.load(f)
    return sample_default[0]