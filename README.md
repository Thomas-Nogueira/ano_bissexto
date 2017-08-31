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
