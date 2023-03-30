#Faça o registrador $t0 e $t1 receberem os valores 10, e 20 respectivamente. E então faça um 
#programa para resolver a seguinte expressão:
#   $t3 = ($t0 + 4) - ($t1 - 6)

.data
.text
main:

addi $t0, $zero, 10 
addi $t1, $zero, 20
addi $t3, $zero, 0 

addi $t0, $t0, 4
addi $t1, $t1, -6

sub $t3, $t0, $t1