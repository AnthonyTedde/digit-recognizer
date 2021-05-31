import pandas as pd
from sklearn import model_selection


def create_folds():
    df = pd.read_csv("data/train.csv")
    X = df.drop("label", axis=1).values
    y = df["label"].values

    kf = model_selection.KFold(n_splits=5, shuffle=True)

    df["kfold"] = -1
    for fold, (trn, tst) in enumerate(kf.split(X, y)):
        df.loc[tst, "kfold"] = fold

    df.to_feather("data/train_folds.feather")
