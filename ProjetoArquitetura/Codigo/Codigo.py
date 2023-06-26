def BinToInt(bin):
    binario = int(bin)
    n = len(str(binario))
    decimal = 0
    i = 0

    while n >= 0:
        resto = binario % 10
        decimal = decimal + (resto * (2**i))
        n = n - 1
        i = i + 1
        binario = binario // 10

    return (decimal)

def IntToBin(valor):
    if valor == 0:
        return '0'  # Tratamento especial para o valor zero

    binario = ''
    while valor > 0:
        bit = valor % 2
        binario = str(bit) + binario
        valor = valor // 2

    return binario
# ======================================================REGISTRADORES=========================================================
# A -> 111
# B -> 000
# C -> 001
# D -> 010
# E -> 011
# H -> 100
# L -> 101 (Também é o registrador Acum)
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
        self.RegL = 0  #Acumulador
        # self.Acum = 0  
        self.Flgs = False
        self.Jump = False

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
        elif (Registrador == '101')  or (Registrador == 'L') or (Registrador == 'Acum'):
            self.RegL = Valor    
        # elif (Registrador == 'Acum'):
        #     self.Acum = Valor   
        elif (Registrador == 'Flgs'):
            self.Flgs = Valor               
        elif (Registrador == 'Jump'):
            self.Jump = Valor               

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
        elif (Registrador == '101')  or (Registrador == 'L') or (Registrador == 'Acum'):
            return self.RegL    
        # elif (Registrador == 'Acum'):
        #     return self.Acum    
        elif (Registrador == 'Flgs'):
            return self.Flgs    
        elif (Registrador == 'Jump'):
            return self.Jump    

    def ImprimeRegistradores(self,Comando):
        # print('\n' * 10)
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

# Registradores - ['111','000','001','010','011','100','101','Acum']
# LI   -> 00rrr110 nnnnnnnn (n é adicionado ao Registrador r)
# LD   -> 01rrrRRR          (Regitrador R é adicionado ao Registrador r)
# ADD  -> 10000rrr          (Valor adicionado ao Registrador 'Acum')
# ADDI -> 11000110 nnnnnnnn (Valor adicionado ao Registrador 'Acum')
# SUB  -> 10010rrr          (Valor adicionado ao Registrador 'Acum')
# SUBI -> 11010110 nnnnnnnn (Valor adicionado ao Registrador 'Acum')
# MUL  -> 11110110 rrrRRR-- (Valor adicionado ao Registrador 'Acum')
# AND  -> 10100rrr          (Compara r com o Registrador 'Acum')
# OR   -> 10110rrr          (Compara r com o Registrador 'Acum')
# XOR  -> 10101rrr          (Compara r com o Registrador 'Acum')
# ANDI -> 11100110 nnnnnnnn (Compara r com o n)
# ORI  -> 11110110 nnnnnnnn (Compara r com o n)
# XORI -> 11101110 nnnnnnnn (Compara r com o n)
# BEQ  -> 11000011 xxxxxxxx (Compara n com 'Acum' ai GoTo ou não)
# BNE  -> 11000010 xxxxxxxx (Compara n com 'Acum' ai GoTo ou não)
# JUMP -> 00011000 xxxxxxxx (GoTo)
# IMP  -> 10000rrr          (Imprime Registrador r)
# EXT  -> 01110110          (Sair)

#--------------------------------------------------------Tratando-Entrada-----------------------------------------------------
LinhasArq        = 0 
CountIntructions = 0 
VetInstructions  = []

Entrada = open("Entrada02.txt",'r')
Entrada.seek(0,0) 
ArqAux = Entrada
ArqAux.seek(0,0)
ArqTexto = ArqAux.readlines()
Entrada.seek(0,0)                                                                      #Atualizar Cursor

for y in ArqTexto:
    LinhasArq = LinhasArq + 1

AuxCountLinhas = LinhasArq    

Reg = Registradores()
Reg.ImprimeRegistradores('Inicializando')

while LinhasArq != 0:
    AuxRegistrador1 = ''
    AuxNumero1 = 0
    AuxNumero2 = 0
    AuxStr1 = ''
    AuxStr2 = ''
    AuxStr3 = ''

    if (Reg.getRegistradores('Jump') == False):
        LinhaArquivo = (Entrada.readline()).replace('\n', '') 
        if (LinhaArquivo == '' or LinhaArquivo == ' '):                                    #Verifica se o arquivo esta vazio ou em branco
            print('ERRO: Vazio!')
            exit()
    else:
        Reg.setRegistradores('Jump',False) 
        print('asdqasda',LinhasArq)
        Entrada.seek(LinhasArq,0)

    VetInstructions.append(LinhaArquivo)
