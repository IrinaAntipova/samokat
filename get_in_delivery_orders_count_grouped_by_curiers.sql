SELECT c.login,
COUNT(o.id) AS “deliveryCount”
FROM "Couriers" as c
LEFT JOIN "Orders" as o ON c.id=o."courierId"
WHERE o."inDelivery" is true
GROUP BY c.login;
