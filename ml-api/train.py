import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("D:/student_placement_prediction/dataset/student_placement_dataset.csv")
X = df.drop("placement", axis=1)
y = df["placement"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train,y_train)

pickle.dump(model, open("model.pkl","wb"))

print("Model trained & saved")