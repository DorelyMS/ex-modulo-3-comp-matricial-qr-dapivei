<div align="center">

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gzarazua/repo_publico_mno/rama2?urlpath=lab)

# Eliminación por bloques (empleando factorización QR)

</div>

***

<div align="justify">

## Índice

- [X] **Objetivos del proyecto**: descripción de los objetivos generales y específicos del proyecto.

- [X] **Contenido del Repositorio**: Distintas carpetas y productos que se fueron desarrollando para cumplir con los objetivos previamente planteadps, así como las herramientas que empleamos para organizarnos como equipo.

- [X] **Sobre el desarrollo del proyectos**: Explicación suscitan de las herramientas que empleamos para organizarnos para el cumplimiento del objetivo del presente proyecto.

- [X] **Conclusiones**: Reflexiones finales sobre el desarrollo del proyecto.

- [X] **Información de contacto**.


**Nota importante:** La totalidad de los documentos y notebooks en este repo pueden ser revisados interactivamente si se utiliza el boton de binder y se clona el repo.

## Objetivo del Proyecto

### General

> Implementar (en python) el método de eliminación por bloques para resolver sistemas de ecuaciones lineales, utilizando como apoyo el método matricial de factorización QR para resolver los sistemas de ecuaciones que surjan en el método de eliminación por bloques.

### Específicos


>Aprendizaje sobre el uso de github como herramienta colaborativa en la creación y desarrollo de proyectos.

>Aprendizaje en la organización de trabajo en equipo para adopción de frameworks como [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) para el desarrollo de proyectos.

## Contenido del Repositorio

- [X] [Project Board](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/projects/1): Contiene información relevante relacionada con la hoja de ruta implementada para programar el método de eliminación por bloques y la factorizacion_QR en Python. En específico, en ella se encuentra: **1) Backlog:**  el detalle de objetivos por etapa (checklist) y milestone; **2) Minutas y acuerdos:** los acuerdos que se derivaron de cada una de las reuniones que se sostuvo con el equipo; **3)** To, In progress, Done: el desarrollo de los diferentes *issues* que se fueron levantandos y su estatus final.


- [X] [Instrucciones](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/instrucciones.md): Instrucciones del profesor, relativas a los objetivos del exámen y los roles de las personas que integran los grupos.

- [X] [Código](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Codigo): Funciones creadas para cumplir con el objetivo del proyecto. Entre los documentos disponibles en este sitio, el más importantes es el módulo que se creó: [moduloEliminacionBloquesQR.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/Codigo/moduloEliminacionBloquesQR.py)

- [X] [Pruebas](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Pruebas): Contiene las diferentes pruebas que se realizaron a las funciones propuestas para verificar que los algoritmos sean precisos y arrojen mensajes de error cuando los datos de entrada no cumplan los requisitos determinados por el algoritmo que se está implementando.


- [X] [Images](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Images): Imágenes que se fueron insertando en este documento o en el [reporteFinal.iypnb](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/reporteFinal.ipynb).


- [X] [Referencias](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Referencias): Bibliografía o páginas consultadas para la elaboración de este proyecto.

- [X] [Reporte final](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/reporteFinal.ipynb): Documento dónde se presentan los resultados finales del proyecto. Incluye: Descripción teórica básica de los métodos implementados, explicación breve del algoritmo propuesto, especificación de funciones principales y funciones auxilarias, ejecución de varios ejemplos que se corrieron, tablas y gráficas que muestren el párametro de bloque (subdivisión de la matriz del sistema), tiempos de ejecución para todo el programa o subdividido por secciones, reporte de errores relativos y condición de matrices de los sistemas resueltos y los resultados de sus pruebas. 


## Sobre el Desarrollo del Proyecto


#### *Framework*

El equipo que elaboró el presente proyecto se estructuró conforme con el *framework scrum*: un grupo de programación, un grupo de revisión y project manager.


