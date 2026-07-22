# Python Pygame Game -- Project Rubric

In this project, you will create a 2D game using pygame. Think about classic
games like Pong, Pacman, Snake, or Space Invaders -- or invent something
entirely new.

## Deliverables

- All files in a clearly labelled folder in your GitHub repository (e.g.,
  `pygame/`)
- A complete game written in Python with pygame
- A completed README.md with the questions below answered

---

### 1) Project Overview [Understanding context / defining / ideating]

**What game did you build?** Describe the core concept, objective, and basic
gameplay.
>> Playing with the word "dreamcatcher", I built a catching game in which the player's objective is to score as many feathers (falling from the sky) as possible while dodging ghosts (also falling from the sky) and also obtaining stars (also falling from the sky), I'll explain what each element does in the question below.

**What inspiration did you build off of?** Identify what existing game or
idea inspired you and what changes you made to the original concept.
>> I remember from my childhood that I used to play a catching game where eggs fell from the sky and you had to catch them into a basket by holding either the left/right side of the screen to use. On the contrary, my game differed from the original by introducing additional falling elements (stars for extra lives, ghosts for deducting lives) and game states (lucid dreaming and nightmares) which amp up the difficulty (at least for me).

*Extending signal:* The game features a creative twist, original mechanic,
or unexpected design element that shows genuine ideation beyond a standard
implementation.

---

### 2) Game Design and Mechanics [Prototyping / Making]

**Game Loop and Frame Regulation**
- Does your game maintain a stable game loop with
  `pygame.time.Clock().tick()`?
>> yes
- Is rendering order correct (clear -> update -> draw -> flip)?
>> yes

**Player Controls and Movement**
- How does the player control their character? Describe the control scheme.
>> there are multiple controls for the game, which include:
>> esc key: resets back to the main menu, this is available throughout all stages of the gameplay (in case you're losing really really bad jk)
>> space key: move to character selection
>> left and right arrow keys: switch between the male and female characters
>> enter: choose character and move to game
>> a key: moves the character left
>> d key: moves the character right
- Is movement smooth and bounded within the screen?
>> yes

**Collision Detection**
- What type of collision detection does your game use (rect-based,
  distance-based)?
>> rect-based
- Describe at least one collision interaction in your game (player-enemy,
  player-item, etc.).
>> there are 3 types of collisions: with the feathers, stars, and ghosts
>> feathers: the feather must come into contact with the basket of the player sprite for the score count to go up by 1
>> stars: the star can collide with any part of the player sprite for the lives count to go up by 1
>> ghosts: the ghost vary in size, in which they can collide with any part of the player sprite  for the lives count to go down by 1

**Game State Management**
- Does your game have distinct states (e.g., menu / playing / game over)?
>> The gameplay includes a main menu, character selection (in which the player has the choice between a male and female character), the game itself, and a game over screen.
>> I also added different "special" states: lucid dreams (the feathers and stars drop like crazy bro it's basically heaven) and nightmares (i've tried surviving it and it's literally impossible but that's ok, the only time i did was when i added 30 lives and i still died within 2 mins).
- How does the game handle win/lose conditions?
>> there are no win conditions, the game just loops infinitely until the lives count hits 0, which switches to the game over menu and prompts the user to click esc to return back to the main menu
- Can the player restart without crashing?
>> yes, just click escape

*Extending signal:* The game goes beyond basic mechanics with a notable
technical or design achievement -- such as intelligent enemy AI (state-based
behaviour, pathfinding), custom physics (gravity, acceleration, friction),
procedural level generation, a save/load system, an original mechanic not
derived from the archetype, or polished game feel with screenshake,
particles, or timed animations.

---

### 3) Programming and Code Quality [Making]

- **Pygame usage:** Code correctly initialises and uses pygame modules
  (display, event, key, sprite, font, etc.) and follows the proper game loop
  pattern.
- **Functions and modular design:** Code is broken into well-named functions
  with clear separation of logic -- for example, separate functions for
  initialisation, input handling, update logic, rendering, and state
  transitions.
- **Readability:** Code is commented where needed, uses descriptive variable
  names, and follows consistent formatting. Constants are defined at the top
  (e.g., `SCREEN_WIDTH`, `PLAYER_SPEED`, `FPS`).
- **Sprites and assets:** Image sprites (loaded via `pygame.image.load()` or
  created with `pygame.Surface`) or drawn shapes are used for game entities
  rather than hardcoded pixel coordinates throughout.

*Extending signal:* Clear, well-organised code that is easy to read and
maintain -- includes a dedicated module structure (e.g., separate files for
settings, sprites, game state), uses `pygame.sprite.Sprite` classes with
proper `Group` objects for entity management, and demonstrates efficient
rendering practices (e.g., using `convert_alpha()` for performance).

---

### 4) Testing, Debugging, and Documentation [Testing]

**Stability and Polish**
- The game can be played through without crashes, soft-locks, or easily
  encounterable bugs.
- Common failure modes are handled (rapid key presses, edge-of-screen
  objects, restarting mid-game).

**Test Evidence**
- Describe at least one test you ran on a specific game mechanic (e.g.,
  collision detection, boundary clamping, score increment) and explain why
  this test demonstrates the code works correctly.
  >> I had trouble with the different states in the actual game, in which the supposed 20 second grace period never occurred after one of the special events (lucid dreaming or nightmare) and kept alternating between the two.
  >> To fix this, I implemened pygame.time.get_ticks() to track time and implement a cooldown timer for 20000 ms (20 secs) before spawning another event.
- Describe at least one test of your game's state transitions (e.g.,
  menu -> playing -> game over -> restart) and why it shows the game handles
  edge cases properly.
