-- =========================================================================
-- TASK 3: GA4 WEB TRAFFIC AD-HOC FUNNEL AGGREGATION QUERY
-- Objective: Filter and count unique users at each e-commerce milestone event.
-- =========================================================================

WITH RawWebEvents AS (
    SELECT 
        user_id,
        session_id,
        page_url,
        event_name,
        duration_seconds
    FROM virtualworks_ga4_stream
)

-- Aggregate milestone counts to feed our Python visualization pipeline
SELECT 
    COUNT(DISTINCT CASE WHEN event_name = 'view_item' THEN user_id END) AS unique_view_item_users,
    COUNT(DISTINCT CASE WHEN event_name = 'add_to_cart' THEN user_id END) AS unique_add_to_cart_users,
    COUNT(DISTINCT CASE WHEN event_name = 'begin_checkout' THEN user_id END) AS unique_begin_checkout_users,
    COUNT(DISTINCT CASE WHEN event_name = 'purchase' THEN user_id END) AS unique_purchase_users
FROM RawWebEvents;
