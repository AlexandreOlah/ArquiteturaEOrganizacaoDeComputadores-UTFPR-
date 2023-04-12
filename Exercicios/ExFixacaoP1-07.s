#Faça um programa, em assembly do mips, para somar dois vetores (V1 e V2) onde:
# v1 = {10,20,30,40,50,60}
# v2 = {0,10,-15, 16, 20, 30}
#O programa deverá percorrer os dois vetores somando cada elemento e colocando
#os mesmos no vetor resultante.
#A saída desejada é apresentada a seguir:
# A soma dos vetores v0 e v1 é:
# 10, 30, 15, 56, 70, 90
#OBS: Modele primeiro a solução em C depois traduza para assembly

.data
pula: .asciiz "\n"
v1: .word 10, 20, 30, 40, 50, 60
v2: .word 0, 10, -15, 16, 20, 30
.text
main:
#Inicializando
li $t1, 0
li $t2, 0
li $t3, 0 #Aux
li $t4, 0
la $s0,v1
la $s1,v2
la $s3, pula

#Loop
Loop:
lw $t3,0($s0)
lw $t1,0($s1)

add $t4, $t3, $t1
sw $t4, 0($s0)

lw $t3,0($s0)
li $v0, 1 #Impressao
add $a0, $zero, $t3
syscall

li $v0, 4 #Impressao \n
add $a0,$zero,$s3
syscall

addi $s0,$s0,4 #atualiza a referencia +4 bits
addi $s1,$s1,4 #atualiza a referencia +4 bits
addi $t2,$t2,1 #contador para passar nas 6 posições
beq $t2, 6, Sair
j Loop

#Exit
Sair:
li $v0, 10
syscall