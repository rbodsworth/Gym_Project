DROP TABLE bookings;
DROP TABLE sessions;
DROP TABLE members;

CREATE TABLE members (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE sessions (
  id SERIAL PRIMARY KEY,
  category VARCHAR(255),
  name VARCHAR(255)
);

CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  member_id INT REFERENCES members(id) ON DELETE CASCADE,
  session_id INT REFERENCES sessions(id) ON DELETE CASCADE,
  review TEXT
);
