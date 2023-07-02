#13) Implementar o código correspondente em mips
#
#    int vetor[] = {3, 0, 1, 2, -6, -2, 4, 10, 3, 7, 8, -9, -15, -20, -87, -100}
#    printf("Seja bem vindo! \nPor favor entre com um valor inteiro para pesquisar no vetor\n\n");
#    scanf("%i", elemento);
#    while(vetor[i] != -100){
#        if(vetor[i] == elemento){
#            printf("Elemento %i encontrado\n\n", elemento );
#            exit(0);
#        }
#        i++;
#    }
#    printf("Elemento não encontrado\n\n");
#    exit(0);

.data
  Frase:    .asciiz "Seja bem vindo! \nPor favor entre com um valor inteiro para pesquisar no vetor\n\n"
  Achou:    .asciiz "Elemento encontrado\n\n"
  NaoAchou: .asciiz "Elemento não encontrado\n\n"
  Vetor:    .word   3, 0, 1, 2, -6, -2, 4, 10, 3, 7, 8, -9, -15, -20, -87, -100
.text
main:
  la $a0, Frase
  li $v0, 4
  syscall

  li $v0, 5
  syscall
  move $t5, $v0

  la $t0, Vetor

While:
  lw $t1, 0($t0)

  beq $t5, $t1, Fim   

  la $a0, NaoAchou
  li $v0, 4
  syscall

  addi $t0, $t0, 4
  bne $t1, -100, While
  li $v0, 10
  syscall
   
Fim:
  la $a0, Achou
  li $v0, 4
  syscall

  add $a0, $zero, $t5
  li $v0, 1
  syscall

  li $v0, 10
  syscall