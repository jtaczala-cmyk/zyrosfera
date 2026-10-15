# Black Hole Transition — Specification

## Goal
A short (4–6 s) transition that feels physically and emotionally heavy. Not a simple fade. The player should feel the space bending.

## Visual sequence (timeline)

**0.0 – 0.8 s**  
Black hole appears at the exit point. Event horizon is a dark disk with a thin, bright accretion ring (blue-white). Space grid around it starts to stretch toward the center.

**0.8 – 2.5 s**  
Lumen is pulled in. Its internal filaments stretch and spin faster. Light from nearby crystals and the sphere stretches into long arcs (gravitational lensing). Bloom strength rises from normal to ~2.8.

**2.5 – 3.8 s**  
Maximum distortion. Screen edges show subtle chromatic aberration and warping. Color palette begins shifting toward the next sector. Low-frequency visual pulse (slight brightness oscillation).

**3.8 – 4.2 s**  
Near-silence moment. Bloom drops sharply. Almost black frame with only the stretched filaments still visible.

**4.2 – 5.5 s**  
Exit. New sector fades in. Bloom returns to normal. New ambient color and lighting. Crystals of the new sector appear with their own light.

## Audio
- Rising sub-bass drone (starts low, climbs slowly).
- High crystalline tones that stretch and detune.
- 0.4 s of near-silence right before exit.
- New sector ambient enters with a short reverb tail.

## Implementation notes for Stop60
- Use existing UnrealBloomPass; only increase strength during the transition.
- Distortion can be a simple full-screen shader or scaled UV offset on a plane in front of the camera.
- Do not add heavy particle systems during the transition (performance).
- Keep total duration under 6 seconds.
- Test on iPhone — if frame rate drops, reduce bloom resolution only during this sequence.

## What it should not be
- A simple black fade.
- A static image of a black hole.
- Overly long or unskippable.

This is a short, intense moment. Quality over quantity.
