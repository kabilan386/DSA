-- Write your MySQL query statement below
-- Table Logs
-- id int
-- num int
-- Sample Input
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 2   |
-- | 6  | 2   |
-- Sample Output
-- +------------------+
-- | ConsecutiveNums |
-- +------------------+
-- | 1                |
-- | 2                |
-- +------------------+
-- 




select Distinct l1.num as ConsecutiveNums from Logs l1 join Logs l2 on l1.id + 1 = l2.id join Logs l3 on l2.id + 1 = l3.id where l1.num = l2.num and l2.num = l3.num