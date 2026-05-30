-- 1. Total de clientes
SELECT COUNT(*) AS total_clients
FROM bank_marketing;

-- 2. Clientes por estado civil
SELECT marital, COUNT(*) AS total
FROM bank_marketing
GROUP BY marital
ORDER BY total DESC;

-- 3. Clientes por profissão
SELECT job, COUNT(*) AS total
FROM bank_marketing
GROUP BY job
ORDER BY total DESC;

-- 4. Resultado da campanha
SELECT y, COUNT(*) AS total
FROM bank_marketing
GROUP BY y
ORDER BY total DESC;

-- 5. Média de saldo por profissão
SELECT job,
       ROUND(AVG(balance)::numeric,2) AS avg_balance
FROM bank_marketing
GROUP BY job
ORDER BY avg_balance DESC
LIMIT 10;

-- 6. Média de idade por estado civil
SELECT marital,
       ROUND(AVG(age)::numeric,2) AS avg_age
FROM bank_marketing
GROUP BY marital
ORDER BY avg_age DESC;

-- 7. Top 10 maiores saldos
SELECT age, job, balance
FROM bank_marketing
ORDER BY balance DESC
LIMIT 10;

-- 8. Contactos por mês
SELECT month, COUNT(*) AS total
FROM bank_marketing
GROUP BY month
ORDER BY total DESC;

-- 9. Número médio de contactos por campanha
SELECT ROUND(AVG(campaign)::numeric,2) AS avg_campaign_contacts
FROM bank_marketing;

-- 10. Subscrições por profissão
SELECT job,
       COUNT(*) FILTER (WHERE LOWER(y) LIKE '%yes%') AS subscribed,
       COUNT(*) FILTER (WHERE LOWER(y) LIKE '%no%') AS not_subscribed
FROM bank_marketing
GROUP BY job
ORDER BY subscribed DESC;