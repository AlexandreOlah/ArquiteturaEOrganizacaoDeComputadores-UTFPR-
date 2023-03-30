#Codifique um programa correspondente ao seguinte código em c:
#    int a = 3;
#    int b = 4;
#    int m = 10;
#    m = a;
#    if ( b < m )
#        m = b;   
#    printf("%i", m);
#Agora, teste a e b com outros valores.

.data 
.text
main:
  li $t0, 3   #A
  li $t1, 4   #B
  li $t2, 10  #M
  li $t3, 0   #Aux

  add $t2, $zero, $t0
  slt $t3, $t1, $t2
  beq $t3, 1, Troca
  j Sair

  Troca:
    add $t2, $zero, $t1 
    j Sair   		

  Sair:
    li $v0,1           #Impressão
    move $a0, $t2
    syscall

    li $v0, 10         #Exit
    syscall   	
  