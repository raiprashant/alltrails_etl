import pandas as pd

def df_to_csv(file_obj1, file_obj2):
    file_obj1 = "users_2017.tsv"
    file_obj2 = "recordings_2017.tsv"
    df = pd.read_csv(file_obj1, sep="\t", header=0)
    df1 = pd.read_csv(file_obj2, sep="\t", header=0)
    df1 = df1[["Recording_ID", "Date_Time", "Pseudo_User_ID", "Activity_Type", "Recording_Summary"]]
    # df1["Recording_Summary"] = range(df1.shape[1])
    # df1["Recording_Summary"] = pd.DataFrame.from_dict(df1["Recording_Summary"] , orient='index')
    # print(df1["Recording_Summary"])

    df1 = df1.sort_values(by='Date_Time')
    df1 = df1.groupby('Pseudo_User_ID').first()

    df2 = pd.merge(df, df1, on='Pseudo_User_ID', how='inner')
    df2["signup_date"] = pd.to_datetime(df2["signup_date"])
    df2['Date_Time'] = pd.to_datetime(df2['Date_Time'])
    df2['dt_diff'] = df2["signup_date"] - df2['Date_Time']
    df2['dt_diff'] = df2['dt_diff']/pd.Timedelta(hours=1)
    # print(df2.count())
    df2 = df2[(df2['dt_diff']) > 0]
    # print(df2.count())
    # print(df2.head())

    return df2.to_csv('final_dataset.csv', index=False)

df_to_csv("users_2017.tsv", "recordings_2017.tsv")
