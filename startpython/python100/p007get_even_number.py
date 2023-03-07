# liebiaotuidaoshi

def even_number(paramsbegin, paramsend):
    sum = 0
    outcome = []
    for item in range(paramsbegin, paramsend):
        if (item % 2) == 0:
            outcome.append(item)
            sum += 1
    return sum, outcome
begin = 4
end = 15

print(f"begin = {begin}, end = {end}, even_number = {even_number(begin, end)}")
data = [item for item in range(begin,end) if item %2 ==0]
print(f"begin = {begin}, end = {end}, even_number = {data}")