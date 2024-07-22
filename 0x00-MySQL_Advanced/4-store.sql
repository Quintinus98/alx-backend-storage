-- A script that creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER add_order AFTER INSERT ON orders FOR EACH ROW UPDATE items SET quantity = quantity - 1 WHERE name = NEW.item_name;
