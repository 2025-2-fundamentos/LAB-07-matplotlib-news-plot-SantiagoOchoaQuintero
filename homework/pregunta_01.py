"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('files/input/news.csv', index_col=0)
    colors = {
        'Television': 'dimgrey',  # Gris oscuro
        'Newspaper': 'grey',      # Gris intermedio
        'Radio': 'lightgrey',     # Gris claro
        'Internet': 'tab:blue'    # Azul para destacar
    }

    z_order = {
        'Television': 1,
        'Newspaper': 1,
        'Radio': 1,
        'Internet': 2  # Queda por encima de las demás líneas [00:06:08]
    }

    line_widths = {
        'Television': 2,
        'Newspaper': 2,
        'Radio': 2,
        'Internet': 4  # Línea más gruesa [00:07:17]
    }

    first_year = df.index[0]
    last_year = df.index[-1]

    # 3. Inicializar la Figura y el Título
    plt.figure(figsize=(10, 6))
    plt.title("Fuentes de Noticias Utilizadas (2001-2010)", fontsize=16)

    for col in df.columns:
        plt.plot(
            df.index,
            df[col],
            color=colors[col],
            linewidth=line_widths[col],
            zorder=z_order[col]
        )

    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)

    plt.gca().get_yaxis().set_visible(False)

    for col in df.columns:

        y_start = df.loc[first_year, col]
        y_end = df.loc[last_year, col]

        plt.scatter(first_year, y_start, color=colors[col], zorder=z_order[col])
        plt.scatter(last_year, y_end, color=colors[col], zorder=z_order[col])

        plt.text(
            first_year - 0.2,
            y_start,
            f"{col.capitalize()} {y_start:.1f}%",
            horizontalalignment='right',
            verticalalignment='center',
            color=colors[col],
            fontsize=10
        )

        plt.text(
            last_year + 0.2,
            y_end,
            f"{y_end:.1f}%",
            horizontalalignment='left',
            verticalalignment='center',
            color=colors[col],
            fontsize=10
        )


    plt.xticks(df.index, df.index.astype(str), horizontalalignment='center')


    plt.tight_layout()

    plt.savefig('files/plots/news.png')