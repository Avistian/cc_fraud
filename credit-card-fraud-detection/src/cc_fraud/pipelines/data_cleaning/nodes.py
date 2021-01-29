import pandas as pd

def _remove_prefix(text):
    prefix = "fraud_"
    return text[text.startswith(prefix) and len(prefix):]

def remove_prefix(data: pd.DataFrame) -> pd.DataFrame:
    data["merchant"] = data["merchant"].apply(_remove_prefix)
    return data

def remove_columns(data: pd.DataFrame) -> pd.DataFrame:
    data.drop(data.columns[[0, 1, 6, 7, 9, 10, 16, 17, 18, 19]], axis=1, inplace=True)
    return data