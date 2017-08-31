# ano_bissexto

## Identificação

Objetivo: teste unitário em Python com Django
Problema: http://dojopuzzles.com/problemas/exibe/ano-bissexto/

## Plano de teste

| Entrada  | Condição | Classes Válidas | Classes Inválidas |
| ------------- | ------------- | ------------- | ------------- |
| ano           | ano ]0,infinito] | ano > 0 | ano <= 0 |
||| ano % 4 = 0 && ano % 100 != 0| ano % 4 != 0 |
||| ano % 100 = 0 && ano % 400 == 0| ano % 400 != 0 |
|| ano é do tipo Int | tipo(ano) == Int | tipo(ano) != Int |

```python
def is_bissexto(ano):
  return True
```

### 1º caso de teste (Tipo ano igual a int)

```python
is_bissexto(1) == True
```

### 2º caso de teste (Tipo ano diferente de int)

```python
is_bissexto("hu3hu3hu3") # Isso aqui lança uma exceção
```

### 3º caso de teste (Ano maior que zero)

```python
is_bissexto(4) == True
```

### 4º caso de teste (Ano menor ou igual a zero)
```python
is_bissexto(0) == False
```

### 5º caso de teste (Ano % 4 = 0 e Ano % 100 != 0)
```python
is_bissexto(4) == True
```

### 6º caso de teste (Ano % 100 = 0 e Ano % 400 = 0)
```python
is_bissexto(400) == True
```

### 7º caso de teste (Ano % 4 != 0)
```python
is_bissexto(5) == False
```

### 8º caso de teste (Ano % 400 != 0 )
```python
is_bissexto(500) == False
```
