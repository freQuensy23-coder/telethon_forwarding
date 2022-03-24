class MemoryList(list):
    """List, that save his state to memory"""

    def __init__(self, name, data=None):
        self.name = name
        data = data or []
        try:
            f = open(f"{name}.dat", "r")
        except FileNotFoundError:
            f = open(f"{name}.dat", "w")
            f.close()
            f = open(f"{name}.dat", "r")
        for line in f:
            data.append(line.strip())
        f.close()
        super(MemoryList, self).__init__(data)

    def append(self, __object: str) -> None:
        super(MemoryList, self).append(__object)
        with open(f"{self.name}.dat", "a") as f:
            f.write(__object + "\n")