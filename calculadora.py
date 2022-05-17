import sys
global num
global num2
def update():
    menuinicial()
    teste()
    loop()


def linha1(tamanho = 15, estilo = '-='):
    print(f"{estilo*tamanho}{estilo[0]}")
    
def linha(tamanho:int, estilo = '-='):
    print(f"{estilo*tamanho}{estilo[0]}")



def menuinicial(titulo = 'Calculadora', tamanho = 15, estilo = '-='):


    linha(tamanho, estilo)
    print(f'{titulo:^{tamanho*2}}')
    linha(tamanho, estilo)

def number():
    global num
    global num2
    num = (input('Numero: '))
    num2 = (input('Numero: '))
    
    

def teste():
    erro = False
    while True:
        
        if erro == False:
            number()
            
             
            if not num.isdigit():
                print(f'Ocorreu um erro {num} Não é um valor valido')
            elif not num2.isdigit():
                print(f'Ocorreu um erro {num2} Não é um valor valido')
                update()

            else:
                operacao()
           
        else:
                erro == True
                break

           
                erro == True
                print("erro")
            

          

def operacao():
    global y
    global x
    x = int(num)
    y = int(num2)
    print (f'''1. Adição
2. Subtração
3. Divisão
4. Multiplicação
0. Sair''')
    global mat 
    mat = int(input('Digite a operação matematica: '))
   
        
    if mat >= 1 or mat <= 4:
        
        if mat == 1:
            print(x + y)
        if mat == 2:
            print(x - y)
        if mat == 3:
            print(x // y)
        if mat == 4:
            print(x * y)
            
     


    
    else:

        print('Ocorreu um erro',mat ,'Nã0 é um valor valido')
        print()
        
    sair = str(input("deseja sair? s/n "))
    if sair == "s":
        sys.exit()
    else:    
        linha1()
        teste()
    
def loop():
    
    erro = False
    while True:
        if erro == False:
            update()
        
        else:
            break

      



sair = False

opc = update()
if opc == 0:
    sair = True

