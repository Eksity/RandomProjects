class Jar:
    def __init__(self, cookies, capacity):
        self.capacity = capacity
        self.cookies = cookies
    
    def __str__(self):
        return '🍪' * self.cookies   

    def deposit(self, n):
        self.cookies += int(n)

    def withdraw(self, n):
        self.cookies -= int(n)

    @property
    def cookies(self):
        return self._cookies

    @property
    def capacity(self):
        return self._capacity

    @cookies.setter
    def cookies(self, cookies):
        if cookies > self.capacity:
            raise ValueError("Too many cookies")
        elif cookies < 0:
            raise ValueError("Negative cookies")
        self._cookies = cookies
    
    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Cookie jar too small")
        self._capacity = capacity


if __name__ == "__main__":
    x = Jar(0, 2)
    print(x)