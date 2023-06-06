import pickle
import numpy as np

# Load the model from pretrained_model folder
normal_model = pickle.load(open('pretrained_model/Normal.pkl', 'rb'))
enhanced_model = pickle.load(open('pretrained_model/K_centroid.pkl', 'rb'))
# Create a function to predict the efficiency
def predict_normal_efficiency(min_consumption, max_consumption, input_power):
    X = np.array([[min_consumption, max_consumption, input_power]])
    result = normal_model.predict(X)[0]
    result = int(result)
    return result

def predict_enhanced_efficiency(min_consumption, max_consumption, input_power):
    X = np.array([[min_consumption, max_consumption, input_power]])
    result = enhanced_model.predict(X)[0]
    result = int(result)
    return result



# test the model
print(predict_normal_efficiency(0.5, 1.5, 2.5))
print(predict_enhanced_efficiency(0.5, 1.5, 2.5))
