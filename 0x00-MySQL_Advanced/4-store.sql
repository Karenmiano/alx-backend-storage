-- Script that creates a trigger that decreases the quantity of
-- an itemafter adding a new order

CREATE TRIGGER update_quantity AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
