# Manim-project
This repository is for collaboration on a project using manim to create an instructive video for a topic related to maths / physics / anything really
If anyone is completely new to manim, here is the documentation for it: https://docs.manim.community/en/stable/

## Ideas
* Variational Calculus Problems
* Coordinate Transformations and Jacobian?
  *   Starting with substitution for single-variable integrals, introducing the concept of the Jacobian, and moving to multivariable integrals (Archit)
* Visualising certain proofs in Algebra / Set theory?
  *   e.g. Visualising the CSB proof may be an interesting idea (Anirudh)
* Visualising proofs related to AOC & Zorn
  *   e.g. Zorn's Lemma with the inclusion ordering - generating a visual intuition for the existence of a maximal element
  *   Zorn's Lemma with other kinds of ordering
  *   Orderings/Partial Orderings (Kevin)
  *   Transfinite induction
  *   ZFC + Choice vs ZFC + Not Choice 

## Collaboration Process
The file `scene_template.py` (thanks, Anirudh) details a workflow that would be quite useful for a Manim project with a lot of collaborators. I was too lazy to write this out myself so here's an AI summary:

### Template Architecture

- **Modular Design**: Animations are encapsulated in independent Creator classes (e.g., `CircleCreator`, `SquareCreator`) rather than monolithic Scene code
- **Dependency Injection**: Creator classes receive only three injected methods (`play`, `add`, `wait`) as constructor parameters—they don't inherit from Scene and have zero unnecessary overhead
- **Lightweight Classes**: Creators are minimal, focused classes containing only the animation logic for a specific diagram/simulation
- **Separation of Concerns**: 
  - **Developers** build Creator classes with complete animation logic
  - **Orchestrator** composes them in `MainScene.construct()`, controlling timing and order
- **Scalable Collaboration**: Multiple developers can work on different Creator classes in parallel without conflicts; orchestrator assembles them cleanly
- **Easy Testing**: Creators can be tested independently by passing mock functions instead of Scene methods
- **Clean Main Scene**: The main scene becomes a narrative outline rather than animation code—highly readable for understanding video flow
