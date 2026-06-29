-- Example SQL query to get unique leads and partners by date and make
-- This query counts the distinct lead_id and partner_id for each combination of date_id and make_name in the DailySales table.
-- Table: DailySales
-- +---------+-----------+---------+------------+
-- | date_id | make_name | lead_id | partner_id |
-- +---------+-----------+---------+------------+
-- | 2024-01-01 | Toyota    | 1       | 101        |
-- | 2024-01-01 | Toyota    | 2       | 102
-- | 2024-01-01 | Honda     | 3       | 103
-- | 2024-01-02 | Toyota    | 4       | 104
-- +---------+-----------+---------+------------+




select date_id , make_name , count(distinct lead_id) as unique_leads, count(distinct partner_id) as unique_partners from DailySales group by date_id , make_name  
