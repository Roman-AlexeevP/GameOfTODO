CREATE TABLE IF NOT EXISTS game_hero (
    name TEXT NOT NULL UNIQUE ,
    current_level INTEGER DEFAULT 0,
    current_experience REAL DEFAULT 0
)