Meteor Shower Pygame Project

Description

This is an action-packed arcade-style game built with Pygame. 🚀 You control a spaceship and your mission is to survive a relentless meteor shower. Dodge and destroy the incoming meteors to achieve the highest score possible. The game features dynamic gameplay with meteors of various sizes, player movement, and shooting mechanics.

How to Play

    Move: Use the WASD keys to move your spaceship.

    Shoot: Press the spacebar to fire lasers and destroy meteors.

    Objective: Survive for as long as you can. The game ends when a meteor collides with your ship. Your score is based on the time you've survived.

Features

    Player Control: Smooth and responsive spaceship movement and shooting.

    Dynamic Meteors: Meteors spawn randomly from the top of the screen with varying sizes and speeds, breaking into smaller pieces when shot.

    Scoring: Your score is displayed in real-time and is based on the duration of your survival.

    Sound Effects: The game includes sound effects for shooting lasers and meteor explosions, enhancing the immersive experience.

    Graphics and Assets: The project uses custom sprites for the player, meteors, and a scrolling background to create a visually engaging space theme.

File Overview

    main.py: The main game script. It handles the game loop, event processing (like keyboard input), scoring, and initializes all game objects.

    player.py: Defines the Player class, which manages the spaceship's movement, shooting, and collision detection.

    laser.py: Defines the Laser class, controlling the behavior of the lasers fired by the player.

    meteor.py: Defines the Meteor class, which handles the movement, rotation, and destruction of meteors. It also includes logic for meteors breaking into smaller pieces.

    assets/ (folder): Contains all the visual and audio assets for the game, including:

        Images: player.png, background.png, meteor_large.png, meteor_small.png

        Sounds: laser.ogg, explosion.wav

        Icon: meteor_game.ico
