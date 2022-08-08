SELECT DISTINCT name
FROM authors
WHERE conference IN (SELECT conference
                     FROM conferences
                     WHERE area = 'systems')
          AND year < 1990
  AND name NOT IN (SELECT name
                   FROM authors
                   WHERE conference NOT IN (SELECT conference
                                            FROM conferences
                                            WHERE area = 'systems') OR year >=
                         1990)
ORDER BY name;