#Faça o registrador $t0 e $t1 receberem os valores 15, e 30 respectivamente. E então faça um #programa para somar $t0 e $1, jogando o resultado da soma em $t3.

.data
.text
main:

addi $t0, $zero, 15 
addi $t1, $zero, 30

add $t3, $t0, $t1