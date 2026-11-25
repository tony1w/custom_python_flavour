# PyX language features demonstration
strict on

let age: int = 20
let numbers = [1, 2, 3, 4, 5]

fn double(x):
    give x * 2

fn keep_even(values):
    give [x for x in values if x % 2 == 0]

let answer = numbers |> keep_even |> sum
show("Sum of doubled? (pipeline demo):", answer)
show("Age:", age)

when age >= 18:
    show("Adult")
otherwise:
    show("Minor")
