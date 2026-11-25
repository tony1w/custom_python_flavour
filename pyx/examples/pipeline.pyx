# Pipeline stages receive the previous result as their first argument.
fn add_ten(value):
    give value + 10

fn multiply(value, factor):
    give value * factor

let result = 5 |> add_ten |> multiply(3)
show(result)  # 45
