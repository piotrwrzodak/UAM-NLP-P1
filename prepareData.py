import json
import pandas as pd


def delete_offers_without_salary():
    with open('data/data_raw.json', "r", encoding="utf8") as content:
        data = json.load(content)
        filtered_data = [x for x in data if x['employment_types'][0]['salary'] is not None]

        with open('data/filled_salaries.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)


def prepare_data():
    # delete_offers_without_salary()
    df = pd.read_csv('data/formatted_data.csv')

    print(df.columns)






