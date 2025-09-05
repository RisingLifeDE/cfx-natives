import json
import os

def split_json_namespaces(input_file):
    with open(input_file, 'r') as file:
        data = json.load(file)

    for namespace, content in data.items():
        for key, key_content in content.items():
            game = key_content.get('game')
            if not game:
                game = 'shared'
            apiset = key_content.get('apiset')
            if not apiset:
                apiset = 'undefined'

            output_dir = os.path.join('namespaces', game, apiset, namespace)
            os.makedirs(output_dir, exist_ok=True)

            if 'name' in key_content:
                file_name = f"{key_content['name']}.json"
            else:
                file_name = f"{key}.json"
            output_file = os.path.join(output_dir, file_name)
            with open(output_file, 'w') as outfile:
                json.dump({key: key_content}, outfile, indent=4)
            print(f'Written key {key} of namespace {namespace} to {output_file}')

input_file = 'natives.json'
split_json_namespaces(input_file)