import os
import chardet
import pandas as pd
partner_countrys = ['World', 'Uzbekistan', 'Tajikistan', 'Turkmenistan', 'Kazakhstan', 'China', 'Philippines',
                    'Vietnam', 'Laos', 'Cambodia', 'Myanmar', 'Thailand', 'Malaysia', 'Brunei', 'Singapore',
                    'Indonesia', 'East Timor', 'Nepal', 'Bhutan', 'Bangladesh', 'India', 'Pakistan', 'Sri Lanka',
                    'Maldives', 'Belarus', 'Poland', 'Lithuania', 'Estonia', 'Latvia', 'Czech Republi', 'Slovakia',
                    'Hungary', 'Slovenia', 'Croatia', 'Bosnia and Herzegovina', 'Montenegro', 'Serbia', 'Romanian',
                    'Albania', 'Bulgaria', 'North Macedonia', 'Ukraine', 'Moldova', 'Mongolia', 'Russia', 'Iran',
                    'Iraq', 'Turkey', 'Syria', 'Jordan', 'Lebanon', 'Israel', 'Palestine', 'Saudi Arabia', 'Yemen',
                    'Oman', 'U.A.E', 'Qatar', 'Kuwait', 'Bahrain', 'Greece', 'Cyprus', 'Egypt', 'Armenia', 'Georgia',
                    'Azerbaijan', 'Afgahanistan']
path = r"D:\Pythonproject\python1105\data"
year = "new_data"
root = os.path.join(path, year)
result = "result_data"
for dirs in os.listdir(root):
    # 如果是文件夹，且为空文件夹
    if not os.listdir(os.path.join(root, dirs)):
        continue
    res = pd.DataFrame()
    for file in os.listdir(os.path.join(root, dirs)):
        if file.endswith(".csv"):
            with open(os.path.join(root, dirs, file), 'rb') as f:
                result = chardet.detect(f.read())
            data = pd.read_csv(os.path.join(root, dirs, file), encoding=result['encoding'])
            # data = data[['Classification', 'Period', 'Trade Flow', 'Reporter Code', 'Reporter', 'Reporter ISO', 'Partner Code', 'Partner', 'Partner ISO', 'Commodity Code', 'Commodity', 'Trade Value (US$)']]
            data = data[['Period', 'ReporterISO', 'ReporterDesc', 'FlowDesc','PartnerISO', 'PartnerDesc', 'CmdCode', 'CmdDesc', 'PrimaryValue']]
            # data = data[data['Partner'].isin(partner_countrys)]
            data = data[data['PartnerDesc'].isin(partner_countrys)]
            res = res.append(data)
    # res = res.groupby(["Period", "Trade Flow", "Partner"])
    res = res.groupby(["Period", "FlowDesc", "PartnerDesc"])
    # res = res.apply(lambda x: x.sort_values(by=["Period", "Trade Flow","Partner"]))
    res = res.apply(lambda x: x.sort_values(by=["Period", "FlowDesc","PartnerDesc"]))
    res.to_excel('{}-总.xlsx'.format(dirs))


