import pickle
import numpy as np

# Load the model
normal_model = pickle.load(open('normal_prediction.pkl', 'rb'))
enhanced_model = pickle.load(open('Enhanced.pkl', 'rb'))

# Create a function to predict the efficiency
def predict_normal_efficiency(min_consumption, max_consumption):
    X = np.array([[min_consumption, max_consumption]])
    result = normal_model.predict(X)[0]
    result = int(result)
    return result

def predict_enhanced_efficiency(min_consumption, max_consumption):
    X = np.array([[min_consumption, max_consumption]])
    result = enhanced_model.predict(X)[0]
    result = int(result)
    return result



# test the model
print(predict_normal_efficiency(0.5, 1.5))
print(predict_enhanced_efficiency(0.5, 1.5))
