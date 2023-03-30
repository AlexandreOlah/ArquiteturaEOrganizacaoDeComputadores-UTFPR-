.data
.text
main:

li $t0, 0
li $t1, 0

li $v0, 5		#Receber Int do teclado
syscall
move $t0, $v0

li $v0, 5		#Receber Int do teclado
syscall
move $t1, $v0

sub $t0, $t0, $t1

li $v0, 1
move $a0, $t0
syscall

li $v0, 10         #exit
syscall 