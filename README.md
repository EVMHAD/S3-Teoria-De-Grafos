# S3F-TeoriaDeGrafos

**Códigos ejemplo para el taller de teoría de grafos con Python &amp;
NetworkX**

La instalación de librerías en Python se hace con `pip`; averigua cómo
se hace eso en tu sistema para no batallar durante la sesión. En sus
demos, Elisa usa `emacs` en `linux`, pero si estás en Windows, con
haber instalado IDLE, vas a sobrevivir, con que hayas practicado el
uso de `pip` de antemano.

## Primera sesión

Vamos a platicar en pizarrón sobre los conceptos básicos de teoría de
grafos y luego familiarizarnos con cómo representar todo eso en Python
usando
[NetworkX](https://networkx.org/documentation/stable/tutorial.html)
viendo el tutorial y explorando las opciones que la librería ofrece
para la generación, visualización y análisis de grafos. Un código
ejemplo para iniciar la exploración está en
[`primera.py`](https://github.com/EVMHAD/S3-Teoria-De-Grafos/blob/main/primera.py)
y ocupa, además de _NetworkX_, una instalación de
[matplotlib](https://matplotlib.org/stable/tutorials/index.html).
Otra librería que se usa en las demos es `celluloid` que facilitar la
creación de animaciones (este
[tutorial](https://towardsdatascience.com/animations-with-matplotlib-d96375c5442c)
explica su uso); se puede usar como _back-end_ con la opción
`writer='imagemagick'` la maravillosa herramienta
[ImageMagick](https://imagemagick.org/index.php) que se instala
aparte.

## Segunda sesión

No necesitamos nuevos paquetes; estaremos analizando propiedades
estructurales en NetworkX y actualizando las visualizaciones acorde.

## Tercera sesión

Se
necesita
[el estilo `tikz-network`](https://github.com/hackl/tikz-network) para
LaTeX.
