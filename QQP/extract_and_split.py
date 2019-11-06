import pandas as pd
from sklearn.model_selection import train_test_split

questions = pd.read_csv("questions.csv")

questions.head()

question_sample = questions.sample(n=100)

train, test = train_test_split(question_sample, test_size=0.2)

test.to_csv("test.tsv", sep="\t")
train.to_csv("train.tsv", sep="\t")
