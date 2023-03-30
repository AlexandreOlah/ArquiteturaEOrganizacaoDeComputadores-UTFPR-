#Reproduza o programa visto durante a aula (slide 25).
#Leia e explique cada linha de código.

.data 
  save:.word 0, 0, 0, 0, 0, 5, 6, 7	
.text
main:

  la $t0, save         # $t0 = Save, Recebe o vetor como se fosse em C
  li $t1, 0            # $t1 = K, constante igual a zero
  li $t2, 0            # $t2 = i, indice
  
  While:
    sll $t3, $t2, 2    # "Transforma" o endereço para 4 btis
    add $s0, $t3, $t0  # Onde o ponteiro esta apontando 
    lw $s1,0($s0)      # Carrega o elemento que esta no vetor a partir do indice
    bne $s1,$t1,Sair   # caso for diferente ele Sai 
    addi $t2, $t2, 1   # i++
    j While            # Repete tudo a partir do While

  Sair:
    li $v0,1           #Impressão
    move $a0, $s1
    syscall
  
    li $v0, 10         #Exit
    syscall   
   