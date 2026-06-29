# Trading Game Client

## Setup

```bash
git clone <this-repo>
cd gr_tradinggame_client
uv sync
```

## Usage

### 1. Edit `solution.py`

Write your strategy in the `play` method:

```python
class Solution:
    def __init__(self):
        self.history = []

    def play(self, reward, lockout, t, T, your_score, other_scores):
        self.history.append(reward)
        return reward > 1.5

play = Solution().play
```

Your function is called every round (including while locked out). Returning True while locked out has no effect but you still see the reward.

### 2. Test locally

```bash
uv run python test.py
```

Checks your function handles edge cases and runs fast enough.

### 3. Submit

Edit `submit.py` with your team name, password, and server address, then:

```bash
uv run python submit.py
```

You can resubmit as many times as you want. The server uses your latest submission.

### Password

Your password is set on your first submission. All future submissions for that team name must use the same password. Choose anything you like, just don't forget it.

## Parameters

| Parameter | Description |
|-----------|-------------|
| `reward` | The reward offered this round (float) |
| `lockout` | Rounds locked out if you accept (int) |
| `t` | Current round number, 1 to T (int) |
| `T` | Total rounds (int) |
| `your_score` | Your cumulative score (float) |
| `other_scores` | Other teams' scores (list of floats) |