<p align="center">
  <img width="460" height="300" src="https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/Images/scrumprocess.png">
 
 **Fuente**: [What is scrum? An overview of the Agile Framework](https://www.youtube.com/watch?v=Ifc2Z4nXMvE)

</p>


Para la coordinación del equipo, se sostuvo una reunión dónde se planificó y elaboró la lista de tareass necesarias para desarrollar los requisitos seleccionados del proyecto. Cada ciertos días, se realizaron reuniones de sincronización para revisar: 1) el estatus del [*scrum taskboard*](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/projects/1); 2) el trabajo de los integrantes del equipo(dependencias entre tareas, progreso hacia el objetivos finales y obstáculos que surgieron.

#### Milestones

Para este proyecto se definieron, conforme con la especificación del método asignado, 3 milestones: **1.** [Implementación Factorización QR](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/milestone/1); **2.** [Implementación Método Eliminación por Bloques](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/milestone/2); **3.** [Integración Factorización QR con Método de Eliminación por Bloques](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/milestone/3). A su vez, cada uno de los *milestones* definidos, englobó a varios *issues* relativos al tópico del milestone.


#### Issues

##### Organización de levantamiento de Issues

Para dar orden durante el levantamiento de los *issues*, se definió que la project manager levantaría los *issues* que surgieran por acuerdo común durante las reuniones. Si de esos *issues*, surgía otros *issues* que involucrarían a otros miembros de los grupos, el grupo que lo identificó levantaría los issues respectivos al otro grupo.


##### Sobre los Issues

En total se levantaron `25` issues, de los cuáles la mayoría de los issues fueron acordados durante las diferentes reuniones que se sostuvieron con el equipo. Los issues fueron del siguiente tipo:


> Instrucciones relativas a la programación del método que se nos fue asignado: eliminación por bloques con el apoyo del método matricial de factorización QR. Para ellos, tpdos los issues se englobaron dentro de los tres milestones que previamente habíamos definido.

> Tasks relativos a la revisión del método implementado por los programadores, mediante los cuáles se solicitaba a los revisores revisar la precisión y documentación adecuada de las funciones. Así como la ejecución de pruebas específicas que probaran: la precisión Factorización QR y que el método de eliminación por bloques con QR funcione adecuadamente considerando los siguientes casos:
> + Sistemas de ecuaciones con soluciones infinitas: los métodos implementados arrojen comentarios indicando que la condición no fue cumplida (que la matriz sea singular) y por tanto que las funciones no sean completadas. Verificación con las librerías disponibles en python, como ser `np.linalg.solve(A,b)`.


> + Sistemas de ecuaciones únicas: que la función eliminacion_bloques(A,b) es capaz de resolver efectivamente sistemas de ecuaciones con solución única y que sus resultados sean consistentes con los resultados que arroja la librería `np.linalg.solve(A,b)` de python.

>+ Sistemas ecuaciones sin solución: los métodos implementados arrojen comentarios indicando que la condición no fue cumplida (que la matriz sea singular) y por tanto que las funciones no sean completadas. Verificación con las librerías disponibles en python, como ser `np.linalg.solve(A,b)`.


> En respuesta a estos *task*, los revisores levantaron *issues* relativos a los siguientes temas:

> + Solicitudes de revisión y homogeneización de los nombres de las funciones y los parámetros empleados, de manera que estos sean informativos para el usuario. , de manera que éste de al usuario una idea general de lo que la realiza la función. Asímismo, se solicitó la mejor descripción de los distintos bloques del código.

> + Creación de un achivo con extensión .py que incluya todas las funciones utilizadas para Solución de sistemas de Ecuaciones Lineales a través del algoritmo de Eliminación por Bloques.
> + Homogeneización de la documentación en formato `Google Docstrings`.
> + Inclusión de una validación sobre las dimensiones de la matriz de entrada. En caso de no cumplirse la condición m>=n, entonces desplegar el siguiente mensaje: `Las dimensiones de la matriz (A) no son válidas`.

> Una vez que los programadores resolvieron los issues que levantaron los revisores. Se asignó finalmente el siguiente set de issues a los integrantes del equipo:

> + A los revisores: Una segunda y última revisión de las modificaciones que realizaron los programadores y del correcto funcionamiento de las funciones en general. Sus *outputs* fueron resguardados en la carpeta de pruebas.

> + A los programadores, la revisión de los últimos detalles que deben ser incluidos en el reporte final: i ) tablas y gráficas que muestren el parámetro del bloque; ii) tiempos de ejecución para todo el programa y subdividido por secciones; iii) cálculo de errores relativos (condición de la matriz); iv) características de máquinas que usamos.


> + A todos, la inclusión de las referencias que se emplearon para la elaboración del proyecto, sean estos libros consultados, papers, referencias en internet, entre otros.


Para consultar los issues que se fueron creando a lo largo del proyecto, además poder visualizarlos en el [Project Board](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/projects/1), pueden ser consultados aquí:
> [*Closed Issues*](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/issues?q=is%3Aissue+is%3Aclosed)


##### Estatus finales

Al momento de revisión del presente trabajo, la totalidad de issues levantados se encuentran cerrados, todos los milestones fueron cumplidos y los objetivos alcanzados satisfactoriamente.


## Conclusiones


#### En términos del empleo de las herramientas de Github y del *framework scrum*

Para el desarrolo del presente trabajo, el empleo de herramientas disponibles en internet como ser Github (para el resguardo de la información que fuimos generando a lo largo del proyecto) y de Git, en específico, para el  Git el control de las distintas versiones de los documentos que fuimos desarrollando fue fundamental. El uso de estas herramientas nos permitió contar con una *bitácora* de los cambios que fuimos realizando durante la elaboración de los distintos productos del proyecto.

Además, gracias al presente proyecto, descubrimos otra faceta de Github: la posibilidad de organización de proyectos por este medio, através del levantamiento de *issues*, creación de *milestones* y *project boards*. Todas estas herramientas, incluidas dentro de Github, nos ayudaron en distintos aspectos: delegación de tareas, seguimiento a las tareas, visualización y calendarización de los temas pendientes y orientación constante hacia nuestro objetivo final: cumplimiento de los objetivos del proyecto. Estas herramientas, junto con el empleo del *framework* scrum, facilito nuestro trabajo final.

#### En términos de la implementación del algoritmo *eliminación por bloques*, utilizando como apoyo el método matricial de factorización QR


#### Retos



#### Información de Contacto

 - Diego Michell Villa Lizárraga, [dvilla88](https://github.com/dvilla88). Revisor.
 - Leonardo Marín Tellez, [leonardomarintellez](https://github.com/leonardomarintellez). Revisor.
 - Bruno César González Fernández, [brunocgf](https://github.com/brunocgf). Programador.
 - Elizabeth Viveros Vergara, [ElyVV](https://github.com/ElyVV). Programadora.
 - Laura Gómez Bustamente, [lauragmz](https://github.com/lauragmz). Revisora.
 - Guillermo Zarazua Cruz, [gzarazua](https://github.com/gzarazua). Programador.
 - Daniela Pinto Veizaga, [dapivei](https://github.com/dapivei). Project Manager.



</div>
