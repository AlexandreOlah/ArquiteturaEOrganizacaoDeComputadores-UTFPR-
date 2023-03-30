#Codifique em assembly do mips um programa correspondente a :
#    int a = 2;
#    int b = 10;
#    x = 0;
#    if ( a >= 0 && b <= 50 )
#         x = 1;
#    printf("%i", x);
#Agora, teste a e b com outros valores.

.data 
.text
main:
  li $t0, 2   #A
  li $t1, 10  #B
  li $t2, 0   #Aux
  li $t3, 0   #X


  slt $t3, $t2, $t0
  add $t2, $zero, 51
  bne $t3, 1, Sair
    slt $t3, $t1, 51
    bne $t3, 1, Sair 		
      add $t3, $zero, 1         

  Sair:
    li $v0,1           #Impressão
    move $a0, $t3
    syscall

    li $v0, 10         #Exit
    syscall   	
  