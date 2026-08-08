# Public-Good-Game

Public Goods Game practice apps for [oTree](https://www.otree.org/) (compatible with **oTree 6**).

This repository is a self-contained oTree project with two practice/tutorial rounds, meant to run before
the real economic experiment so participants can familiarize themselves with the rules. Both apps use
sliders/number inputs so a single participant can set their own decision *and* the decisions of three
simulated co-players, then see the resulting payoffs.

**Note:** as programmed, neither practice round stores player decisions in the database, since they're
only meant for participants to get familiar with the game. If you want to record decisions, add the
corresponding fields to the `Player` model and wire them into the page's `form_model` / `form_fields`
and template.

## Apps

### `public_goods_practice`

A standard public goods game. You decide your own contribution and the contributions of 3 simulated
co-players, then see everyone's payoff.

Parameters (`public_goods_practice/__init__.py`, `class C`):
- Players per group: 4
- Endowment: 20
- Efficiency factor (marginal per-capita return): 0.4

### `public_goods_punishment_practice`

A public goods game with costly punishment (Fehr & Gächter, 2000). After the contribution phase, you can
pay to reduce the payoff of one or more co-players; the simulated co-players in turn punish contributions
below the group average, so you also experience being on the receiving end.

Parameters (`public_goods_punishment_practice/__init__.py`, `class C`):
- Players per group: 4
- Endowment: 20
- Efficiency factor: 0.5
- Simulated co-player contributions: 0, 10, 20 (fixed, so outcomes are reproducible)
- Punishment cost ratio: 0.5 UM spent per UM removed from a target's payoff
- Max punishment per target: 20 UM

Both apps have an easily editable 5-minute timeout (`timeout_seconds` in each app's `__init__.py`).

## Project structure

- `settings.py` — oTree/project settings (session configs, admin credentials, secret key).
- `public_goods_practice/` and `public_goods_punishment_practice/` — the two oTree apps:
  - `__init__.py` — app definition (constants, models, page sequence).
  - `Practice.html` — the practice page template (layout and payoff-calculation script).
- `_static/global/practice.css` — shared styling (cards, sliders, tables, dark mode) used by both apps.
- `requirements.txt` — pinned to `otree>=6.0,<7.0`.

## Running locally

```bash
pip install -r requirements.txt
otree devserver
```

Then open the app in the browser at the URL oTree prints (typically `http://localhost:8000`).

Before deploying anywhere public, override the demo defaults via environment variables:

```bash
export OTREE_ADMIN_PASSWORD="choose-a-strong-password"
export OTREE_SECRET_KEY="generate-a-new-random-string"
```

## License

Released under the [MIT License](LICENSE).
