#1) Faça o registrador $t0 e $t1 receberem os valores 15, e 30 respectivamente. 
#E então faça um programa para somar $t0 e $1, jogando o resultado da soma em $t3.

.data
.text
main:
  addi $t1,$zero, 15	
  addi $t2,$zero, 30

  add $t3, $t1, $t2	

#Impressão
  li $v0, 1
  add $a0, $zero, $t3
  syscall
#Exit
  li $v0, 10
  syscall