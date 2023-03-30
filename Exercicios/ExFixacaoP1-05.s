#Codifique em assembly do mips um programa correspondente a:
#    int i = 0;
#    int j = 10;
#    int k = 0;
#    while (i < j){
#        i++;
#        k +=10;
#    }
#    printf("%i", i);
#    printf("%i", k);

.data 
.text
main:

  li $t0, 0  #i
  li $t1, 10 #j  
  li $t2, 0  #k  
  li $t3, 0  #Aux    
  
  While:
    slt $t3, $t0, $t1
    bne $t3, 1, Sair
      addi $t0, $t0, 1
      addi $t2, $t2, 10
      j While      
      
  Sair:
    li $v0,1           #Impressão
    move $a0, $t0
    syscall
    li $v0,1           #Impressão
    move $a0, $t2
    syscall
    
    li $v0, 10         #Exit
    syscall   	