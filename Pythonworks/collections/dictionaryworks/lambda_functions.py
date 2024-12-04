

box=[
    {"color":"green","size":2},
    {"color":"green","size":7},
    {"color":"blue","size":1},
    {"color":"blue","size":5},
    {"color":"yellow","size":3},
    {"color":"yellow","size":8},
]

sizes=[b.get("size") for b in box]

print(sizes)