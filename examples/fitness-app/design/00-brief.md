# Brief: Repwise (demo)

> Demo project for the `figma-app-design-builder` skill. The brief below is a sample answer to the Step 0 questions, written for this demonstration. [User brief · demo]

## Purpose
- **Who:** people aged 20–35 who go to the gym about 3 times a week and are past their first month, but still unsure what to do each session.
- **Problem:** they lose track of what they lifted last time, so they guess weights, skip progression and lose motivation.
- **Top tasks:**
  1. Start today's planned workout.
  2. Log each set (weight × reps) quickly, with a rest timer.
  3. See progress: personal records and weekly volume.

## Features (v1)
- Workout plans (3-day starter split; editable)
- Active workout logger with rest timer (a Live Activity while the timer runs)
- Exercise library with search
- Progress: weekly volume, personal records, session history
- Profile and settings
- Sign in with Apple, requested when the user first saves a workout (not at launch)
- Notifications: workout-day reminder only
- No payments in v1

## Feel
Calm, focused, serious but friendly. Not neon, not gamified. No brand colour or logo yet.

## Scope
iPhone only. Greyscale low fidelity first, then high fidelity.

## Site map

```
Onboarding (first launch, skippable, modal)
  ├── Goal (build strength / build muscle / stay consistent)
  └── Experience (new / some / regular)

Tab: Today
  └── Today                      home: today's workout, this week
      └── Workout Preview        drill-down: exercise list, Start
          └── Active Workout     modal (covers Tab Bar): log sets, rest timer
              └── Workout Summary  end of modal flow: PRs, volume, Save
                  └── Sign in with Apple sheet (first save only)

Tab: Library
  └── Exercises                  list + search + muscle filter
      └── Exercise Detail        drill-down: how-to, history for this lift

Tab: Progress
  └── Progress                   weekly volume, personal records
      └── Session Detail         drill-down: one past workout

Tab: Profile
  └── Profile & Settings
      ├── Plan settings          drill-down
      ├── Notifications          drill-down
      └── Account                drill-down: sign in / sign out / delete account

System
  └── Rest-timer Live Activity   Lock Screen + Dynamic Island
```
