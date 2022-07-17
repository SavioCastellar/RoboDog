<p align="center">
  <a>
    <img src="https://media.istockphoto.com/vectors/isometric-set-of-techno-robot-dog-vector-id685800642?k=20&m=685800642&s=612x612&w=0&h=bkQRhsBP-vYvqepWaMDS0SaPHR2tKjgjlSk46K7iaM8=" width="306" height="229">
  </a>
</p>

<h3 align="center">RoboDog</h3>

<p align="center">
  This is a personal project for AI studies.
</p>

## Introduction
The goal of the project is to understand how an agent acts in an environment according to it perceptions.<br>
To achieve this objective the RoboDog ```agent``` and the Park ```environment``` were created.<br>
The agent must be able to interact with it perceptions and take actions.<br>
For the purpose of interactions, Food and Water ```things``` were allocated at the Park.<br>
Walk, Eat and Drink are the actions the agent is able to take.<br>
So... The RoboDog walks at the Park, notices the things that are nearby and take actions based in it perceptions.

## Technologies
Project is created with:
* Python: 3.6.0
* Notebook: 4.3.1

<a href="https://github.com/SavioCastellar/RoboDog/blob/main/requirements.txt">Requirements</a>

## Features
```agents.py```<br />
File where the agent, the enviroment and those attributes are defined.

```agents.ipynb```<br />
You can run the program in a Jupyter Notebook from here.

```agents.yaml```<br />
That's the python env.

```AIBO.jpg```<br />
RoboDog image ^.^

```requirements.txt```<br />
The version for all used packages can be seen here.

## Output

``` Ruby
    # RoboDog at position 0
    park.add_thing(dog, 0)
    
    # Food at position 5
    park.add_thing(food, 5)
    
    # Water at position 7
    park.add_thing(water, 7)
    
    # Number of steps
    park.run(10)
```
<br>
For the environment above, that's the output we get:
<a>
  <img src="https://user-images.githubusercontent.com/78110795/179368899-bee8cdec-037f-4c41-8abc-29f9532995b4.PNG"  width="229.5" height="171.25">
</a>
