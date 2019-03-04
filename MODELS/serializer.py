from MODELS import rfclassifier as rfc
from sklearn.metrics import classification_report
import pickle

pickle.dump(rfc.rfc, open("../API/iris_rfc.pkl", "wb"))

pkld_rfclassifier = pickle.load(open("../API/iris_rfc.pkl", "rb"))

# test the serialized model
print(classification_report(rfc.y_test, pkld_rfclassifier.predict(rfc.X_test)))



