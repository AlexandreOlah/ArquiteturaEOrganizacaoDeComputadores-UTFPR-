#Faça um programa, em assembly do mips, que receba dois inteiros do teclado, 
#e imprima o maior. Se os números forem iguais imprima -111.

.data
.text
main:
  li $t3,3	
  li $t4,-111

  li $v0, 5		#Receber Int do teclado
  syscall
  move $t0, $v0

  li $v0, 5		#Receber Int do teclado
  syscall
  move $t1, $v0

  beq $t0,$t1,Igual
    slt $t3,$t0,$t1
    beq $t3,1,Verdade
      li $v0, 1
      move $a0, $t0
      syscall
      li $v0, 10         #exit
      syscall 

  Igual:
    li $v0, 1
    move $a0, $t4
    syscall
    li $v0, 10         #exit
    syscall 
  Verdade:
    li $v0, 1
    move $a0, $t1
    syscall
    li $v0, 10         #exit
    syscall 