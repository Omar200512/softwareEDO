import sympy as sp
import numpy as np
import tools as t

head = t.read_file("admin_header")
tail  = t.read_file("admin_tail") 

sp.init_printing(use_unicode=True)

        

# -- Ejercicio 2 -- 

def ejer2(m):
    
    for i in range(0,m):
    
        #-- Creación del archivo .tex --
        
        # Nombre del archivo
        namefile =  "./tex/ejerc2_" + str(i)+".tex"
        
        # -- Apertura del archivo  --       
        file = open(namefile, 'w')

        # -- Escritura del preámbulo en el archivo .tex --
        file.write(str(head)) 
        
        
        # -- Declaración de los vectores pseudo aleatorios  de números enteros --
        a = np.random.randint(3,7,1)        
        b = np.random.randint(-2,3,1)        
        
        # -- Declaración de la variable simbólica --
        x  = sp.Symbol('x')
        y = sp.Function('y')(x)

        # Declaración de la ecuación diferencial homogénea
        expr = sp.diff(y, x, x) + a[0] * sp.diff(y, x) + b[0] * y

        # Encabezados del ejercicio              
        file.write('Resolver la ecuación diferencial homogénea de segundo orden:\n')    
        file.write('\\begin{center} \n')
        file.write('$\displaystyle ' + sp.latex(expr) + '=0 $')
        file.write('\end{center}\n')

          
        # Respuesta al ejercicio        
        file.write('\\begin{center}\n')
        file.write('\\textbf{Respuesta}\n')
        file.write('\end{center}\n')
                
        file.write('\\begin{enumerate}\n')
        
        # -- Solución general de la EDO --     
        sol = sp.dsolve(expr)
        file.write('\item La solución general de la ecuación es: $ y(x)=' + sp.latex(sol.rhs) + '$\n')
        
        # -- Condiciones iniciales --
        file.write('\item Las condiciones iniciales no se proporcionan.\n')
        
        file.write('\\end{enumerate}')
        
        # -- Escritura final en el archivo .tex --             
        file.write(str(tail))      

        # -- Cierre del archivo .tex --           
        file.close()


# -- Generacion de 10 ejercicios .tex (descomentar uno a la vez). Correr el archivo --      
m = 10 
ejer2(m)

# -- Ejecutar en la terminal para general los archivos .pdf: --

# GNU-Linux
# for i in *.tex; do pdflatex $i; done && rm *.aux *.log *.tex

# MS Windows
#  FOR \%i IN (*.tex) DO pdflatex %i &&  DEL *.log *.aux *.out
