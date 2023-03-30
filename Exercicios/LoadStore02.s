.data
.text
main:

li $t0, 100
li $t1, 200

sw $t0, 80($sp)
sw $t1, 160($sp)

lw $t2, 80($sp)

li $v0, 1
move $a0, $t2
syscall

lw $t3, 160($sp)

li $v0, 1
move $a0, $t3
syscall

li $v0, 10              #exit
syscall 