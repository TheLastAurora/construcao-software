import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]
    
    return quick_sort(smaller) + equal + quick_sort(larger)

class TesteOrdenacao:
    def __init__(self):
        self.tamanhos = [100, 1000, 10000]
    
    def gerar_vetor(self, tamanho):
        return [random.randint(1, 1000) for _ in range(tamanho)]
    
    def executar_teste(self, algoritmo, tamanho):
        vetor = self.gerar_vetor(tamanho)
        
        inicio = time.time()
        algoritmo(vetor)
        fim = time.time()
        
        tempo_execucao = fim - inicio
        print(f"Tempo de execução do algoritmo {algoritmo.__name__} para vetor de tamanho {tamanho}: {tempo_execucao:.6f} segundos")
    
    def executar_testes(self):
        for tamanho in self.tamanhos:
            vetor = self.gerar_vetor(tamanho)
            print(f"Vetor original: {vetor}")
            
            print("Executando MergeSort:")
            self.executar_teste(merge_sort, tamanho)
            print()
            
            print("Executando QuickSort:")
            self.executar_teste(quick_sort, tamanho)
            print()
            print("=" * 40)
            print()

teste = TesteOrdenacao()
teste.executar_testes()
