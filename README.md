<h1 align="center">Snake Game</h1>

<p align="center">🐍</p>

<p align="center">
 <a href="#objetivo">Objetivo</a> •
 <a href="#tecnologias">Tecnologias</a> • 
 <a href="#autor">Autor</a>
</p>


### Objetivo
---
<h3>Este código em Python usa a biblioteca Pygame para criar um jogo simples de "Snake", onde o jogador controla uma cobra que deve comer a comida que aparece na tela para crescer. Aqui está uma descrição do código:
O código começa importando as bibliotecas necessárias: pygame para a criação do jogo e random para gerar números aleatórios.
O jogo é inicializado usando pygame.init() e a janela é configurada com o título "Snake" usando pygame.display.set_caption(). O tamanho da janela é definido como 1200 pixels de largura por 800 pixels de altura, e a tela é criada usando pygame.display.set_mode(). Um relógio é inicializado usando pygame.time.Clock() para controlar a taxa de quadros do jogo.
As constantes square_size e game_speed determinam o tamanho dos quadrados que compõem a cobra e a velocidade do jogo, respectivamente.
A função create_food() é definida para gerar coordenadas aleatórias para a comida. A comida é posicionada em múltiplos do tamanho do quadrado para que fique alinhada corretamente na tela.
As funções draw_food(), draw_snake(), e draw_score() são definidas para desenhar a comida, a cobra e a pontuação na tela, respectivamente.
A função speed_select(key) recebe a tecla pressionada pelo jogador e retorna as velocidades horizontal e vertical correspondentes com base na tecla pressionada.
A função principal run_game() inicia o loop do jogo. A posição inicial da cobra (x e y) é configurada no centro da tela. A velocidade inicial (speed_x e speed_y) é definida como zero, indicando que a cobra não está se movendo. A lista pixels armazena as coordenadas dos pixels da cobra.
O loop do jogo continua até que a variável end_game seja definida como True. No loop, a tela é preenchida com a cor preta usando screen.fill(BLACK).
O código responde aos eventos do jogador, como pressionar uma tecla para controlar a direção da cobra. Se a cobra ultrapassar as bordas da tela ou colidir consigo mesma, o jogo termina.
As posições da cobra são atualizadas com base nas velocidades horizontal e vertical. Novas posições são adicionadas à lista pixels e, se a cobra cresceu além do tamanho especificado, o pixel mais antigo é removido.
A cobra, a comida e a pontuação são desenhadas na tela usando as funções de desenho definidas anteriormente. A tela é atualizada com pygame.display.update().
Se a cobra colidir com a comida, seu tamanho aumenta e uma nova posição de comida é gerada aleatoriamente.
O loop é limitado pela função clock.tick(game_speed) para manter uma taxa constante de quadros por segundo.
No final do código, a função run_game() é chamada para iniciar o jogo.</h3>

### Tecnologias
---

Python

### Autor
---


 <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/91858793?v=4" width="100px;" alt=""/>
 <br />

Rafael Paim 👋🏽

[![Linkedin Badge](https://img.shields.io/badge/-Rafael-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rafael-paim-78274113b/)](https://www.linkedin.com/in/rafael-paim-78274113b/) 
[![Gmail Badge](https://img.shields.io/badge/-rafapaim92@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:rafapaim92@gmail.com)](mailto:rafapaim92@gmail.com)
