#Desenvolvido por Prô Terra - MakerZine
#Para mais detalhes, acesse: https://www.makerzine.com.br
def IntToBin(bin):
    binario = int(bin)
    n = len(str(binario))
    # valor_digitado = binario
    decimal = 0
    i = 0

    while n >= 0:
        resto = binario % 10
        decimal = decimal + (resto * (2**i))
        n = n - 1
        i = i + 1
        binario = binario // 10
    # print("O número (binario) digitado",valor_digitado,", na base decimal, vale:",decimal)

    return (decimal)
# ======================================================REGISTRADORES=========================================================
# A -> 111
# B -> 000
# C -> 001
# D -> 010
# E -> 011
# H -> 100
# L -> 101
# ==================================================ESTRUTURA=REGISTRADORES===================================================
VetRegistradores = ['111','000','001','010','011','100','101','Acum']

class Registradores:

    def __init__(self):
        self.RegA = 0
        self.RegB = 0
        self.RegC = 0
        self.RegD = 0
        self.RegE = 0
        self.RegH = 0
        self.RegL = 0
        self.Acum = 0  #Acumulador

    def setRegistradores(self,Registrador,Valor):        
        if   (Registrador == '111')  or (Registrador == 'A'):
            self.RegA = Valor
        elif (Registrador == '000')  or (Registrador == 'B'):
            self.RegB = Valor    
        elif (Registrador == '001')  or (Registrador == 'C'):
            self.RegC = Valor    
        elif (Registrador == '010')  or (Registrador == 'D'):
            self.RegD = Valor    
        elif (Registrador == '011')  or (Registrador == 'E'):
            self.RegE = Valor    
        elif (Registrador == '100')  or (Registrador == 'H'):
            self.RegH = Valor    
        elif (Registrador == '101')  or (Registrador == 'L'):
            self.RegL = Valor    
        elif (Registrador == 'Acum') or (Registrador == 'X'):
            self.Acum = Valor    

    def getRegistradores(self,Registrador):        
        if   (Registrador == '111')  or (Registrador == 'A'):
            return self.RegA
        elif (Registrador == '000')  or (Registrador == 'B'):
            return self.RegB    
        elif (Registrador == '001')  or (Registrador == 'C'):
            return self.RegC    
        elif (Registrador == '010')  or (Registrador == 'D'):
            return self.RegD    
        elif (Registrador == '011')  or (Registrador == 'E'):
            return self.RegE    
        elif (Registrador == '100')  or (Registrador == 'H'):
            return self.RegH    
        elif (Registrador == '101')  or (Registrador == 'L'):
            return self.RegL    
        elif (Registrador == 'Acum') or (Registrador == 'X'):
            return self.Acum    

    def ImprimeRegistradores(self,Comando):
        print('\n' * 10)
        print('---------------------------------------------------------------------------------')
        print('----------------------------TERMINAL-DE-REGISTRADORES----------------------------')
        print('---------------------------------------------------------------------------------')
        print('Ao executar o comando <'+Comando+'> são estes os valores dos registradores:')
        print(' Registrador A = ' , self.RegA )
        print(' Registrador B = ' , self.RegB )
        print(' Registrador C = ' , self.RegC )
        print(' Registrador D = ' , self.RegD )
        print(' Registrador E = ' , self.RegE )
        print(' Registrador H = ' , self.RegH )
        print(' Registrador L = ' , self.RegL )
        print('---------------------------------------------------------------------------------')
        print('\n')

# ============================================================OPCODE==========================================================
# Lógica e aritméticas
# ADD  ADDI   SUB  MULT  DIV  AND  OR  XOR  NOR  SLT   SLL  SRL  SRA  ANDI   ORI  XORI

# Chamadas de Sistema Sistema:
# IMPRIMIR INTEIRO
# SAIR (EXIT)
    
# Acesso a memória:
# LW  SW 

# Condicionais e Saltos condicionais:
# BEQ  BNE  

# Saltos incondicionais
# J JR JAL


# Mips   / z80  
# ADD   -> 10000rrr            (8 bits)      r = Registradores
# ADDI  -> 11000110 + nnnnnnnn (8 + 8 bits)  n = Numero em binario 

# LD  -> 01rrrRRR  (8 bits) r = Registrador 1 / R = Registrador 2 -> Conteudo de R é carregoda em r (Ambos ficam com o mesmo valor)
# LD -> 00rrr110 + nnnnnnnn (8 + 8 bits) r = Registrador 1 / n = Numero inteiro -> Inteiro de 8 bits (n) é carregado em r
# LD -> 01rrr110 (8 bits) r = Registrador 1 / HL = Conteudo de 8 bits na memória -> Inteiro de 8 bits (HL) é carregado em r
# LD -> 11011101 + 01rrr110 + dddddddd (8 + 8 + 8 bits) r = Registrador 1 / d = Numero Inteiro -> Registrador soma d + oq esta em IX
#--------------------------------------------------------Tratando-Entrada-----------------------------------------------------
LinhasArq = 0 

Entrada = open("Entrada01.txt",'r')
Entrada.seek(0,0) 
ArqAux = Entrada
ArqAux.seek(0,0)
ArqTexto = ArqAux.readlines()
Entrada.seek(0,0)                                                                      #Atualizar Cursor

for y in ArqTexto:
    LinhasArq = LinhasArq + 1

Reg = Registradores()
Reg.ImprimeRegistradores('Inicializando')

while LinhasArq != 0:
    AuxRegistrador1 = ''
    AuxNumero1 = 0

    LinhaArquivo = (Entrada.readline()).replace('\n', '') 
    if (LinhaArquivo == '' or LinhaArquivo == ' '):                                    #Verifica se o arquivo esta vazio ou em branco
        print('ERRO: Vazio!')
        exit()

    if   ((LinhaArquivo[0:2] == '00') and (LinhaArquivo[2:5] in VetRegistradores) and (LinhaArquivo[5:8] == '110')): #Tipo um ADDI no Mips
        AuxRegistrador1 = LinhaArquivo[2:5]
        AuxNumero1 = IntToBin(int((Entrada.readline()).replace('\n', '')[:8]))
        Reg.setRegistradores(AuxRegistrador1,AuxNumero1)
        Reg.ImprimeRegistradores(' ADDI ')      
        LinhasArq = LinhasArq - 1
    elif ((LinhaArquivo[0:2] == '01') and (LinhaArquivo[2:5] in VetRegistradores) and (LinhaArquivo[5:8] in VetRegistradores)): #Tipo um ADD no Mips
        AuxNumero1 = Reg.getRegistradores(LinhaArquivo[5:8])   
        Reg.setRegistradores(LinhaArquivo[2:5], AuxNumero1)
        Reg.ImprimeRegistradores(' ADD ')

    LinhasArq = LinhasArq - 1

ArqAux.close()
Entrada.close()