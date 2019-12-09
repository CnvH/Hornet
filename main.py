import machine
import pyb
import vespa


if __name__ == '__main__':
    print('main executing...')

x = Ring(4)
x.status()
for j in range(1, 3):
    x.add_head(j)
    x.status()
print('Popped from Head : ', x.pop_head()[1])
x.status()

print('Popped from tail : ', x.pop_tail()[1])
x.status()

print('Popped from Head : ', x.pop_head()[1])
x.status()

print('Popped from Head : ', x.pop_head()[1])
x.status()

for j in range(1, 4):
    x.add_head(j)
    x.status()
print('Popped from Head : ', x.pop_head()[1])
x.status()

print('Popped from tail : ', x.pop_tail()[1])
x.status()

print('Popped from Head : ', x.pop_head()[1])
x.status()

print('Popped from Head : ', x.pop_head()[1])
x.status()
