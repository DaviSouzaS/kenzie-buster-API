# kenzie-buster-API

OBS: Este não é o repositório original do projeto. O template deste projeto é privado, então não consigo colocar o repositório original como público (por este motivo o número de commits neste repositório é tão baixo).

Mais um projeto do módulo 5 do curso de desenvolvimento web full stack da Kenzie Academy Brasil. O projeto tem como objetivo gerenciar uma loja de filmes.

A aplicação gerencia usuários, filmes e pedidos, incluindo autenticação e permissões de rotas para diferentes tipos de usuário. Os usuários comuns podem ter acesso as informações dos filmes, realizar pedidos e editar informações do próprio perfil, já os administradores podem cadastrar filmes, editar informações de qualquer usuário e deletar filmes cadastrados.

Para a criação dos usuários estendi o comportamento do Abstract User do Django, tornando a tabela de usuários mais completa. Em comparação com o Node.Js acredito que o Python acaba sendo mais simples em criar CRUDs.

As tecnologias utilizadas para o desenvolvimento do projeto foram:

- Python
- Django
- djangorestframework
- djangorestframework-simplejwt
- SQLite
