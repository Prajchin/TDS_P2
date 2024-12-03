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



