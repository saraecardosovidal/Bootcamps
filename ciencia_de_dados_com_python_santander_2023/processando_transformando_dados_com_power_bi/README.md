Descrição do desafio módulo 3 – Processamento de Dados Simplificado com Power BI

1. Criei uma instancia na Azure para SQL
2. Criei o Banco de dados com base disponível no github
3. Integrei o Power BI com SQL no Azure
4. Removi colunas que não são utilizadas

Realizei esses passos anteriormente, porém meu projeto corrompeu e expirou a licensa gratutita na Azure, portanto, para não deixar de entregar o desafio realizando as transformações, construi o banco no Excel.

Diretrizes para transformação dos dados

1. Verifique os cabeçalhos e tipos de dados
OK

2. Modifique os valores monetários para o tipo double preciso
Campo Salary da tabela Employee alterado para double preciso.

3. Verifique a existência dos nulos e analise a remoção
OK

4. Os employees com nulos em Super_ssn podem ser os gerentes. Verifique se há algum colaborador sem gerente
OK, na tabela employee há um gerente, sem gerente superior, no registro 8 - James.

5. Verifique se há algum departamento sem gerente
OK

6. Se houver departamento sem gerente, suponha que você possui os dados e preencha as lacunas.
Departamento Headquarters estava sem gerente atribuido e substitui pelo código do James (chefe do Franklin e da Jeniffer).

7. Verifique o número de horas dos projetos
Mesclei a tabela Works_on com a Project atraves dos campos Pno e Pnumber respectivamente, removi as colunas que não são necessárias no momento e realizei um agrupamento pela coluna Pname (nome do projeto) e somei a coluna Hours.

8. Separar colunas complexas
Separei a coluna Address na tabela Employee utilizando o Dividir Coluna por Delimitador '-', obtendo assim 5 colunas. Após isso ajustei os dados apenas do registros 4 e obtive as 4 colunas finais: Address, Number, City e State.

9. Mesclar consultas employee e departament para criar uma tabela employee com o nome dos departamentos associados aos colaboradores. A mescla terá como base a tabela employee. Fique atento, essa informação influencia no tipo de junção
Mesclei a tabela Employee com a Departament atraves dos campos Dno e Dnumber respectivamente.

10. Neste processo elimine as colunas desnecessárias.
OK

11. Realize a junção dos colaboradores e respectivos nomes dos gerentes . Isso pode ser feito com consulta SQL ou pela mescla de tabelas com Power BI. Caso utilize SQL, especifique no README a query utilizada no processo.
Realizei a mescla entre a tabela employees_departament e employee atraves dos campos Super_ssn e Ssn respectivamente e mantive apenas o campo Fname, renomeando o mesmo para Manager.

12. Mescle as colunas de Nome e Sobrenome para ter apenas uma coluna definindo os nomes dos colaboradores
Realizado na tabela employees_departament através do Mesclar Colunas com os campos Fname, Minit e Lname, renomeando o campo para Full_name.

13. Mescle os nomes de departamentos e localização. Isso fará que cada combinação departamento-local seja único. Isso irá auxiliar na criação do modelo estrela em um módulo futuro.
Tabela Departament_Location

14. Explique por que, neste caso supracitado, podemos apenas utilizar o mesclar e não o atribuir.
Para utilização do Combinar>Acrescentar Consultas é necessário possuir uma estrutura padrão dos dados, pois eles são empilhados, já para utilizar o Combinar>Mesclar Consultas é necessário apenas uma coluna para chave de relacionamento entre as tabelas e a informação será acrescentada em determinada estrutura já realizada, funcionando como um join.

15. Agrupe os dados a fim de saber quantos colaboradores existem por gerente
Tabela Employees_departament

16. Elimine as colunas desnecessárias, que não serão usadas no relatório, de cada tabela
