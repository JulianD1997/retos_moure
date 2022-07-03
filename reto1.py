"""/*
 * Reto #1
 * ¿ES UN ANAGRAMA?
 * Fecha publicación enunciado: 03/01/22
 * Fecha publicación resolución: 10/01/22
 * Dificultad: MEDIA
 *
 * Enunciado: Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
 * Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
 * NO hace falta comprobar que ambas palabras existan.
 * Dos palabras exactamente iguales no son anagrama.
 *
 * Información adicional:
 * - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
 * - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
 * - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
 * - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
 *
 */"""
from operator import truediv


def anagram (word_one, word_two):
    if (word_one == word_two) or (len(word_one) != len(word_two)):
        return False
    else: 
        word_one = list(sorted(word_one))
        word_two = list(sorted(word_two))
        if word_one == word_two:
            return True
        else:
            return False
finalize = True
while finalize:
    first_word = input("Ingresa la primer palabra : ").upper()
    second_word = input("Ingresa la segunda palabra : ").upper()
    if anagram(first_word, second_word):
        print(f"{first_word} y {second_word} son anagrama")
    else :
        print(f"{first_word} y {second_word} no son anagrama")
    """
    if first_word == second_word :
        print("No son Anagrama")
    else :
        first_word = list(sorted(first_word))
        second_word = list(sorted(second_word))
        for i in range(len(first_word)):
            if first_word[i] == second_word[i]:
                continue    
            else :
                print("No son anagrama")
                break
        print("Son anagrama")"""
    finalize = False if input("¿finalizar (S/N)? :").lower() == "s" else True