#---------------------------------------------------------Acesso-a-Memoria----------------------------------------------------
#                                                             LW  SW 
#... ....................................................................................................................        
    if   ((LinhaArquivo[0:2] == '00') and (LinhaArquivo[2:5] in VetRegistradores) and (LinhaArquivo[5:8] == '110')):            
        AuxRegistrador1 = LinhaArquivo[2:5]
        AuxNumero1 = BinToInt(int((Entrada.readline()).replace('\n', '')[:8]))
        Reg.setRegistradores(AuxRegistrador1,AuxNumero1)
        Reg.ImprimeRegistradores(' LI ')  # Tipo LI no MIPS   
        LinhasArq = LinhasArq - 1
        AuxNumero1 = 0 
#... ....................................................................................................................        
    elif ((LinhaArquivo[0:2] == '01') and (LinhaArquivo[2:5] in VetRegistradores) and (LinhaArquivo[5:8] in VetRegistradores)): 
        AuxNumero1 = Reg.getRegistradores(LinhaArquivo[5:8])
        Reg.setRegistradores(LinhaArquivo[2:5], AuxNumero1)
        Reg.ImprimeRegistradores(' LD ')  # Tipo LD no MIPS   
        AuxNumero1 = 0 
#------------------------------------------------------Logicas-e-Aritmeticas--------------------------------------------------
#                     ADD  ADDI   SUB  MULT  DIV  AND  OR  XOR  NOR  SLT   SLL  SRL  SRA  ANDI   ORI  XORI
#...ADD A, r..................................................................................................................
    elif ((LinhaArquivo[0:5] == '10000') and (LinhaArquivo[5:8] in VetRegistradores)):                                          
        AuxNumero1 = Reg.getRegistradores(LinhaArquivo[5:8])
        Reg.setRegistradores('Acum', AuxNumero1)
        Reg.ImprimeRegistradores(' ADD ') # Tipo ADD no MIPS
        AuxNumero1 = 0 
#...ADD A, n..................................................................................................................        
    elif ((LinhaArquivo[0:8] == '11000110')):                                                                                   
        AuxNumero1 = BinToInt(int((Entrada.readline()).replace('\n', '')[:8]))
        AuxNumero1 = AuxNumero1 + (Reg.getRegistradores('Acum'))
        Reg.setRegistradores('Acum',AuxNumero1)
        Reg.ImprimeRegistradores(' ADDI ') # Tipo ADDI no MIPS
        LinhasArq = LinhasArq - 1
        AuxNumero1 = 0 
#...SUB r   ..................................................................................................................        
    elif ((LinhaArquivo[0:5] == '10010') and (LinhaArquivo[5:8] in VetRegistradores)): 
        AuxNumero1 = (Reg.getRegistradores('Acum') - Reg.getRegistradores(LinhaArquivo[5:8]))
        Reg.setRegistradores('Acum', AuxNumero1)
        Reg.ImprimeRegistradores(' SUB ') # Tipo SUB no MIPS
        AuxNumero1 = 0 
#...SUB n   ..................................................................................................................        
    elif ((LinhaArquivo[0:8] == '11010110')):                                                                                   
        AuxNumero1 = (Reg.getRegistradores('Acum') - BinToInt(int((Entrada.readline()).replace('\n', '')[:8])))
        Reg.setRegistradores('Acum',AuxNumero1)
        Reg.ImprimeRegistradores(' SUBI ') # Tipo SUBI no MIPS
        LinhasArq = LinhasArq - 1
        AuxNumero1 = 0 
#...MUL     ..................................................................................................................        
    elif ((LinhaArquivo[0:8] == '11110110')):   
        AuxStr1    = (Entrada.readline()).replace('\n', '')[0:6]
        AuxNumero1 = (Reg.getRegistradores(AuxStr1[0:3]) * Reg.getRegistradores(AuxStr1[3:6]))

        Reg.setRegistradores('Acum',AuxNumero1)
        Reg.ImprimeRegistradores(' MUL ') # Tipo MUL no MIPS
        LinhasArq = LinhasArq - 1
        AuxNumero1 = 0 
        AuxStr1 = ''
        # Função adaptada por mim
