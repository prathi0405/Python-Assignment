import pandas as pd
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(_name_)

def parse_tsv_file(file_path):
    # Use pandas to read the TSV file and convert the timestamp column to datetime
    df = pd.read_csv(file_path, sep='\t', header=None, names=['timestamp', 'query'])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def filter_queries_by_date(df, date_prefix):
    # Filter the DataFrame based on the date prefix
    filtered_df = df[df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S').str.startswith(date_prefix)]
    return filtered_df['query'].unique()

@app.route('/1/queries/count/<date_prefix>', methods=['GET'])
def get_query_count(date_prefix):
    df = parse_tsv_file('hn_logs.tsv')
    filtered_queries = filter_queries_by_date(df, date_prefix)
    return jsonify({"count": len(filtered_queries)})

if _name_ == '_main_':
    app.run(debug=True)