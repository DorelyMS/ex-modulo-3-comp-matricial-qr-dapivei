 # Eliminación por bloques (empleando factorización QR)

***
<div align="justify">

## Objetivo del Proyecto

### General

> Implementar el método de eliminación por bloques para resolver sistemas de ecuaciones lineales en lenguaje de programación de python, utilizando como apoyo el método matricial de factorización QR, para resolver los sistemas de ecuaciones que surjan en el método de eliminación por bloques.

### Específicos


>Aprendizaje sobre el uso de github como herramienta colaborativa en la creación y desarrollo de proyectos.

>Aprendizaje en la organización de trabajo en equipo para adopción de frameworks como [scrum](https://www.youtube.com/watch?v=b02ZkndLk1Y&feature=emb_logo) para el desarrollo de proyectos.

## Contenidos de Sitio

- [X] [Project Board](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/projects/1): Contiene información relevante relacionada con la hoja de ruta implementada para programar el método de eliminación por bloques y la factorizacion_QR en Python. En específico, en ella se encuentra: **1) Backlog:**  el detalle de objetivos por etapa (checklist) y milestone; **2) Minutas y acuerdos:** los acuerdos que se derivaron de cada una de las reuniones que se sostuvo con el equipo; **3)** To, In progress, Done: el desarrollo de los diferentes *issues* que se fueron levantandos y su estatus final.


- [X] [Instrucciones](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/instrucciones.md): Instrucciones del profesor, relativas a los objetivos del exámen y los roles de las personas que integran los grupos.

- [X] [Código](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Codigo): Funciones creadas para cumplir con el objetivo del proyecto. Entre los documentos disponibles en este sitio, el más importantes es el módulo que se creó: [moduloEliminacionBloquesQR.py](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/Codigo/moduloEliminacionBloquesQR.py)

- [X] [Pruebas](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Pruebas): Contiene las diferentes pruebas que se realizaron a las funciones propuestas apra verificar que los algoritmos sean precisos y marquen error cuando los datos de entrada no cumplan los requisitos determinados por el algoritmo que se está implementando.


- [X] [Images](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Images): Imágenes que se fueron insertando en este documento o en el [reporteFinal.iypnb](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/reporteFinal.ipynb).


- [X] [Referencias](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/tree/master/Referencias): Bibliografía o páginas consultadas para la elaboración de este proyecto.

- [X] [Reporte final](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/blob/master/reporteFinal.ipynb): Documento dónde se presentan los resultados finales del proyecto. Incluye: Descripción teórica básica de los métodos implementados, explicación breve del algoritmo propuesto, especificación de funciones principales y funciones auxilarias, ejecución de varios ejemplos que se corrieron, tablas y gráficas que muestren el párametro de bloque (subdivisión de la matriz del sistema), tiempos de ejecución para todo el programa o subdividido por secciones, reporte de errores relativos y condición de matrices de los sistemas resueltos y los resultados de sus pruebas. Revisar de forma interactiva aquí: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1hfoEBN0WVZqOKjxOPJt4vOzypP8hoL1-)


## Sobre el Desarrollo del Proyecto


#### Metodología

El equipo que elaboró el presente proyecto se estructuró conforme con el *framework scrum*: un grupo de programación, un grupo de revisión y project manager.

#### Milestones

Para este proyecto se definieron, conforme con la especificación del método asignado, 3 milestones: **1.** [Implementación Factorización QR](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/milestone/1); **2.** [Implementación Método Eliminación por Bloques](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/milestone/2); **3.** [Integración Factorización QR con Método de Eliminación por Bloques](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/milestone/3). A su vez, cada uno de los *milestones* definidos, englobó a varios *issues* relativos al tópico del milestone.

#### Reuniones periódicas

Cada cierto tiempo, el equipo sostuvo reuniones para: verificar el avance de los objetivos y compartir con los integrantes del grupo los obstáculos y hallazgos durante la ejecución de las distintas tareas.

<center>

