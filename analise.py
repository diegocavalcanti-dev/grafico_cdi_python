import subprocess
from sys import argv, exit


def extracao():
    # Call the extracao.py script
    subprocess.run(['python', 'extracao.py'], check=True)

def visualizacao(output_image):
    # Call the visualizacao.py script with the output image name
    subprocess.run(['python', 'visualizacao.py', output_image], check=True)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Uso: python analise.py <grafico_analise>")
        exit(1)

    output_image = f"{argv[1]}.png"

    extracao()
    visualizacao(output_image)