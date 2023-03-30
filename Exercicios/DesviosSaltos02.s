#Faça um programa, em assembly do mips, que receba um valor inteiro do teclado, 
#se esse valor for igual a 10 imprima-o na tela e saia do programa. 
#Senão imprima 0 e saia do programa.

.data
.text
main:
  li $t0, 10 
  li $t2, 0

  li $v0, 5		#Receber Int do teclado
  syscall
  move $t1, $v0

  beq $t0,$t1,Igual
    li $v0, 1
    move $a0, $t2
    syscall 
    li $v0, 10         #exit
    syscall 

  Igual:
    li $v0, 1
    move $a0, $t1
    syscall
    li $v0, 10         #exit
    syscall 