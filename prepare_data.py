import json


def delete_offers_without_salary():
    with open('data/data_raw.json', "r", encoding="utf8") as content:
        data = json.load(content)
        filtered_data = [x for x in data if x['employment_types'][0]['salary'] is not None]

        with open('data/filled_salaries.json', 'w', encoding='utf-8') as f:
            json.dump(filtered_data, f, ensure_ascii=False, indent=4)


def prepare_data():
    print('Data preparation')
    # delete_offers_without_salary()
    # next json data was flattened with js scripts from flatten_json.js -> result in formatted.json
    # next I converted json to csv











