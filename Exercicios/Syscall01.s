.data
.text
main:

li $t0, 50
li $t1, 100

sw $t0, 40($sp)
sw $t1, 56($sp)

lw $t2, 40($sp)
lw $t3, 56($sp)

add $t3, $t2, $t3

li $v0, 1
move $a0, $t3
syscall

li $v0, 10              #exit
syscall 