Vianna_CircuitsolverProjeto: Programa para solucionar circuitos do tipo laços
Por matrizes e método de cramer.

Motivação: Agilidade na resolução desse tipo de circuito para o cotidiano de um projetista ou técnico.

Programa final: resolver um circuito de 5 ou menos laços ( pois no mundo real, podemos dividir os circuitos desejados em etapas e assim 5 é um ótimo número para laços de um circuito analisado, isto é, dificilmente um circuito simples terá mais de 5 laços)

Diagrama de classe do projeto antes de iniciar a execução.
![Screenshot](digclasses.png)

OBS: no diagrama de classes acima temos a ideia inicial do projeto, no entanto quando executei o projeto houve a nescessidade de mudar o diagrama de classes. Sendo assim, as classes se transformaram em objetos e a unica classe é a principal a qual chama os elementos do pyQT.

Fluxograma do algoritmo do programa.
![Screenshot](fluxograma.png)

Foi utilizado o seguinte tutorial:  http://pythonforengineers.com/your-first-gui-app-with-python-and-pyqt/

Assim escolhida a interface gráfica do projeto como pyQT, construimos um simples taxador de juros, impostos ou etc. o usuário entra com o valor inicial, com a porcentagem de taxa e recebe o valor final com taxa.

![Screenshot](tutorial.png)



O programa final tem a seguinte interface gráfica:

![Screenshot](interface.png)

Para utilizar o programa deve-se escolher um circuito de 5 laços com o formato dessa figura
![Screenshot](circuito.jpg)
onde tenha-se o valor das fontes de tensão e resistências. O programa devolverá a corrente em cada laço separado por ponto e virgula, como mostra o video do programa funcionando.
A FUNCIONALIDADE SERIE E PARALELO ESTÁ EM VERSÃO BETA DE DESENVOLVIMENTO, PORTANTO NÃO ESTÁ FUNCIONANDO.

Para compilar o programa, deve colocar o codigo temp.py e cicuitsolver.ui na mesma pasta e compilar os mesmo com seu compilador python. Observe se a versão do python QT e do Python instalada em seu computador é condizente com a do código.

VIDEO DO PROGRAMA FUNCIONANDO 
https://drive.google.com/file/d/1x3WHWjAxq7UFjYAZTbpM-uDJlIDd9tYd/view?usp=sharing
