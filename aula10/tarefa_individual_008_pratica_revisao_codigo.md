# Tarefa Individual 008

## Models

   1. Cliente: 
- Nenhuma inconformidade
   2. PremioSeguro:
   	- Nesting de cláusulas IF das linhas 42-53 deve ser removido.
   	- Verificações de condição das cláusulas IF da linha 56 são repetidas várias vezes,  neste caso deveria se nestar.
   3. Teste:
   	- Nenhuma inconformidade
   	
##Util
1. CpfValidador:
	- Condição IF da linha 38 é totalmente ineficiente, operaçõesmatemáticas pela divisão do número por 10 e seu armazenamento numarray da biblioteca ND4J seria mais eficiente.
2. CpfValidadorRefactored
	- Refatorado para pior (mesmo problema da classe anterior)
3. DataUtils
	- Variável "result" da linha 100 não é utilizada
4. EstadoCivilValidador
	- Linhas 17-21 era possível utilizar um operador ternário paradeixar o código mais conciso
5. NacionalidadeValidador
	- Nenhuma inconformidade
6. PassaporteValidador
	- Três imports de pacotes não utilizados
7. SexoValidador
	- Nenhuma inconformidade
##Testes

1. ClientTest
	- No teste validaEstadoCivil1 está faltando a linha expected = EstadoCivilInvalidoException.class