#...DIV     ..................................................................................................................        
    # O processador Z80 não possui uma instrução de divisão embutida. Ao contrário da instrução de multiplicação (MUL), o Z80 não possui uma instrução específica para a divisão de números.
#...AND r   ..................................................................................................................        
    elif ((LinhaArquivo[0:5] == '10100') and (LinhaArquivo[5:8] in VetRegistradores)):
        AuxNumero1 = Reg.getRegistradores('Acum')
        AuxNumero2 = Reg.getRegistradores(LinhaArquivo[5:8])
        AuxStr1    = IntToBin(AuxNumero1)
        AuxStr2    = IntToBin(AuxNumero2)

        for w in range(len(AuxStr1)):
            if (AuxStr1[w] == AuxStr2[w]):
                AuxStr3 = AuxStr3 + '1'
            else:    
                AuxStr3 = AuxStr3 + '0'
        
        AuxNumero1 = 0     
        AuxNumero1 = BinToInt(AuxStr3)
        Reg.setRegistradores('Acum',AuxNumero1)

        Reg.ImprimeRegistradores(' AND ') # Tipo AND no MIPS
        AuxNumero1 = 0     
        AuxNumero2 = 0     
#...OR      ..................................................................................................................        
    elif ((LinhaArquivo[0:5] == '10110') and (LinhaArquivo[5:8] in VetRegistradores)):
        AuxNumero1 = Reg.getRegistradores('Acum')
        AuxNumero2 = Reg.getRegistradores(LinhaArquivo[5:8])
        AuxStr1    = IntToBin(AuxNumero1)
        AuxStr2    = IntToBin(AuxNumero2)

        for w in range(len(AuxStr1)):
            if ((AuxStr1[w] == '1') or (AuxStr2[w] == '1')):
                AuxStr3 = AuxStr3 + '1'
            else:    
                AuxStr3 = AuxStr3 + '0'
        
        AuxNumero1 = 0     
        AuxNumero1 = BinToInt(AuxStr3)
        Reg.setRegistradores('Acum',AuxNumero1)

        Reg.ImprimeRegistradores(' OR ') # Tipo OR no MIPS
        AuxNumero1 = 0     
        AuxNumero2 = 0     
#...XOR     ..................................................................................................................        
    elif ((LinhaArquivo[0:5] == '10101') and (LinhaArquivo[5:8] in VetRegistradores)):
        AuxNumero1 = Reg.getRegistradores('Acum')
        AuxNumero2 = Reg.getRegistradores(LinhaArquivo[5:8])
        AuxStr1    = IntToBin(AuxNumero1)
        AuxStr2    = IntToBin(AuxNumero2)

        for w in range(len(AuxStr1)):
            if (AuxStr1[w] != AuxStr2[w]):
                AuxStr3 = AuxStr3 + '1'
            else:    
                AuxStr3 = AuxStr3 + '0'
        
        AuxNumero1 = 0     
        AuxNumero1 = BinToInt(AuxStr3)
        Reg.setRegistradores('Acum',AuxNumero1)

        Reg.ImprimeRegistradores(' XOR ') # Tipo XOR no MIPS
        AuxNumero1 = 0     
        AuxNumero2 = 0     
#...NOR     ..................................................................................................................        
    # No processador Z80, não existe uma instrução NOR (ou "OR Negado") nativamente implementada. 
    # A instrução NOR é uma operação lógica que retorna o resultado "1" apenas se ambos os bits de entrada forem "0". 
    # Embora o Z80 possua instruções lógicas básicas, como AND e OR, não possui uma instrução específica para NOR.
#...SLT     ..................................................................................................................  
    elif ((LinhaArquivo[0:5] == '10111') and (LinhaArquivo[5:8] in VetRegistradores)):
        AuxNumero1 = Reg.getRegistradores('Acum')
        AuxNumero2 = Reg.getRegistradores(LinhaArquivo[5:8])
        AuxStr1    = IntToBin(AuxNumero1)
        AuxStr2    = IntToBin(AuxNumero2)

        if (AuxStr1[w] < AuxStr2[w]):
               Reg.getRegistradores('Flgs',True)
        else:    
           Reg.getRegistradores('Flgs',False)
        
        Reg.ImprimeRegistradores(' SLT ') # Tipo SLT no MIPS
        AuxNumero1 = 0     
        AuxNumero2 = 0     

