-- Script that selects the number of band fans per country,
-- From a table of bands profile including their number of fans

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands 
GROUP BY origin 
ORDER BY nb_fans DESC;
