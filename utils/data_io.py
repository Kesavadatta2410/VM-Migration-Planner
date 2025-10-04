import pandas as pd
import json

def read_vms(file_path):
    df = pd.read_csv(file_path) if file_path.endswith('csv') else pd.read_json(file_path)
    # columns: id, cpu, ram, storage
    return [VM(row['id'], row['cpu'], row['ram'], row['storage']) for _, row in df.iterrows()]

def read_hosts(file_path):
    df = pd.read_csv(file_path) if file_path.endswith('csv') else pd.read_json(file_path)
    # columns: id, max_cpu, max_ram, max_storage
    return [Host(row['id'], row['max_cpu'], row['max_ram'], row['max_storage']) for _, row in df.iterrows()]

def read_network(file_path):
    return pd.read_csv(file_path) if file_path.endswith('csv') else pd.read_json(file_path)

def export_plan(plan, file_path):
    if file_path.endswith('csv'):
        pd.DataFrame(plan).to_csv(file_path, index=False)
    else:
        with open(file_path, 'w') as f:
            json.dump(plan, f, indent=2)
