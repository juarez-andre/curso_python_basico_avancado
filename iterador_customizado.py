"""
Escrevendo um iterador customizado

OBS: No momento não preciso me preocupar com o conteúdo de Classes/Orientação a Objeto. O objetivo da aula
é mostrar que para que eu crie um iterador customizado, basta que eu tenha os métodos _iter_ e _next_.


class Contador:
    def _init_(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def _iter_(self):
        return self

    def _next_(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


con = Contador(1, 6)

it = iter(con)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

for n in Contador(1, 61):
    print(n)

for n in range(1, 61):
    print(n)
"""

