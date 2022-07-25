
<p align="right">
  <a>
    <img src="https://cdn-icons-png.flaticon.com/512/3909/3909219.png" width="32" height="32">
  </a>
</p>


<p align="center">
  <a>
    <img src="https://media.istockphoto.com/vectors/isometric-set-of-techno-robot-dog-vector-id685800642?k=20&m=685800642&s=612x612&w=0&h=bkQRhsBP-vYvqepWaMDS0SaPHR2tKjgjlSk46K7iaM8=" width="306" height="229">
  </a>
</p>

<h3 align="center">RoboDog</h3>

<p align="center">
  Das ist eine persönliche Projekt um AI zu studieren.
</p>

## Einleitung
Das Ziel in diesem Projekt ist zu vertehen, wie ein Agent in einer Umgebung nach einer Wahrnehmung handelt.<br>
Um dieses Ziel zu erreinchen, wurden der RoboDog ```Agent``` und der Park ```Umgebung``` umgesetzt.<br>
Der Agent muss in der Lage sein und mit den Wahrnehmungen zu interagieren.<br>
Gehen, essen und trinken sind die Taten der Agent kann macht.<br>
So... RoboDog geht durch dem Park, bemerkt Dinge das in der Nähe sind und interagiert.<br>

## Technologien
Das Projekt ist erstellt mit:
* Python: 3.6.0
* Notebook: 4.3.1

<a href="https://github.com/SavioCastellar/RoboDog/blob/main/requirements.txt">Requirements</a>

## Merkmale
```agents.py```<br />
In dieser Datei sind der Agent und die Umgebung umgesetzt.

```agents.ipynb```<br />
Hier können Sie das Programm in Jupyter Notebook ausführen.

```agents.yaml```<br />
Das ist die virtuelle Umgebung.

```AIBO.jpg```<br />
Bild des RoboDog ^.^

```requirements.txt```<br />
Die Version für alle notwendiges Pakete finden Sie hier.

## Output

``` Ruby
    # RoboDog in Stellung 0
    park.add_thing(Hund, 0)
    
    # Esse in Stellung 5
    park.add_thing(Essen, 5)
    
    # Wasser in Stellung 7
    park.add_thing(Wasser, 7)
    
    # Anzahl der Schritte das hat der Hund gemacht
    park.run(10)
```

Für die Umgebung darüber, haben wir dieser Output:

``` Ruby
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>, <Essen>]
    #RoboDog: hat in 5 gegessen.
    [<RoboDog>]
    [<RoboDog>, <Wasser>]
    #RoboDog: hat in 7 getrunken.
    [<RoboDog>]
    [<RoboDog>]
    [<RoboDog>]
```
