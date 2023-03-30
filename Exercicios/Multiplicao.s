#Faça um programa, em assembly do MIPS, que receba e multiplique 
#dois inteiros POSITIVOS, sem usar a instrução de multiplicação do MIPS. 
#Imprima o resultado na tela.

.data 
.text
main:
  li $t0,0	
  li $t1,0
  li $t2,0  

  li $v0, 5            #Recebe Teclado
  syscall   
  move $t0, $v0

  li $v0, 5            #Recebe Teclado
  syscall   
  move $t1, $v0

  While:
    add  $t2, $t2, $t1
    addi $t0, $t0, -1
    beq  $t0, 0, Sair
      j  While

  Sair:
    li $v0,1           #Impressão
    move $a0, $t2
    syscall
  
    li $v0, 10         #Exit
    syscall  