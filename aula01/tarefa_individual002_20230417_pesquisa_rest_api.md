## Tarefa 002 - 17/04/2022 - Pesquisa Rest API

1. Elaborar uma pesquisa sobre o tema "_Rest API_".
2. Elaborar um texto **no formato markdown** de pelo menos uma página, descrito com suas próprias palavras, destacando:
* As definições dos conceitos envolvidos;
* As principais características deste conceito (pelo menos umas cinco).

    Para que se possa definir o que é uma RESTfull API, é necessário definir o que é uma API e, em seguida, o que é REST. API é o acrônimo para Application Programming Interface, ou seja, um conjunto de regras que possibilita a comunicação entre diferentes aplicações. Ela é uma camada intermediária que processa a transferência de dados entre as aplicações envolvidas, por meio de requisições e respostas. Já o REST (REpresentational State Transfer) é uma arquitetura criada em 2000 por Roy Fielding e possui os seguintes princípios de design:
    <ul>
        <li><b>Interface uniforme:</b> Os recursos requisitados são conceitualmente separados da sua representação real, de modo que a informação retornada seja expressa em outro formato, "uniforme".</li>
        <li><b>Desacoplamento CLient-server: Separa o Cliente e o Servidor, de modo que a portabilidade do cliente é aprimorada por não precisar se preocupar com o armazenamento de dados, melhorando a portabiliade e escalabilidade.</b></li>
        <li><b>Inexistência de estado: Essa arquitetura é baseada em estados do cliente, de modo que quando se faz uma requisição ao servidor já se sabe qual estado atender para um recurso específico, assim o servidor não precisa armazenar essas informações específicas.</b></li>
        <li><b>Cacheabilidade: Os recursos devem ser "cacheáveis" ou no cliente ou no servidor, mas o servidor deve informar nas respostas se essas informações podem ser reutilizadas.</b></li>
        <li><b>Arquitetura por camadas: Essa abordagem possibilita a que as requisições do cliente se conectem a diferentes camadas do servidor, de modo que se possa adicionar diferentes partes intermediárias nessa comunicação, como serviços e middlewares.</b></li>
        <li><b>Code on demand:</b> As respostas do servidor podem envolver código executável, seja de componentes inteiros ou scripts em Javascript, por exemplo. </li>
    </ul>