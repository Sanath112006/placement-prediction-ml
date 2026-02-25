import pandas as pd
import numpy as np

np.random.seed(42)

data = {
 "cgpa": np.round(np.random.uniform(5, 9.8, 300), 2),
 "aptitude_score": np.random.randint(40, 100, 300),
 "communication_score": np.random.randint(40, 100, 300),
 "internships": np.random.randint(0, 3, 300),
 "projects": np.random.randint(1, 5, 300),
 "workshops": np.random.randint(0, 3, 300)
}

df = pd.DataFrame(data)

df["placement"] = (
    (df.cgpa > 7).astype(int) +
    (df.aptitude_score > 65).astype(int) +
    (df.communication_score > 60).astype(int) +
    (df.internships > 0).astype(int)
)

df["placement"] = (df["placement"] >= 2).astype(int)

df.to_csv("D:/student_placement_prediction/dataset/student_placement_dataset.csv", index=False)

print("Dataset created successfully ✅")