#...SLL     ..................................................................................................................            
    # O processador Z80 não possui uma instrução diretamente equivalente à instrução SLL (Shift Left Logical) do MIPS. 
    # A instrução SLL no MIPS realiza um deslocamento lógico para a esquerda dos bits de um registrador, 
    # preenchendo os bits de menor ordem com zeros.

#...SRL     ..................................................................................................................        
    # Não encontrada no Manual 
#...SRA     ..................................................................................................................        
    # Não encontrada no Manual 
#...ANDI    ..................................................................................................................        
    elif (LinhaArquivo[0:5] == '11100110'):
        AuxNumero1 = Reg.getRegistradores('Acum')
        AuxStr1    = IntToBin(AuxNumero1)
        AuxStr2    = (Entrada.readline()).replace('\n', '')[:8]
        LinhasArq = LinhasArq - 1

        for w in range(len(AuxStr1)):
            if (AuxStr1[w] == AuxStr2[w]):
                AuxStr3 = AuxStr3 + '1'
            else:    
                AuxStr3 = AuxStr3 + '0'
        
        AuxNumero1 = 0     
        AuxNumero1 = BinToInt(AuxStr3)
        Reg.setRegistradores('Acum',AuxNumero1)

        Reg.ImprimeRegistradores(' ANDI ') # Tipo ANDI no MIPS
        AuxNumero1 = 0     
        AuxNumero2 = 0     
#...ORI     ..................................................................................................................        
    elif (LinhaArquivo[0:5] == '11110110'):
        AuxNumero1 = Reg.getRegistradores('Acum')
        AuxStr1    = IntToBin(AuxNumero1)
        AuxStr2    = (Entrada.readline()).replace('\n', '')[:8]
        LinhasArq = LinhasArq - 1

        for w in range(len(AuxStr1)):
            if ((AuxStr1[w] == '1') or (AuxStr2[w] == '1')):
                AuxStr3 = AuxStr3 + '1'
            else:    
                AuxStr3 = AuxStr3 + '0'
        
        AuxNumero1 = 0     
        AuxNumero1 = BinToInt(AuxStr3)
        Reg.setRegistradores('Acum',AuxNumero1)

        Reg.ImprimeRegistradores(' ORI ') # Tipo ORI no MIPS
        AuxNumero1 = 0     
        AuxNumero2 = 0     
#...XORI    ..................................................................................................................        
    elif (LinhaArquivo[0:5] == '11101110'):
        AuxNumero1 = Reg.getRegistradores('Acum')
        AuxStr1    = IntToBin(AuxNumero1)
        AuxStr2    = (Entrada.readline()).replace('\n', '')[:8]
        LinhasArq = LinhasArq - 1

        for w in range(len(AuxStr1)):
            if (AuxStr1[w] != AuxStr2[w]):
                AuxStr3 = AuxStr3 + '1'
            else:    
                AuxStr3 = AuxStr3 + '0'
        
        AuxNumero1 = 0     
        AuxNumero1 = BinToInt(AuxStr3)
        Reg.setRegistradores('Acum',AuxNumero1)

        Reg.ImprimeRegistradores(' XORI ') # Tipo XORI no MIPS
        AuxNumero1 = 0     
        AuxNumero2 = 0     

#------------------------------------------------------Condicionais-e-Saltos--------------------------------------------------
#                                                            BEQ  BNE  
#...Jp nn   ..................................................................................................................        
    elif (LinhaArquivo[0:8] == '11000011'):  
        print('Aqui',LinhasArq )
        BinParaComparar = (Entrada.readline()).replace('\n', '')[:8]
        InstructionGoTo = (Entrada.readline()).replace('\n', '')[:8]
        
        if (BinParaComparar == Reg.getRegistradores('Acum')):
            LinhaArquivo = InstructionGoTo
            LinhasArq = LinhasArq + 1
            Reg.setRegistradores('Jump',True)

        Reg.ImprimeRegistradores(' BEQ ') # Tipo BEQ no MIPS
        
    elif (LinhaArquivo[0:8] == '11000010'):                                          
        BinParaComparar = (Entrada.readline()).replace('\n', '')[:8]
        InstructionGoTo = (Entrada.readline()).replace('\n', '')[:8]
        
        if (BinParaComparar != Reg.getRegistradores('Acum')):
            LinhaArquivo = InstructionGoTo
            LinhasArq = LinhasArq + 1
            Reg.setRegistradores('Jump',True)
        else:    
            LinhasArq = LinhasArq + 2

        Reg.ImprimeRegistradores(' BNE ') # Tipo BNE no MIPS
