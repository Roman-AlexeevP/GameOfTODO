CREATE TABLE IF NOT EXISTS game_hero (
    uid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    current_level INTEGER DEFAULT 0,
    current_experience REAL DEFAULT 0
)