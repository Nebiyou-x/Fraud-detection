import pandas as pd

def test_no_missing_values_after_cleaning():
    df = pd.DataFrame({
        "age": [25, None, 40],
        "purchase_value": [100, 200, 150]
    })

    df["age"].fillna(df["age"].median(), inplace=True)

    assert df.isnull().sum().sum() == 0
