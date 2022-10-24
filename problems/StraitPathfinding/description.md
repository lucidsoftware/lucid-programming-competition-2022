# Strait Pathfinding

You're in charge of getting a motorboat back through a busy strait. However,
the strait is *very* busy, and you don't have much fuel. How much fuel will it
take to get you back to port?

## Input

You'll get an input like this:

```
Width of Port
Length of Port
Map of Port
```

The length and width of the strait will be integers. The map of the port will
be a `length` $\times$ `width` set of characters representing the strait. The following
characters will be used:

* `v` for a boat that begins travelling downwards
* `^` for a boat that begins travelling upwards
* `x` for an obstacle that stays in place
* `~` for open water
* `@` for your starting position

For example:

```
5
10
~~~~~~~~~~
~~~~~~x~~~
@~~v~~~~~~
~~~~~~~~x~
~~~~~~^~~~
```

Your goal will always be to get across the east (rightmost) edge of the strait,
or in other words to move off the right side of the given map.

## Output

You'll output the minimum amount of fuel required to return to port. You are
allowed to remain in place or move orthagonally (up, down, right, and left) but
not diagonally. You use one unit of fuel regardless of if you move or remain
in place.

## Example Inputs and Outputs

**Input 1:**

```
3
5
~~^~~
@~~~~
~~~~~
```

**Output 1:**

```
6
```

**Input 2:**

```
5
10
~~xx~~x~~~
~~~^~~~~~~
@~~~~~~~~~
~~~~~~~~~~
~~~xx~~x~^
```

**Output 2:**

```
10
```

## Boat Rules

You (`@`) and the other boats move at the same time. This means that moving into
a space that was previously occupied by another boat is legal; in this case you
pass by the other boat harmlessly:

```
~~~      ~~~
~@~  =>  ~^~ 
~^~      ~@~
```

Staying in place when another boat would collide with you is an invalid move:

```
~~~      ~~~
~@~  =>  ~!~
~^~      ~~~
```

Boats will avoid collisions with the sides or obstacles by turning around in
place instead of moving:

```
~~~      ~~~
~v~  =>  ~^~
~x~      ~x~
```

```
~~~      ~~~
~~~  =>  ~~~
~v~      ~^~
--- edge ---
```

## Constraints

* $w \leq 10$
* $l \leq 30$
* $n_{\textrm{boats}} \leq l$
* $n_{\textrm{obstacles}} \leq l \times 2$
* Each strait will have a valid path
* Each column of the strait will have at most one boat