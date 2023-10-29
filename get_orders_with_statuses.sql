SELECT o.track, (case when o.finished is true then 2 when o.cancelled is true then -1 when o."inDelivery" is true then 1 end) as status  FROM "Orders" AS o;
