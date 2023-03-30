#A partir do código assembly do mips, ao qual implementa o programa a seguir:
#    int fat = 0;
#    int n = 5;         
#    for(fat = 1; n > 1; n = n - 1)
#        fat = fat * n;     
#    printf("%d", fat);
#OBS: Não utilize a instrução MUL, faça a partir de sucessivas somas.
.data
  pula: .asciiz "\n Bye Bye\n"
  separa: .asciiz " - "
.text
main:
  li $t0, 6 #fat
  li $t1, 6 #n
  li $t2, 0 #Aux
  li $t3, 0 #Somatorio do Fat
  li $t4, 0 #Somatorio do Fat
  la $s3, pula
  la $s2, separa

  for:
    addi $t2,$t0,-1
    Mult:
      add $t3,$t3,$t1
      addi $t2,$t2,-1
      bne $t2,0,Mult
        add $t1,$zero,$t3
        add $t0,$t0,-1
        beq $t0,1,Sair
          add $t3,$zero,$zero
          j for

Sair:
  li $v0, 1                     #Imprime resultado
  move $a0,$t3
  syscall

  li $v0, 4                     #Impressao \n
  add $a0,$zero,$s3
  syscall

  li $v0, 10                     #EXIT
  syscall