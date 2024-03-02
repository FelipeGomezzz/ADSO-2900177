# Comandos - Git
![](https://johngodlee.github.io/geotaster_git_workshop/img/geotaster_git_banner.png)

## Listar nuestras configuraciones globales de Git

git config -l


## Ver como funciona un comando

git <comando> --help


## Configurar nuestro nombre para mostrar en Git

git config --global user.name "Elvis"


## Configurar el correo de nuestro usuario en Git

git config --global user.email "elvis@micorreo.com"


## Inicializar el repositorio

git init


## Consultar el estado de nuestro repositorio local

git status 


## Agregar cambios al area de staging para que Git detecte los cambios

git add <NombreArchivo.extension>

*Staging Area son los cambios que git detecta y los mantiene en memoria RAM, es decir, se borran si no haces commit*
> Si queremos agregar todos los archivos del directorio actual escribimos  git add .  en lugar del nombre del archivo

## Guardar cambios del staging en el repositorio local

git commit -m 'Tu mensaje aqui'

> Si no escribes un mensaje te saltara un editor llamado Vim pidiendote que agregues el mensaje, para ello precionas Q y luego la tecla I y escribes tu mensaje. Finalmente para salir del editor presionas ESC + SHIFT + Z + Z

## Ver historial de commits

git log


Una forma un poco mas bonita de verlo es:

git log --all --graph --decorate --oneline

En uno de los commits listados veremos la palabra HEAD tal cual en mayusculas. Eso nos quiere decir que ese commit es nuestra version actual en el repositorio.
*Muestra cada commit con un id que podemos utilizar para poder volver hacia atras los cambios*
> Cuando la lista es muy larga nos desplazamos con las flechas ARRIBA y ABAJO del teclado. Y para salir presionamos la tecla Q.


## Ver historia del repositorio en software

gitk

> Con este comando se nos abrira el software nos muestra las ramas, tags, historia, etc.

## Alias en Git
Una forma de usar comandos largos con un nombre mas corto

alias <nombre-alias>="Comando aqui"

> Luego de crearlo simplemente escribimos el nombre del alias para ejecutar nuestro comando.

## Git Commit + Git Add
Para hacer git commit -m 'Tu mensaje aqui' y git add en una sola linea usamos

git commit -am 'Tu mensaje aqui'

> Solo funciona si anteriormente los archivos ya han sido añadidos una vez con git add <nombre-archivo.extension> o git add .

## .GitIgnore
El archivo llamado .gitignore nos sirve para ignorar archivos y directorios que no es necesario enviar a nuestro repositorio
> Para crearlo solamente creamos un nuevo archivo con el nombre .gitignore

## Ignorar archivos en especifico
Abrimos el archivo .ignore y agregamos en una linea <nombre.extension> del archivo. Ejemplo:

miarchivo.txt

> Solo debemos especificar un archivo por linea dentro de .gitignore

## Ignorar archivos por extension
Abrimos el archivo .ignore y agregamos en una linea <*.extension> del archivo. Ejemplo:

*.txt

Como puedes notar usamos * para decirle a git "TODOS" y la extension de los archivos que tendran en comun para ser ignorados. En este caso ignoramos todos los .txt
> Solo debemos especificar un archivo por linea dentro de .gitignore

## Ignorar directorios (carpetas)
Abrimos el archivo .ignore y agregamos en una linea <nombre_carpeta>/ del archivo. Ejemplo:

micarpeta/

Como puedes notar usamos / al final para decirle a git "esto es una carpeta". En este caso ignoramos todos los los archivos de la carpeta.
> Solo debemos especificar un directorio por linea dentro de .gitignore

## Crear una nueva rama

git branch <nombre-de-la-nueva-rama>


## Crear y cambiar a la vez a una nueva rama

git checkout -b <nombre-de-la-nueva-rama>

> Con este comando estamos creando una nueva rama y a la vez nos desplazamos hacia ella.

## Ver ramas creadas y su historia

git show-branch

Tambien podemos ver las ramas con su historia pero de forma mas detallada asi:

git show-branch --all


## Eliminar una rama

git branch -d <nombre-de-la-nueva-rama>


## Cambiar a otra rama (por defecto estamos en Master)


git checkout <nombre-de-la-nueva-rama>


## Fusionar ramas (Traer cambios de una rama a la rama actual)

git merge <nombre-rama>


## Restaurar una version antigua de un archivo

git checkout <id-del-commit> <nombre-de-archivo.extension>

*Si no especificamos el nombre del archivo cambiara todos los archivos que esten registrados en el commit seleccionado*

## Restaurar el ultimo commit

git checkout HEAD <nombre-de-archivo.extension>

*Si no especificamos el nombre del archivo todos los archivos se restauraran a los cambios hechos en el ultimo commit*

## Comparar diferencias entre commits

git diff <id-commit> <id-otro-commit>


## Comparar diferencias entre nuestros cambios actuales y el ultimo commit

git diff master <nombre-archivo.extension>


## Comparar cambios entre nuestros cambios actuales y el penultimo commit

git diff master^ <nombre-archivo.extension>

> Con ^ le decimos a git que pase al anterior de la ultima version, es decir, podriamos usar ^^ para ver la version anterior a la penultima.

## Comparar cambios del mismo archivo entre ramas

git diff <nombre-otra-rama> <nombre-archivo.extension>

## Clonar repositorio remoto

git clone <URL>

> Esto nos traera una copia completa desde el repositorio remoto y lo guardara en la carpeta donde estemos ubicados en la consola actualmente

## Agregar repositorio remoto

git remote add origin <URL del repositorio>

## Traer cambios de repositorio remoto a repositorio local

git fetch origin

> origin es la el repositorio remoto que agregamos y podemos agregar master o nombre de la rama de nuestro repositorio remoto que queremos traer hacia nuestro repositorio local. Sin embargo, estos cambios no se veran reflejados en nuestro directorio de trabajo hasta que usemos git merge

## Traer cambios de repositorio local hacia nuestro directorio de trabajo

git merge master

> Podemos reemplazar master por la rama que queremos traer a nuestro directorio de trabajo

## Resolver conflictos al hacer merge
Si al hacer git merge <nombre-rama> nos encontramos con el conflicto de que dos o mas desarrolladores cambiaron la misma linea de diferente forma, si utilizamos VS Code nos preguntara si deseamos mantener nuestros cambios o los que vienen en el merge. Luego de seleccionar uno de estos debemos hacer git add y git commit nuevamente para guardar los cambios.
> Es recomendable hacer una llamada a tu equipo de trabajo para ponerse de acuerdo con el cambio que elijan.

## Git Fetch + Git Merge = Git Pull
Con este comando podemos traer los cambios de nuestro repositorio local hacia nuestro repositorio local y hacia nuestro directorio de trabajo a la vez

git pull origin master

> origin es la el repositorio remoto que agregamos y podemos agregar master o nombre de la rama de nuestro repositorio remoto que queremos traer hacia nuestro repositorio local y directorio de trabajo. Sin embargo antes debimos agregar el origen remoto y master puede ser reemplazado por el nombre de otra rama.

## Enviar cambios de nuestro repositorio al repositorio remoto

git push -u origin master

> origin es la el repositorio remoto que agregamos y master la rama de nuestro repositorio local que le enviamos

# Configura tus llaves SSH en local

## Crear llaves

ssh-keygen -t rsa -b 4096 -C "elvis@micorreo.com"

> -b 4096 nos dice la complejidad de las llaves y -C "elvis@micorreo.com" el correo de quien sera el dueño de las llaves vinculado a GitHub

## Comprobar si SSH esta funcionando 

eval $(ssh-agent -s)

> Si nos aparece algo parecido a Agent pid 123 esta funcionando.

## Agregando llave privada a nuestro sistema

ssh-add ~/.ssh/id_rsa

> ~ indica que queremos ubicarnos en HOME/ de nuestro usuario o donde este ubicada nuestra llave privada. Recuerda no compartirla ni mostrarla.


# Tags y Versiones en Git & GitHub

## Agregar un Tag
Los Tags nos sirven para almacenar o destacar un commit como si se tratase como una version de lanzamiento distinta en GitHub

git tag -a <nombre-tag> -m "Tu mensaje" <hash-aqui>

> El hash es el ID de los commit al que hacemos referencia

## Ver nuestros Tags

git tag

> Nos muestra los nombres de nuestros tags.

## Ver a que Hash (ID del commit) esta conectado el Tag

git show-ref --tags


## Ver Historial de Git

history


## Enviar Tags a GitHub

git push origin --tags

> Con esto enviamos todos nuestros tagsa GitHub, puedes verlos en la pestaña de branchs.

## Eliminar Tags de nuestro repositorio

git tag -d <nombre-tag>

> Con esto eliminaremos el tag del repositorio local

Si lo que deseas es eliminar el tag de GitHub primero debes eliminarlo del repositorio en GitHub debes ejecutar lo siguiente:

git push origin :refs/tags/<nombre-tag-a-borrar>

> Con este comando le dices a GitHub que lo quite de los Tags en tu repositorio remoto. Pero si no quieres que vuelva a aparecer debes borrarlo de tu repositorio local tambien.

## Git Rebase
Nos permite crear una rama comunmente usada para reparar errores, para luego integrarla a la rama que deseemos como si no hubiese pasado nada.

Un rebase es hacer cambios silenciosos

Para ello estando en la rama donde reparamos el error usamos el siguiente comando tomando en cuenta los siguientes pasos:
1. Hacemos rebase desde la rama temporal hacia donde queremos enviar los datos (Esto nos traera todo de dicha rama a la rama temporal para evitar un conflicto que solo puede ser resuelto con reset)
2. Ahora si nos posicionamos sobre la rama principal y le hacemos rebase para traernos los cambios a la rama principal.

git rebase <rama-a-integrarnos>

3. Finalmente borramos la rama temporal con: 

git branch -D <rama-a-borrar>  

> Rebase reescribe la historia del repositorio, cambia la historia de donde comenzó la rama y solo debe ser usado de manera local. Solo es recomendable usarlo en repositorio local ya que en uno remoto es una mala practica.

## Git Stash: Guardar cambios en memoria y recuperarlos después
Cuando necesitamos regresar en el tiempo porque borramos alguna línea de código pero no queremos pasarnos a otra rama porque nos daría un error ya que debemos pasar ese “mal cambio” que hicimos a stage, podemos usar git stash para regresar el cambio anterior que hicimos.

git stash es típico cuando estamos cambios que no merecen una rama o no merecen un rebase si no simplemente estamos probando algo y luego quieres volver rápidamente a tu versión anterior la cual es la correcta.

Digamos que tenemos unos cambios y necesitas cambiar a otra rama, **pero** no quieres o no necesitas hacer un commit aun, esto nos resultaria en error verdad. Podemos guardar esos cambios de forma temporal con:

git stash

> Notaras con tus cambios volvieron al ultimo commit, eso es porque los cambios se guardaron en el stash. **Algo a tomar en cuenta es que debes restaurar el stash en la misma rama que fue hecha para evitar problemas**

Para listar los stash usamos:

git stash list


Restaurar los cambios:

git stash pop

> Con esto restauraremos los cambios que guardamos de forma temporal

Para borrar el stash guardado usamos:

git stash drop


## Crear una rama a partir del stash

git stash branch <nombre-de-nueva-rama>

> Con esto creamos una rama nueva con las modificaciones hechas anteriormente y para guardar solo hacemos git commit -am "Tu Mensaje"```
