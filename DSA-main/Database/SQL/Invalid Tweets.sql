-- Find invalid tweets where the content exceeds 15 characters
-- Example: If the content of a tweet is "This is an invalid tweet because it is too long", it will be considered invalid.
-- Tweets with content length greater than 15 characters are considered invalid.
-- Table: Tweets
-- +----------------+---------+
-- | tweet_id       | content |
-- +----------------+---------+
-- | 1              | Hello!  |
-- | 2              | This is an invalid tweet because it is too long | 
-- +----------------+---------+




select tweet_id from Tweets where LENGTH(content) > 15;