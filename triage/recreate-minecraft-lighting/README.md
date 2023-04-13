# Recreate Minecraft's lighting.

https://codegolf.stackexchange.com/questions/245451/recreate-minecrafts-lighting.

Minecraft has a fairly unique lighting system. Each block's light value is either one less than the brightest one surrounding it, or it is a light source itself. Your task is to write a method that takes in a 2D array of light source values, and then returns a 2D array with spread out lighting, where 0 is the minimum value.

```
Input1 = [
         [0, 0, 4, 0], 
         [0, 0, 0, 0], 
         [0, 2, 0, 0], 
         [0, 0, 0, 0]
        ]

Output1 = [
         [2, 3, 4, 3], 
         [1, 2, 3, 2], 
         [1, 2, 2, 1], 
         [0, 1, 1, 0]
        ]

Input2 = [
         [2, 0, 0, 3], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0], 
         [0, 0, 0, 0]
        ]

Output2 = [
         [2, 1, 2, 3], 
         [1, 0, 1, 2], 
         [0, 0, 0, 1], 
         [0, 0, 0, 0]
        ]
```

**Notes**

You can assume:

1. Input will not be empty.
2. The y axis will be the same length.
3. All numbers will be integers; no nulls, doubles, or floats.
4. All numbers will be between 0 and 15 (inclusive).

Rules:

1. Return a 2D array following the above mechanics.
2. No value can be less than 0.
3. If there are two highest neighbors, just subtract one from them.
4. Light sources do not change, unless a surrounding block is brighter than it.
5. No standard loopholes.
6. This is code golf, so shortest code wins!