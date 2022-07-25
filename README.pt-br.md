<p align="right">
  <a>
    <img src="https://cdn-icons-png.flaticon.com/512/3909/3909370.png" width="32" height="32">
  </a>
</p>


<p align="center">
  <a>
    <img src="https://media.istockphoto.com/vectors/isometric-set-of-techno-robot-dog-vector-id685800642?k=20&m=685800642&s=612x612&w=0&h=bkQRhsBP-vYvqepWaMDS0SaPHR2tKjgjlSk46K7iaM8=" width="306" height="229">
  </a>
</p>

<h3 align="center">RoboDog</h3>

<p align="center">
  Este é um projeto pessoal para o estudo de IA.
</p>

## Introdução
O objetivo do projeto é entender como um agente se comporta em um ambiente de acordo com suas percepções.<br>
Para alcançar esse objetivo, o RoboDog ```agente``` e o Parque ```ambiente``` foram implementados.<br>
O agente deve ser capaz de notar suas percepções e realizar algumas ações.<br>
Para fins de interação, Comida e Água ```coisas``` foram colocadas no Parque.<br>
Andar, Comer e Beber são as ações que o agente é capaz de realizar. <br>
Dessa forma, o RoboDog anda pelo parque, percebe as coisas ao seu redor e realiza ações baseado em suas percepções.<br>

## Tecnologias
O projeto é criiado com:
* Python: 3.6.0
* Notebook: 4.3.1

<a href="https://github.com/SavioCastellar/RoboDog/blob/main/requirements.txt">Requirements</a>

## Recursos
```agents.py```<br />
Arquivo no qual o agente, o ambiente e seus atributos estão definidos.

```agents.ipynb```<br />
O programa pode ser rodado em um Jupyter Notebook por aqui.

```agents.yaml```<br />
Este é o ambiente virtual do python.

```AIBO.jpg```<br />
Imagem utilizada para representar o RoboDog ^.^

```requirements.txt```<br />
As versões para todas as bibliotecas e pacotes utilizados podem ser encontradas aqui.

## Saída
``` Ruby
    # RoboDog está na posição 0
    park.add_thing(dog, 0)
    
    # Comida na posição 5
    park.add_thing(food, 5)
    
    # Água na posição 7
    park.add_thing(water, 7)
    
    # Número de passos que o RoboDog dará
    park.run(10)
```

Para o ambiente acima, recebemos a seguinte saída:

``` Ruby
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>, <Comida>]
    #RoboDog: Comeu na posição 5.
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>, <Agua>]
    #RoboDog: Bebeu na posição 7.
```
