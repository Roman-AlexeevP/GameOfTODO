CREATE TABLE IF NOT EXISTS tasks (
    uid INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    hours_to_complete INTEGER NOT NULL ,
    priority_type INTEGER NOT NULL ,
    ended_at DATETIME,
    is_active TINYINT NOT NULL DEFAULT 0,
    is_complete TINYINT NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL,
    worked_hours INTEGER

)