SELECT c."firstName", COUNT(o.address) AS orders FROM "Couriers" as c LEFT JOIN "Orders" as o ON c.id=o."courierId" WHERE o."inDelivery" is true GROUP BY c."firstName";
