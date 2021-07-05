# Objects

Objects are used to model things in code. Can be a physical item, ie a display screen or a digital unit, ie bank account, enemy in a computer game.
Objects are groups of data and functions (methods). These functions are specifically designed to interact with that object only.
Everything is an object in Python.

## Digital Objects

```
numbers = [1, 2, 3]
```

numbers is a list object which contains both data and methods, such as the append method

```
numbers.append(4)
# numbers would now look like [1, 2, 3, 4]
```

## Real-world Objects

In the case of wiring up an LED to a Raspberry Pi computer. Lets say we connected the LED to pin 17. To turn on the LED our code would need to look like:

```
from gpiozero import LED
red = LED(17)
red.on()
```

LED objects have an on method to turn them on within Python. If we had another LED wired up to pin 21, for example, we could create another object such as `green = LED(21)`.
By using methods, such as the `.on()` method, we gain some benefits from the use of abstraction. We don't need to know exactly what is going on under the hood, but we know that by using this method, our desired outcome will be achieved.