#------------------------------------------------------Saltos-Incondicionais--------------------------------------------------        
#                                                            J JR JAL
#...Jp e    ..................................................................................................................        
    elif (LinhaArquivo[0:5] == '00011000'):
        InstructionGoTo = (Entrada.readline()).replace('\n', '')[:8]
        
        LinhaArquivo = InstructionGoTo
        # Reg.setRegistradores('Jump',True)
        for x in range(len(VetInstructions)):
            AuxNumero1 = x

        LinhasArq = AuxNumero1 + 1      

        print('LINHAS ARQ',LinhasArq)
        Reg.ImprimeRegistradores(' JUMP ') # Tipo J no MIPS
        AuxNumero1 = 0 

#  JR JAL -> Não foi possível pois o processador tem poucos recursos e não conseguimos replicar de forma fiel

#-------------------------------------------------------Chamadas-de-Sistema---------------------------------------------------
#                                                  IMPRIMIR INTEIRO / SAIR (EXIT)
#...IMPRIMI ..................................................................................................................        
    # No contexto do processador Z80, não há uma chamada de sistema específica para impressão. O Z80 é um processador de arquitetura de 8 bits que não possui um sistema operacional embutido. Portanto, não há chamadas de sistema padrão para operações de entrada e saída.
    # No entanto, ao utilizar o Z80 em conjunto com um sistema ou ambiente específico, é possível usar instruções de E/S (entrada/saída) específicas desse sistema para realizar operações de impressão. A maneira exata de realizar uma operação de impressão depende do sistema operacional ou ambiente no qual o Z80 está sendo usado.
    # Por exemplo, em um sistema que utiliza o CP/M (Control Program for Microcomputers), um sistema operacional popular para computadores baseados no Z80, a chamada de sistema para impressão seria feita por meio da interrupção do sistema com o número apropriado do serviço de impressão.
    # Em resumo, a chamada de sistema específica para impressão no Z80 varia de acordo com o sistema operacional ou ambiente específico no qual o processador está sendo usado. É necessário consultar a documentação ou as especificações do sistema em questão para obter informações detalhadas sobre a chamada de sistema correta para impressão.

    # Solução encontrada por mim para imprimir
    elif ((LinhaArquivo[0:5] == '11000') and (LinhaArquivo[5:8] in VetRegistradores)):                                          
        print('ASDASDASDASDASDA')
        AuxNumero1 = Reg.getRegistradores(LinhaArquivo[5:8])
        Reg.ImprimeRegistradores(' IMP ') # Tipo syscall 5 no MIPS
        print('Impressão do Registrador <',LinhaArquivo[5:8],'> nele encontra o valor:',AuxNumero1)
        AuxNumero1 = 0     

#...SAIR    ..................................................................................................................        
    # No processador Z80, não há uma instrução específica em binário para "sair do sistema". O Z80 é um processador de arquitetura de 8 bits que não possui uma instrução nativa para finalizar ou encerrar um programa.
    # A funcionalidade de "sair do sistema" é normalmente implementada usando chamadas de sistema ou interrupções específicas do sistema operacional ou ambiente em que o Z80 está sendo utilizado.
    # Portanto, a instrução binária específica para "sair do sistema" no Z80 depende do sistema operacional ou ambiente específico em que o processador está sendo executado. Cada sistema operacional pode ter sua própria forma de realizar essa operação, por meio de interrupções ou chamadas de sistema específicas.
    # Para determinar a instrução binária exata para "sair do sistema" no seu contexto específico, é necessário consultar a documentação ou as especificações do sistema operacional ou ambiente em questão.

    #  A instrução HALT suspende a operação da CPU até que uma interrupção ou reinicialização subseqüente seja
    # recebido. Enquanto no estado HALT, o processador executa NOPs para manter a memória
    # lógica de atualização.
    elif ((LinhaArquivo[0:8] == '01110110')):                                                                                   
        Reg.ImprimeRegistradores(' EXT ') # Tipo syscall 10 no MIPS
        print('\n---------------------------------------EXIT--------------------------------------\n')
        LinhasArq = 0  

    if ((LinhaArquivo[0:8] == '01110110')):
        LinhasArq = 0  
    else:        
        LinhasArq = LinhasArq - 1

ArqAux.close()
Entrada.close()