<table class="tg" style="undefined;table-layout: fixed; width: 1160px">
<colgroup>
<col style="width: 154.166667px">
<col style="width: 1006.166667px">
</colgroup>
  <tr>
    <th class="tg-a0p1">Fecha Reunión</th>
    <th class="tg-a0p1">Acuerdo</th>
  </tr>
  <tr>
    <td class="tg-60hh" rowspan="4"><br><span style="font-weight:bold">4 de abril de 2020</span></td>
    <td class="tg-lsux"><br>- El equipo quedó conformado de la siguiente manera: <span style="font-weight:bold">Grupo de programación:</span> Bruno, Eli, Guillermo. <span style="font-weight:bold">Grupo de Revisión: </span>Leonardo, Laura, Diego. <span style="font-weight:bold">Project Manager: </span>Daniela.<br><br></td>
  </tr>
  <tr>
    <td class="tg-cwfa">- El equipo definió los objetivos y pasos a seguir para implementar el,método de eliminación por bloques con el empleo de la factorización QR.</td>
  </tr>
  <tr>
    <td class="tg-lsux">- El grupo de programación acordó programar e implementar los algoritmos,necesarios para el método de eliminación por bloques con el empleo de,la factorización QR.</td>
  </tr>
  <tr>
    <td class="tg-cwfa">- Próxima reunión: <span style="font-style:italic">12 de abril de 2020.</span></td>
  </tr>
  <tr>
    <td class="tg-wz24" rowspan="3">12 de abril de 2020<br></td>
    <td class="tg-lsux">- El grupo de programación presentó las funciones que implementó y documentó (necesarias para el método de eliminación de bloques con el empleo de la factorización QR).</td>
  </tr>
  <tr>
    <td class="tg-boy4">- El equipo acordó que el grupo de revisión verificaría la precisión, exactitud y documentación del código presentado por el grupo de programadores. Para ello se comprometieron a correr una serie de pruebas,unitarias. Due date: miercóles 15 de abril.</td>
  </tr>
  <tr>
    <td class="tg-v0dp">- Próxima reunión: <span style="font-style:italic">15 de abril de 2020.</span></td>
  </tr>
  <tr>
    <td class="tg-d6wr" rowspan="8">15 de abril de 2020<br></td>
    <td class="tg-cwfa"><br>- El grupo de revisión expuso al grupo los diferentes *issues* que levantaron en relación con: unit testing, estandarización de la documentación, creación de módulos, errores.<br><br><br><br></td>
  </tr>
  <tr>
    <td class="tg-lsux">- El equipo de revisión acordó terminar la revisión del código,propuesto por el equipo de programadores. Due date:jueves 16 de abril de 2020.<br></td>
  </tr>
  <tr>
    <td class="tg-cwfa">- El grupo de programación acordó atender el total de la documentación. Due date: viernes 17 de abril de 2020.<br></td>
  </tr>
  <tr>
    <td class="tg-lsux">- Equipo de revisión acordó terminar la segunda revisión del,código, una vez que el equipo de programación atienda el primer de,bloque de issues que se levantaron. Due date: sábado 18 de abril.</td>
  </tr>
  <tr>
    <td class="tg-cwfa"><br>- Elaboración de,esqueleto del reporte final. Due date: viernes 17 de abril de 2020.<br></td>
  </tr>
  <tr>
    <td class="tg-lsux">- Elaboración de,esqueleto del reporte final. Due date: viernes 17 de abril.</td>
  </tr>
  <tr>
    <td class="tg-cwfa">- Reporte final. Due date: 19 de abril, previo a la reunión programada con Erick.</td>
  </tr>
  <tr>
    <td class="tg-v0dp">- Update del Readme.md. Due date: 19 de abril, previo a la reunión programada con Erick.</td>
  </tr>
</table>

</center>

#### Issues

Para dar orden durante el levantamiento de los *issues*, se definió que la project manager levantaría los *issues* que surgieran por acuerdo común durante las reuniones. Si de esos *issues*, surgía otros *issues* que involucrarían a otros miembros de los grupos, el grupo que lo identificó levantaría los issues respectivos al otro grupo.

Para consultar los issues que se fueron creando a lo largo del proyecto, además poder visulizarlos en el [Project Board](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/projects/1), pueden ser consultados aquí:

> [*Open Issues*](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/issues?q=is%3Aopen+is%3Aissue)

> [*Closed Issues*](https://github.com/mno-2020-gh-classroom/ex-modulo-3-comp-matricial-qr-dapivei/issues?q=is%3Aissue+is%3Aclosed)
## Estatus final

Al momento de revisión del presente trabajo, la totalidad de issues levantados se encuentran cerrados, todos los milestones fueron cumplidos y los objetivos alcanzados satisfactoriamente.

#### Información de Contacto

 - Diego Michell Villa Lizárraga, [dvilla88](https://github.com/dvilla88). Revisor.
 - Leonardo Marín Tellez, [leonardomarintellez](https://github.com/leonardomarintellez). Revisor.
 - Bruno César González Fernández, [brunocgf](https://github.com/brunocgf). Programador.
 - Elizabeth Viveros Vergara, [ElyVV](https://github.com/ElyVV). Programadora.
 - Laura Gómez Bustamente, [lauragmz](https://github.com/lauragmz). Revisora.
 - Guillermo Zarazua Cruz, [gzarazua](https://github.com/gzarazua). Programador.
 - Daniela Pinto Veizaga, [dapivei](https://github.com/dapivei). Project Manager.



</div>

BOTÓN JUPYTERLAB_NUMERICAL_BINDER
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/gzarazua/repo_publico_mno/rama2?urlpath=lab)
