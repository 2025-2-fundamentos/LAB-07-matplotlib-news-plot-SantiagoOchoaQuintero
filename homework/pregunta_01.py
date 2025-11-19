# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import os
import matplotlib.pyplot as plt
import pandas as pd

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    input_path = 'files/input/news.csv' 
    output_path = 'files/plots/news.png'

    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_csv(input_path, index_col=0)

    colors = {
        'Television': 'dimgrey',
        'Newspaper': 'grey',
        'Radio': 'lightgrey',
        'Internet': 'tab:blue'  
    }
    
    zorders = {
        'Television': 1,
        'Newspaper': 1,
        'Radio': 1,
        'Internet': 2  
    }
    
    linewidths = {
        'Television': 2,
        'Newspaper': 2,
        'Radio': 2,
        'Internet': 4  
    }

    plt.figure(figsize=(10, 6))
    
    for col in df.columns:
        plt.plot(
            df.index, 
            df[col], 
            color=colors[col], 
            label=col, 
            linewidth=linewidths[col],
            zorder=zorders[col]
        )

    plt.title("How people get their news", fontsize=16)
    

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(False) 
    
    plt.gca().axes.get_yaxis().set_visible(False) 

    for col in df.columns:
        first_year = df.index[0]
        last_year = df.index[-1]
        first_val = df.loc[first_year, col]
        last_val = df.loc[last_year, col]
        

        plt.scatter(first_year, first_val, color=colors[col], zorder=zorders[col])
        plt.scatter(last_year, last_val, color=colors[col], zorder=zorders[col])

        plt.text(first_year - 0.2, first_val, f'{col} {first_val}%', ha='right', va='center', color=colors[col])
        plt.text(last_year + 0.2, last_val, f'{last_val}%', ha='left', va='center', color=colors[col])

    plt.tight_layout()

    plt.savefig(output_path)