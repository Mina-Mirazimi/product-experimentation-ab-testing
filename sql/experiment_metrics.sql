SELECT treatment,
COUNT(*) AS users,
AVG(purchased * 1.0) AS conversion_rate,
AVG(orders * 1.0) AS orders_per_user,
AVG(revenue * 1.0) AS revenue_per_user,
AVG(engaged_7d * 1.0) AS engagement_7d_rate,
AVG(refund * 1.0) AS refund_rate,
AVG(support_contact * 1.0) AS support_contact_rate
FROM rewards_experiment
GROUP BY treatment
ORDER BY treatment;
