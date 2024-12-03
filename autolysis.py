import pandas as pd
#Reading CSV Files
def read_csv_file(filename):
    try:
        data = pd.read_csv(filename)
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
      
#Summarizing the Data
def summarize_data(data):
    summary = {
        "columns": list(data.columns),
        "data_types": data.dtypes.to_dict(),
        "missing_values": data.isnull().sum().to_dict(),
        "unique_values": data.nunique().to_dict(),
        "summary_statistics": data.describe(include='all').to_dict()
    }
    return summary

#Performing Statistical Analyses
def correlation_analysis(data):
    try:
        correlations = data.corr()
        return correlations
    except Exception as e:
        print(f"Error in correlation analysis: {e}")
        return None

#Generating Visualizations
import seaborn as sns
import matplotlib.pyplot as plt

def generate_heatmap(data, output_file):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig(output_file)
    plt.close()

# Dynamic Use of LLMs

import os

def get_aiproxy_token():
    token = os.getenv("AIPROXY_TOKEN")
    if not token:
        raise ValueError("AIPROXY_TOKEN is not set!")
    return token

 #Summarize the Dataset
data = read_csv_file("dataset.csv")
if data is not None:
    summary = summarize_data(data)
    print(summary)

#Analyze with Python Functions
if data is not None:
    correlations = correlation_analysis(data)
    if correlations is not None:
        print(correlations)
        generate_heatmap(data, "correlation_heatmap.png")

#Ask the LLM for Insights and Narration
import openai

def ask_llm_for_insights(prompt, token):
    openai.api_key = token
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message["content"]

token = get_aiproxy_token()
prompt = f"Summarize the following dataset insights: {summary}"
insights = ask_llm_for_insights(prompt, token)
print(insights)



