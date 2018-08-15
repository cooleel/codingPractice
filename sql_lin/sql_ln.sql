/* sql_coding
table name: article_views

date  viewer_id  article_id  author_id
2017-08-01  123  456 789
2017-08-02  432  543 654
2017-08-01  789  456 789
2017-08-03  567  780 432

How many article authors have never viewed their own article?

How many members viewed more than one article on 2017-08-01?
*/

--1
SELECT  COUNT(DISTINCT article_id )
FROM article_views
WHERE author_id NOT IN
(SELECT author_id
FROM article_views
WHERE author_id = viewer_id);

--2
SELECT COUNT(DISTINCT viewer_id)
FROM article_views
WHERE data = '2017-08-01'
GROUP BY viewer_id
HAVING COUNT(DISTINCT article_id) > 1;