>> I emptied all my spawned sprites (feathers, ghosts, and stars) before escaping the game and going through the main menu, character selection, and gameplay again, in which new sprites were spawned and scores/lives were reset.

**Known Bugs and Limitations**
- What bugs or edge cases remain in your game? What would you fix with more
  time?
>> Something that troubles me is that there are two transparent corners on the ghosts (bottom left and top right) that are transparent, but still trigger and take away a life, which I would ideally like to fix.
>> When you die during a nightmare and you restart back through the m.m. and c.s., it starts you back mid-nightmare and I can't figure out how to fix it. I tried making the mode back to normal under the "if game_state = "playing"", but it then bugs the program by spawning any special event for like 1 second and then it goes poof.

**Timing / Profiling (optional but encouraged)**
- Profile your game's frame rate under different conditions. Report average
  FPS or identify frames where the frame rate drops noticeably. What part of
  the game is most demanding, and why?

*Extending signal:* The game is robust and polished -- extensive edge-case
testing shows thorough validation, and profiling is used to identify and
resolve a specific performance bottleneck. May have bugs, but these are known
and documented.

---

### 5) Collaboration and Process [Sharing]

**Challenge faced:** What was a challenge you encountered while building your
game? How did you overcome it? (e.g., debugging a collision bug, designing a
game mechanic, managing sprite assets)
>> The bounds for my game. At the beginning of my troubleshooting, the sprite.rect would hit 0 and get stuck there (which I fiddled with the numbers to fix); meanwhile, it would travel outside the bounds despite me having a restriction at 900. I realised then that I did not take into account that the sprites have a width, in which the restriction only applied for the leftmost pixels of the sprite. Additionally, I later found that the sprites have different widths because the girl's hair was so much more volumptuous compared to the boy.
>> I fixed the issue setting a separate restriction for the each sprite so that the right restriction was the screen width (900) - the sprite's width.

**Future work:** If you had more time, what would you add or improve in your
game?
>> I would add a saving system so that the scores could be documented to perhaps a text file. This allows players to compared their scores and try to beat their pb's.

**Tool/Person-Use Statement** (bullet points; required for each tool or
person used)
- Tool / Person: the function pygame.sprite.Group()
- Used for: container class to store and manage sprites
- What I learned from the tool or person: how to spawn and manage all of the feathers, ghosts, and stars respectively in their own categories, especially given the different special game events (lucid dreaming (no ghosts, tons of stars and feathers) and nightmares (no stars or feathers, just pure death))

*Extending signal -- growth:* Identifies clear growth and lessons learned
through the project, with a specific plan for future improvement.

*Extending signal -- collaboration:* Sought out and provided peer collaboration (peer review)
that measurably improved the game (e.g., a bug fixed, a feature added, or a
design improved based on peer feedback).

*Extending signal -- resourcefulness:* Demonstrates effective use of external
tools or references (documentation, tutorials, forums) that improved the
design, build, or testing process.

---

### 6) Ready-to-submit Checklist

- [ ] Game runs without errors and is playable from start to finish
- [ ] Game includes a stable game loop with regulated frame rate
- [ ] Player controls are implemented and responsive
- [ ] At least one collision interaction is implemented (player-enemy,
      player-item, player-wall, etc.)
- [ ] Game has distinct start/end states (menu, game over, or win condition)
- [ ] Score, timer, or lives are displayed on screen
- [ ] Game is easy to understand -- either intuitive to play or includes
      clear instructions (on-screen text or a start screen explaining
      controls and objective)
- [ ] Code is split into functions with clear separation of logic
- [ ] Code is commented and uses clear variable names
- [ ] README.md completed with all sections answered
- [ ] Peer review complete (both gave and received peer feedback)
- [ ] All files are in a clearly labelled folder (e.g., `pygame/`) in your
      GitHub repository

---

### 7) Grading

Proficient is the target. Extending signals are an indication of extending
level work; not all signals are required for an extending grade. Other
signals not indicated may also be worthy of an extending grade.

Your grade will be assigned a proficiency based on evidence of each of the
curricular competencies demonstrated (indicated generally by square
brackets):

- Emerging: 3/10
- Developing: 6/10
- Proficient: 9/10
- Extending: 10/10

The competencies assessed are:
- Understanding context / defining / ideating
- Prototyping
- Making
- Testing
- Sharing