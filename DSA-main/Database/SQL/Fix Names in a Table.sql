-- Write an SQL query to fix the names in the Users table. The first letter should be capitalized, while the rest of the name should be in lowercase.
-- Users Table:
-- +---------+---------+
-- | user_id | name    |
-- +---------+---------+
-- | 1       | alice   |
-- | 2       | BOB     |
-- | 3       | ChArLiE |
-- +---------+---------+

-- Output:
-- +---------+---------+
-- | user_id | name    |
-- +---------+---------+
-- | 1       | Alice   |
-- | 2       | Bob     |
-- | 3       | Charlie |
-- +---------+---------+



select user_id,CONCAT(UPPER(SUBSTRING(name,1,1)),LOWER(SUBSTRING(name,2))) as name from Users order by user_id